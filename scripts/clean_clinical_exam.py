"""
clean_clinical_exam.py

Contains functions to clean various clinical exam datasets,
including BMI, blood pressure, cholesterol, glucose, 

"""

import pandas as pd
import numpy as np
from config import CLEAN_DATA_DIR, datasets
from data_loading import load_dataset
from typing import Optional
from utils import (
    show_missing,
    rename_columns,
    drop_missing,
    remove_outliers, 
    replace_close_values_with_nan   
)

# 1. BMI
def clean_bmi(df: Optional[pd.DataFrame]) -> pd.DataFrame:
    """
    Clean the BMI dataset.

    - Renames relevant columns for clarity.
    - Converts BMI values to numeric and removes any unrealistic values.
    - Drops rows with missing BMI values.
    - Saves the cleaned data to a CSV file.

    Args:
        df: Raw BMI data as a pandas DataFrame or None.

    Returns:
        A cleaned pandas DataFrame with BMI data.
    """
    if df is None or df.empty:
        print("BMI dataframe is empty.")
        return pd.DataFrame()
    print("Cleaning BMI data.")
    print("Dataframe rows and columns size before cleaning:", df.shape)    

    df = rename_columns(df, {'SEQN': 'participant_id', 'BMXBMI': 'bmi'})
    df['participant_id'] = df['participant_id'].apply(
    lambda x: str(int(x)) if pd.notnull(x) else np.nan
    )

    df['bmi'] = pd.to_numeric(df['bmi'], errors='coerce')
    df = df[(df['bmi'] >= 11.1) & (df['bmi'] <= 74.8)]

    show_missing(df, "BMI - Before Cleaning")
    df = drop_missing(df, ['bmi'])
    show_missing(df, "BMI - After Cleaning")
    df.reset_index(drop=True, inplace=True)
    print("Dataframe rows and columns size after cleaning:", df.shape)

    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
    output_path = CLEAN_DATA_DIR / "bmx_l_clean.csv"
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned BMI data to {output_path}")

    return df

# 2. Blood Pressure
def clean_bp(df: Optional[pd.DataFrame]) -> pd.DataFrame:
    """
    Clean blood pressure data by:
    - Renaming columns.
    - Removing outliers outside plausible systolic and diastolic ranges.
    - Calculating the average systolic and diastolic values.    
    - Saving the cleaned and summarized data.

    Args:
        df: Raw blood pressure DataFrame or None.

    Returns:
        A DataFrame with participant IDs, average systolic and diastolic BP, and categories.
    """
    if df is None or df.empty:
        print("Blood Pressure dataframe is empty.")
        return pd.DataFrame()

    print("Cleaning Blood Pressure data")
    print("Dataframe rows and columns size before cleaning:", df.shape)

    df = rename_columns(df, {
        'SEQN': 'participant_id',
        'BPXOSY1': 'systolic_1',
        'BPXOSY2': 'systolic_2',
        'BPXOSY3': 'systolic_3',
        'BPXODI1': 'diastolic_1',
        'BPXODI2': 'diastolic_2',
        'BPXODI3': 'diastolic_3',
    })
    df['participant_id'] = df['participant_id'].apply(
    lambda x: str(int(x)) if pd.notnull(x) else np.nan
    )
    show_missing(df, "BP - Before Cleaning")

    systolic_cols = ['systolic_1', 'systolic_2', 'systolic_3']
    diastolic_cols = ['diastolic_1', 'diastolic_2', 'diastolic_3']

    for col in systolic_cols:
        df[col] = df[col].apply(lambda x: x if 50 <= x <= 233 else np.nan)
    for col in diastolic_cols:
        df[col] = df[col].apply(lambda x: x if 24 <= x <= 142 else np.nan)

    df['systolic_avg'] = df[systolic_cols].mean(axis=1)
    df['diastolic_avg'] = df[diastolic_cols].mean(axis=1)

    df = drop_missing(df, ['systolic_avg', 'diastolic_avg'])

    show_missing(df, "BP - After Cleaning")
    print("Dataframe rows and columns size after cleaning:", df.shape)

    
    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
    output_path = CLEAN_DATA_DIR / "bpxo_l_clean.csv"
    df_to_save = df[['participant_id', 'systolic_avg', 'diastolic_avg']]
    df_to_save.to_csv(output_path, index=False)
    print(f"Saved cleaned Blood Pressure data to {output_path}")

    return df_to_save

