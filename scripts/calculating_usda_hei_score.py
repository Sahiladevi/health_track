import pandas as pd
import numpy as np
from pathlib import Path

from config import (RAW_DATA_DIR, CLEAN_DATA_DIR, PROCESSED_DATA_DIR)
from data_loading import load_dataset
from utils import pretty_path, explore_data

def calculate_hei_scores(
    clean_data_dir=CLEAN_DATA_DIR,
    processed_data_dir=PROCESSED_DATA_DIR,
    save_csv=True
):
    """
    Calculate Healthy Eating Index (HEI) 2015 scores for participants based on NHANES dietary data.

    This function loads cleaned NHANES individual foods and total nutrient datasets, along with the
    Food Patterns Equivalents Database (FPED). It merges these datasets, calculates nutrient totals
    and densities per 1000 kcal, and computes component HEI scores for each participant.

    Scores are combined into a total HEI score and categorized as 'Poor', 'Needs Improvement', or 'Good'.
    
    Args:
        raw_data_dir (Path): Directory containing raw datasets (e.g., FPED Excel file).
        clean_data_dir (Path): Directory containing cleaned NHANES datasets (CSV files).
        processed_data_dir (Path): Directory where the output CSV file will be saved.
        save_csv (bool): Whether to save the resulting DataFrame as a CSV file.

    Returns:
        pd.DataFrame: DataFrame containing HEI component scores, total HEI score, and diet quality categories
                      for each participant.

    Raises:
        RuntimeError: If any of the required datasets fail to load.
    """
    
    # Load the data
    dr1iff = load_dataset(clean_data_dir / "dr1iff_l_clean.csv")
    dr1tot = load_dataset(clean_data_dir / "dr1tot_l_clean.csv")
    fped = load_dataset(clean_data_dir / "fped_1720_clean.csv")

    if dr1iff is None or dr1tot is None or fped is None:
        raise RuntimeError("One or more datasets failed to load. Please check paths and formats.")

    # Merge NHANES Individual Foods with FPED on food code
    print("Merging NHANES Individual Foods with FPED using food codes...")
    merged = pd.merge(dr1iff, fped, left_on="food_code", right_on="FOODCODE", how="inner")

    """# Clean FPED column names
    merged.columns = merged.columns.str.replace(r"\s+\(.*\)", "", regex=True)"""
    
    nutrient_cols = [
        'F_TOTAL', 'F_JUICE', 'F_CITMLB', 'F_OTHER',
        'V_TOTAL', 'V_DRKGR', 'V_LEGUMES',
        'G_WHOLE', 'G_REFINED',
        'D_TOTAL', 'D_MILK', 'D_YOGURT', 'D_CHEESE',
        'PF_TOTAL', 'PF_MPS_TOTAL', 'PF_SEAFD_HI', 'PF_SEAFD_LOW',
        'SOLID_FATS', 'ADD_SUGARS', 'OILS'
    ]

    for col in nutrient_cols:
        merged[col + "_TOT"] = merged[col] * merged["grams_consumed"] / 100

    merged["energy"] = merged["energy_kcal"]

    print("\n------------Aggregate Nutrients and Energy by Participant------------------------\n")

    agg_cols = [col + "_TOT" for col in nutrient_cols] + ["energy"]

    dietary_weight_per_person = merged.groupby("participant_id")["food_item_weight"].sum().reset_index()
    person_level = merged.groupby("participant_id")[agg_cols].sum().reset_index()

    for col in nutrient_cols:
        person_level[col + "_PER1000KCAL"] = person_level[col + "_TOT"] / (person_level["energy"] / 1000)

    dr1tot["SODIUM_PER1000KCAL"] = (dr1tot["sodium_mg"] / dr1tot["energy_kcal"])
    dr1tot["SAT_FAT_PCT_ENERGY"] = (dr1tot["satfat_g"] * 9 / dr1tot["energy_kcal"]) * 100

    person_level = person_level.merge(
        dr1tot[["participant_id", "SODIUM_PER1000KCAL", "SAT_FAT_PCT_ENERGY", "total_diet_weight"]],
        on="participant_id", how="left"
    )

    person_level = person_level.merge(dietary_weight_per_person, on="participant_id", how="left")

    def score_component(val, min_val, max_val, reverse=False, max_score=10):
        if pd.isna(val):
            return 0
        if reverse:
            if val <= max_val:
                return max_score
            elif val >= min_val:
                return 0
            else:
                return max_score * (min_val - val) / (min_val - max_val)
        else:
            if val >= max_val:
                return max_score
            elif val <= min_val:
                return 0
            else:
                return max_score * (val - min_val) / (max_val - min_val)

    df = person_level.copy()

    df['fatty_acid_ratio'] = np.where(
        df['SOLID_FATS_PER1000KCAL'] == 0,
        np.nan,
        df['OILS_PER1000KCAL'] / df['SOLID_FATS_PER1000KCAL']
    )

    df['hei_fatty_acid'] = df['fatty_acid_ratio'].apply(lambda x: score_component(x, 1.2, 2.5, max_score=10))

    df['hei_total_fruit'] = df['F_TOTAL_PER1000KCAL'].apply(lambda x: score_component(x, 0, 0.8, max_score=5))
    df['hei_whole_fruit'] = df['F_OTHER_PER1000KCAL'].apply(lambda x: score_component(x, 0, 0.4, max_score=5))
    df['hei_total_veg'] = df['V_TOTAL_PER1000KCAL'].apply(lambda x: score_component(x, 0, 1.1, max_score=5))
    df['hei_greens_beans'] = (df['V_DRKGR_PER1000KCAL'] + df['V_LEGUMES_PER1000KCAL']).apply(lambda x: score_component(x, 0, 0.2, max_score=5))
    df['hei_whole_grains'] = df['G_WHOLE_PER1000KCAL'].apply(lambda x: score_component(x, 0, 1.5, max_score=10))
    df['hei_dairy'] = df['D_TOTAL_PER1000KCAL'].apply(lambda x: score_component(x, 0, 1.3, max_score=10))
    df['hei_total_protein'] = df['PF_TOTAL_PER1000KCAL'].apply(lambda x: score_component(x, 0, 2.5, max_score=5))
    df['hei_sea_plant_protein'] = (df['PF_SEAFD_HI_PER1000KCAL'] + df['PF_SEAFD_LOW_PER1000KCAL']).apply(lambda x: score_component(x, 0, 0.8, max_score=5))

    df['hei_refined_grains'] = df['G_REFINED_PER1000KCAL'].apply(lambda x: score_component(x, 4.3, 1.8, reverse=True, max_score=10))
    df['hei_added_sugars'] = df['ADD_SUGARS_PER1000KCAL'].apply(lambda x: score_component(x, 26, 6.5, reverse=True, max_score=10))

    df['hei_sodium'] = df['SODIUM_PER1000KCAL'].apply(lambda x: score_component(x, 2.0, 1.1, reverse=True, max_score=10))
    df['hei_sat_fats'] = df['SAT_FAT_PCT_ENERGY'].apply(lambda x: score_component(x, 16, 8, reverse=True, max_score=10))

    hei_components = [
        'hei_total_fruit', 'hei_whole_fruit', 'hei_total_veg', 'hei_greens_beans',
        'hei_whole_grains', 'hei_dairy', 'hei_total_protein', 'hei_sea_plant_protein',
        'hei_fatty_acid', 'hei_refined_grains', 'hei_added_sugars',
        'hei_sodium', 'hei_sat_fats'
    ]

    df[hei_components] = df[hei_components].fillna(0)
    df['hei_score'] = df[hei_components].sum(axis=1)

    print("Mean HEI component scores and total:")
    print(df[hei_components + ['hei_score']].mean().round(1))

    bins = [-float('inf'), 60, 80, float('inf')]
    labels = ['Poor', 'Needs Improvement', 'Good']

    df = df.copy()
    df['diet_score_category'] = pd.cut(df['hei_score'], bins=bins, labels=labels)
    df['diet_score_category'] = df['diet_score_category'].cat.add_categories('Unknown')
    df.loc[df['hei_score'].isna(), 'diet_score_category'] = 'Unknown'

    final_columns = ['participant_id', 'total_diet_weight', 'food_item_weight', 'diet_score_category'] + \
                    [col for col in df.columns if col.startswith('hei_')]

    final_df = df[final_columns]

    output_path = processed_data_dir / "hei2015_scores.csv"

    if save_csv:
        final_df.to_csv(output_path, index=False)

    print("Saved cleaned data to:", pretty_path(output_path))   
    return final_df

def main():    
    final_df = calculate_hei_scores()
   
if __name__ == "__main__":
    main()

