"""
script\\clean_diet
This script handles cleaning and preprocessing of dietary datasets.

It includes two main cleaning functions: one for the total diet dataset and one for
the individual diet dataset. Each function renames columns for clarity, handles
corrupted or suspicious values, deals with missing or zero values appropriately,
removes outliers, and saves the cleaned data to csv file.
"""

import pandas as pd
import numpy as np

from config import CLEAN_DATA_DIR, datasets
from data_loading import load_dataset
from utils import (
    rename_columns,
    show_missing,
    replace_zeros_with_nan,
    drop_invalid_weight,
    replace_close_values_with_nan,
    remove_outliers,
    drop_missing,
    pretty_path
)

def clean_total_diet(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and prepare the total diet dataset.

    This function renames columns for clarity, handles corrupted values by replacing
    near-zero corrupted floats with NaN, removes missing and invalid weight entries,
    filters out outliers in key dietary metrics, and finally saves the cleaned data
    to a CSV file.

    Args:
        df (pd.DataFrame): Raw total diet data to be cleaned.

    Returns:
        pd.DataFrame: The cleaned total diet dataset.
    """
    if df.empty:
        print("The dataframe is empty.")
        return df

    print("Starting total diet cleaning...")
    print("Initial shape:", df.shape)

    rename_map = {
        'DR1TKCAL': 'energy_kcal',
        'DR1TSODI': 'sodium_mg',
        'DR1TSFAT': 'satfat_g',       
        'WTDRD1': 'total_diet_weight',
        'SEQN': 'participant_id'
    }
    df = rename_columns(df, rename_map)

    df["participant_id"] = df["participant_id"].apply(
        lambda x: str(int(x)) if pd.notnull(x) else np.nan
    )

    corrupted_val = 5.397605e-79
    tolerance = 1e-78
    num_cols = ['energy_kcal', 'sodium_mg', 'satfat_g']
    df = replace_close_values_with_nan(df, target=corrupted_val, tolerance=tolerance, columns=num_cols)

    # Step 2: Skip replacing zeros with NaN (zeros allowed)

    required_columns = ['energy_kcal', 'sodium_mg', 'satfat_g']
    df = drop_missing(df, columns=required_columns)

    df = drop_invalid_weight(df, weight_column='total_diet_weight')

    df = remove_outliers(df, column='energy_kcal', min_value=0, max_value=10446)
    df = remove_outliers(df, column='sodium_mg', min_value=0, max_value=20006)
    df = remove_outliers(df, column='satfat_g', min_value=0, max_value=208.842)

    show_missing(df, name="Final Cleaned Dataset (with Sodium)")

    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
    output_path = CLEAN_DATA_DIR / "dr1tot_l_clean.csv"
    df.to_csv(output_path, index=False)
    print("Saved cleaned file to:", pretty_path(output_path))

    print("Final shape after cleaning:", df.shape)
    return df


def clean_individual_diet(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and process the individual diet dataset.

    This function renames columns for easier access, converts key columns to numeric types,
    handles suspicious very small values by converting them to NaN, replaces zero consumption
    grams with NaN, flags outliers and missing values, filters out invalid food codes and weights,
    and saves the cleaned data to a CSV.

    Args:
        df (pd.DataFrame): Raw individual diet data.

    Returns:
        pd.DataFrame: Cleaned and filtered individual diet dataset.
    """
    if df.empty:
        print("The dataframe is empty.")
        return df

    print("Starting cleaning...")
    print("Initial shape:", df.shape)
  
    rename_map = {
        "SEQN": "participant_id",
        "DR1IGRMS": "grams_consumed",
        "DR1IKCAL": "energy_kcal",
        "WTDRD1": "food_item_weight",
        "DR1IFDCD": "food_code"
    }
    df = rename_columns(df, rename_map)

    df["participant_id"] = df["participant_id"].apply(
        lambda x: str(int(x)) if pd.notnull(x) else np.nan
    )

    float_cols = ["energy_kcal", "grams_consumed", "food_item_weight"]
    for col in float_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    print("Initial missing and zero value counts:")
    print("Missing grams_consumed:", df["grams_consumed"].isna().sum())
    print("Zero grams_consumed:", (df["grams_consumed"] == 0).sum())
    print("Missing energy_kcal:", df["energy_kcal"].isna().sum())
    print("Zero energy_kcal:", (df["energy_kcal"] == 0).sum())

    weird_val = 5.39760534693402e-79
    tolerance = 1e-80    
    df = replace_close_values_with_nan(df, weird_val, tolerance, float_cols)

    df = replace_zeros_with_nan(df, ["grams_consumed"])

    df.loc[(df["energy_kcal"] <= 0) & (df["food_item_weight"] > 0), "energy_kcal"] = np.nan

    df["energy_kcal_outlier_flag"] = (df["energy_kcal"] > 4575).astype(int)

    df = df[df["energy_kcal"] <= 4575]

    df["grams_consumed_missing_flag"] = df["grams_consumed"].isna().astype(int)
    df["energy_kcal_missing_flag"] = df["energy_kcal"].isna().astype(int)

    df["dietary_recall_complete"] = np.where(df["food_item_weight"] > 0, 1, 0)

    print("Missing data summary:")
    show_missing(df[["energy_kcal", "grams_consumed", "food_item_weight"]], name="Dietary")

    df = drop_invalid_weight(df, "food_item_weight")

    df["food_code"] = pd.to_numeric(df["food_code"], errors="coerce")
    df = df[df["food_code"].notna()]

    print("Final shape after cleaning:", df.shape)

    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
    output_path = CLEAN_DATA_DIR / "dr1iff_l_clean.csv"
    df.to_csv(output_path, index=False)
    print("Saved cleaned file to:", pretty_path(output_path))

    return df


def main() -> None:
    # Example: run clean_total_diet
    print("Loading DR1TOT_L dataset")
    label_total = "DR1TOT_L"
    diet_info_total = datasets.get(label_total)

    if diet_info_total is None:
        print(f"{label_total} not found in datasets config.")
    else:
        file_path_total = diet_info_total["file_path"]
        print("Loading data from:", pretty_path(file_path_total))
        columns_total = diet_info_total.get("columns")
        df_total = load_dataset(file_path_total, columns_total)

        if df_total is not None and not df_total.empty:
            clean_total_diet(df_total)
        else:
            print("Total diet dataset not loaded or empty.")

    # Example: run clean_diet
    print("\nLoading DR1IFF_L dataset")
    label_individual = "DR1IFF_L"
    diet_info_individual = datasets.get(label_individual)

    if diet_info_individual is None:
        print(f"{label_individual} not found in datasets config.")
    else:
        file_path_individual = diet_info_individual["file_path"]
        print("Loading data from:", pretty_path(file_path_individual))
        columns_individual = diet_info_individual.get("columns")
        df_individual = load_dataset(file_path_individual, columns_individual)

        if df_individual is not None and not df_individual.empty:
            clean_individual_diet(df_individual)
        else:
            print("Individual diet dataset not loaded or empty.")


if __name__ == "__main__":
    main()