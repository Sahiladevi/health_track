"""
clean_chronic.py

This script cleans chronic disease data from NHANES:
- Diabetes (DIQ)
- Cardiovascular Conditions (MCQ)

It recodes values, creates labels, makes combined indicators,
and saves the cleaned versions as CSV files.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from config import CLEAN_DATA_DIR
from data_loading import load_dataset  
from config import datasets 
from typing import Optional, Dict

# Mapping codes to binary Yes/No
YES_NO_MAP = {1: 1, 2: 0}  # 1 = Yes, 2 = No
MEDS_MAP = {1: 'Taking meds', 0: 'Not taking meds'}

# Mapping for diabetes diagnosis
DIABETES_MAP = {1: 1, 2: 0}

# Mapping columns for cardiovascular conditions
MCQ_CONDITIONS = {
    'MCQ160B': 'congestive_heart_failure',
    'MCQ160C': 'coronary_heart_disease',
    'MCQ160D': 'angina',
    'MCQ160E': 'heart_attack'
}

def label_meds(val: Optional[int]) -> str:
    """
    Convert medication indicator integer to a readable label.

    Args:
        val: Medication code (1 for taking meds, 0 for not, others unknown).

    Returns:
        A string label: 'Taking meds', 'Not taking meds', or 'Unknown'.
    """
    if val == 1:
        return 'Taking meds'
    elif val == 0:
        return 'Not taking meds'
    else:
        return 'Unknown'

# Clean Diabetes Questionnaire data
def clean_diq(df: pd.DataFrame, label: str = "DIQ_L") -> pd.DataFrame:
    """
    Clean the Diabetes Questionnaire dataset.

    Recode diagnosis and medication columns, handle missing/unknown values,
    and create a combined diabetes status indicator.

    Args:
        df: Raw DIQ dataset as a DataFrame.
        label: Optional label for logging and filenames.

    Returns:
        Cleaned DataFrame with selected columns and saved CSV file.
    """
    if df.empty:
        print(f"{label}: The dataset is empty. Skipping...")
        return df

    print(f"{label}: Starting cleaning. Original shape: {df.shape}")

    df = df.rename(columns={"SEQN": "participant_id"})

    # Replace unknown/refused with NaN, map Yes/No
    df['diabetes_dx'] = df['DIQ010'].replace({3: np.nan, 7: np.nan, 9: np.nan}).map(DIABETES_MAP)
    df['diabetes_meds'] = df['DIQ070'].replace({7: np.nan, 9: np.nan}).map(YES_NO_MAP)
    df['diabetes_meds_cat'] = df['diabetes_meds'].apply(label_meds)

    # Create diabetes_status: 1 if diagnosed or meds, 0 if both no, NaN otherwise
    dx_1 = df['diabetes_dx'] == 1
    meds_1 = df['diabetes_meds'] == 1
    dx_0 = df['diabetes_dx'] == 0
    meds_0 = df['diabetes_meds'] == 0

    dx_1 = dx_1.fillna(False)
    meds_1 = meds_1.fillna(False)
    dx_0 = dx_0.fillna(False)
    meds_0 = meds_0.fillna(False)

    df['diabetes_status'] = np.where(
        dx_1 | meds_1,
        1,
        np.where(dx_0 & meds_0, 0, np.nan)
    )

    print(f"{label}: Cleaning done.")

    columns_to_keep = ['participant_id', 'diabetes_dx', 'diabetes_meds', 'diabetes_meds_cat', 'diabetes_status']
    df_clean = df[columns_to_keep].reset_index(drop=True)

    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path = CLEAN_DATA_DIR / f"{label.lower()}_clean.csv"
    df_clean.to_csv(out_path, index=False)
    print(f"{label}: Saved cleaned data to {out_path}")
    print(f"{label}: Final shape: {df_clean.shape}")

    return df_clean

# Clean Cardiovascular Conditions data
def clean_mcq(df: pd.DataFrame, label: str = "MCQ_L") -> pd.DataFrame:
    """
    Clean Cardiovascular Conditions data.

    Maps codes to binary indicators for various heart conditions,
    creates an indicator if participant has any cardiovascular condition,
    and saves cleaned data.

    Args:
        df: Raw MCQ dataset as a DataFrame.
        label: Optional label for logging and filenames.

    Returns:
        Cleaned DataFrame with selected columns and saved CSV file.
    """
    if df.empty:
        print(f"{label}: The dataset is empty. Skipping...")
        return df

    print(f"{label}: Starting cleaning. Original shape: {df.shape}")
    df = df.rename(columns={"SEQN": "participant_id"})

    # Replace 7 and 9 with NaN, map Yes/No for each heart condition
    for col, new_col in MCQ_CONDITIONS.items():
        df[new_col] = df[col].replace({7: np.nan, 9: np.nan}).map(YES_NO_MAP)

    # Create a column indicating if participant has any heart condition
    # Fill NaNs with 0 just for max calculation (treat missing as no)
    df_conditions_filled = df[list(MCQ_CONDITIONS.values())].fillna(0)
    df['any_cvd'] = df_conditions_filled.max(axis=1)

    print(f"{label}: Cleaning done.")

    columns_to_keep = ['participant_id'] + list(MCQ_CONDITIONS.values()) + ['any_cvd']
    df_clean = df[columns_to_keep].reset_index(drop=True)

    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path = CLEAN_DATA_DIR / f"{label.lower()}_clean.csv"
    df_clean.to_csv(out_path, index=False)
    print(f"{label}: Saved cleaned data to {out_path}")
    print(f"{label}: Final shape: {df_clean.shape}")

    return df_clean



def main(
    diq_df: Optional[pd.DataFrame] = None,
    mcq_df: Optional[pd.DataFrame] = None,
) -> Dict[str, Optional[pd.DataFrame]]:
    """
    Main function to clean NHANES chronic disease datasets.

    It can accept pre-loaded dataframes or load from files based on config.
    Cleans DIQ, and MCQ datasets individually, saving cleaned files.

    Args:
        diq_df: Optional pre-loaded Diabetes Questionnaire data.
        mcq_df: Optional pre-loaded Cardiovascular Conditions data.

    Returns:
        Dictionary with keys 'diq', 'mcq' and cleaned DataFrames or None if skipped.
    """
    print("=== Chronic Disease Cleaning Started ===")

    cleaned = {}

    # Load DIQ_L
    if diq_df is not None:
        print("Cleaning DIQ_L dataset (provided)...")
        cleaned['diq'] = clean_diq(diq_df)
    else:
        print("Loading DIQ_L dataset...")
        diq_info = datasets.get("DIQ_L")
        if diq_info is None:
            print("DIQ_L dataset info missing in config. Skipping DIQ cleaning.")
            cleaned['diq'] = None
        else:
            diq_df_loaded = load_dataset(diq_info["file_path"], diq_info.get("columns"))
            if diq_df_loaded is None:
                print("DIQ_L dataset not found or could not be loaded. Skipping DIQ cleaning.")
                cleaned['diq'] = None
            else:
                cleaned['diq'] = clean_diq(diq_df_loaded)

    # Load MCQ_L
    if mcq_df is not None:
        print("Cleaning MCQ_L dataset (provided)...")
        cleaned['mcq'] = clean_mcq(mcq_df)
    else:
        print("Loading MCQ_L dataset...")
        mcq_info = datasets.get("MCQ_L")
        if mcq_info is None:
            print("MCQ_L dataset info missing in config. Skipping MCQ cleaning.")
            cleaned['mcq'] = None
        else:
            mcq_df_loaded = load_dataset(mcq_info["file_path"], mcq_info.get("columns"))
            if mcq_df_loaded is None:
                print("MCQ_L dataset not found or could not be loaded. Skipping MCQ cleaning.")
                cleaned['mcq'] = None
            else:
                cleaned['mcq'] = clean_mcq(mcq_df_loaded)

    print("=== Finished cleaning process ===")
    return cleaned


if __name__ == "__main__":
    main()