# 3. Total Cholesterol
def clean_total_cholesterol(df: Optional[pd.DataFrame]) -> pd.DataFrame:
    """
    Clean total cholesterol data by renaming columns, removing missing values,
    removing outliers, and saving cleaned data.

    Args:
        df: Raw cholesterol DataFrame or None.

    Returns:
        Cleaned cholesterol DataFrame.
    """
    if df is None or df.empty:
        print("Total cholesterol dataframe is empty.")
        return pd.DataFrame()
    
    required_cols = ['SEQN', 'LBXTC']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")
    
    print("Cleaning Total Cholesterol data")
    print("Dataframe rows and columns size before cleaning:", df.shape)

    df = rename_columns(df, {'SEQN': 'participant_id', 'LBXTC': 'total_cholesterol'})
    df['participant_id'] = df['participant_id'].apply(
    lambda x: str(int(x)) if pd.notnull(x) else np.nan
    )

    show_missing(df, "Cholesterol - Before Cleaning")
    df = drop_missing(df, ['total_cholesterol'])
    df = remove_outliers(df, 'total_cholesterol', 62, 438)
    show_missing(df, "Cholesterol - After Cleaning")

    print("Dataframe rows and columns size after cleaning:", df.shape)

    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
    output_path = CLEAN_DATA_DIR / "tchol_l_clean.csv"
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned Total Cholesterol data to {output_path}")

    return df

# 4. Glucose
def clean_glucose(df: Optional[pd.DataFrame]) -> pd.DataFrame:
    """
    Clean glucose data by renaming columns, converting units as needed,
    removing missing and outlier values, and saving the cleaned data.

    Args:
        df: Raw glucose DataFrame or None.

    Returns:
        Cleaned glucose DataFrame.
    """
    if df is None or df.empty:
        print("Glucose dataframe is empty.")
        return pd.DataFrame()

    print("Cleaning Glucose data")
    print("Dataframe rows and columns size before cleaning:", df.shape)

    df = rename_columns(df, {
        'SEQN': 'participant_id',
        'WTSAF2YR': 'fasting_subsample_weight',
        'LBXGLU': 'fasting_glucose_mg_dl',
        'LBDGLUSI': 'fasting_glucose_mmol_l'
    })
    #df['participant_id'] = df['participant_id'].astype(float).astype(int).astype(str)
    df['participant_id'] = df['participant_id'].apply(
    lambda x: str(int(x)) if pd.notnull(x) else np.nan
    )

    df['fasting_subsample_weight'] = pd.to_numeric(df['fasting_subsample_weight'], errors='coerce')

    show_missing(df, "Glucose - Before Cleaning")

    df = replace_close_values_with_nan(df, target=0, tolerance=1e-5, columns=['fasting_subsample_weight'])

    df = df[~(df['fasting_glucose_mg_dl'].isna() & df['fasting_glucose_mmol_l'].isna())]

    df.loc[df['fasting_glucose_mmol_l'].isna() & df['fasting_glucose_mg_dl'].notna(),
           'fasting_glucose_mmol_l'] = df['fasting_glucose_mg_dl'] / 18

    df.loc[df['fasting_glucose_mg_dl'].isna() & df['fasting_glucose_mmol_l'].notna(),
           'fasting_glucose_mg_dl'] = df['fasting_glucose_mmol_l'] * 18

    df = remove_outliers(df, 'fasting_glucose_mg_dl', 59, 561)
    df = remove_outliers(df, 'fasting_glucose_mmol_l', 3.3, 31.1)

    df = df[df['fasting_subsample_weight'].notna()]
    df = df[df['fasting_subsample_weight'] > 0]

    show_missing(df, "Glucose - After Cleaning")
    print("Dataframe rows and columns size after cleaning:", df.shape)

    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
    output_path = CLEAN_DATA_DIR / "glu_l_clean.csv"
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned Glucose data to {output_path}")

    return df


# Main function
def main():
    print("Starting clinical exam datasets cleaning")

    datasets_and_cleaners = [
        ("BMX_L", clean_bmi),
        ("BPXO_L", clean_bp),
        ("TCHOL_L", clean_total_cholesterol),
        ("GLU_L", clean_glucose)        
    ]

    cleaned_dfs = {}

    for label, clean_func in datasets_and_cleaners:
        print(f"\nLoading dataset {label}")
        info = datasets.get(label)
        if not info:
            print(f"No config entry found for {label}")
            continue

        df = load_dataset(info["file_path"], info.get("columns"))
        if df is None:
            print(f"{label} dataset not loaded.")
            continue

        print(f"Cleaning {label} dataset...")
        cleaned_df = clean_func(df)
        print(f"Finished cleaning {label}, cleaned shape: {cleaned_df.shape}")
        cleaned_dfs[label] = cleaned_df    

    print("\nAll cleaning complete.")

if __name__ == "__main__":
    main()
