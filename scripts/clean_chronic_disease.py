"""
scripts\\clean_chronic.py

This script cleans chronic disease data from NHANES.
- Diabetes (DIQ)
- Cardiovascular Conditions (MCQ)
- saves the cleaned versions as CSV files.
"""
import pandas as pd
import numpy as np
from config import CLEAN_DATA_DIR
from data_loading import load_dataset  
from config import datasets 
from typing import Optional, Dict
from utils import pretty_path

# Mapping codes to binary Yes/No
YES_NO_MAP = {1: 1, 2: 0}  # 1 = Yes, 2 = No
DIABETES_MAP = {1: 1, 2: 0}

MCQ_CONDITIONS = {
    'MCQ160B': 'congestive_heart_failure',
    'MCQ160C': 'coronary_heart_disease',
    'MCQ160D': 'angina',
    'MCQ160E': 'heart_attack'
}

def clean_diq(df: pd.DataFrame, label: str = "DIQ_L") -> pd.DataFrame:
    """
    Clean the Diabetes Questionnaire dataset.

    Map codes to diagnosis and medication columns, handle missing/unknown values,
  
    Args:
        df: Raw DIQ dataset as a DataFrame.
        label: Optional label for logging and filenames.

    Returns:
        Cleaned DataFrame with selected columns and saved CSV file.
    """
    if df.empty:
        print(f"{label}: The dataset is empty.")
        return df

    df = df.rename(columns={"SEQN": "participant_id"})
    df['participant_id'] = df['participant_id'].apply(
    lambda x: str(int(x)) if pd.notnull(x) else np.nan
    )

    df['diabetes_dx'] = df['DIQ010'].replace({3: np.nan, 7: np.nan, 9: np.nan}).map(DIABETES_MAP)
    df['diabetes_meds'] = df['DIQ070'].replace({7: np.nan, 9: np.nan}).map(YES_NO_MAP)

    columns_to_keep = ['participant_id', 'diabetes_dx', 'diabetes_meds']
    df_clean = df[columns_to_keep].reset_index(drop=True)

    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path = CLEAN_DATA_DIR / f"{label.lower()}_clean.csv"
    df_clean.to_csv(out_path, index=False)
    print(f"{label}: Saved basic cleaned data to {pretty_path(out_path)}")
    print(f"{label}: Final shape: {df_clean.shape}")
    return df_clean

def clean_mcq(df: pd.DataFrame, label: str = "MCQ_L") -> pd.DataFrame:
    """
    Clean Cardiovascular Conditions data.

    Maps codes to binary indicators for various heart conditions
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

    df = df.rename(columns={"SEQN": "participant_id"})
    df['participant_id'] = df['participant_id'].apply(
    lambda x: str(int(x)) if pd.notnull(x) else np.nan
    )

    for col, new_col in MCQ_CONDITIONS.items():
        df[new_col] = df[col].replace({7: np.nan, 9: np.nan}).map(YES_NO_MAP)

    columns_to_keep = ['participant_id'] + list(MCQ_CONDITIONS.values())
    df_clean = df[columns_to_keep].reset_index(drop=True)

    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path = CLEAN_DATA_DIR / f"{label.lower()}_clean.csv"
    df_clean.to_csv(out_path, index=False)
    print(f"{label}: Saved basic cleaned data to {pretty_path(out_path)}")
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
    print("=== Chronic Disease Basic Cleaning Started ===")
    cleaned = {}

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

    print("=== Finished basic cleaning ===")
    return cleaned

if __name__ == "__main__":
    main()
