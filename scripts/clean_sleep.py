"""
scripts/clean_sleep.py

This script processes and cleans the NHANES SLQ_L dataset, which includes sleep duration data.
- Renames confusing column names to something more readable.
- Converts sleep hour values to numbers (in case they're stored as strings).
- Filters out missing or unrealistic sleep durations.
- Handles weird near-zero values that can mess up the data.
- Calculates each person's average sleep across the week.
- Saves the cleaned-up data as a CSV file.

"""

import pandas as pd
import numpy as np
from pathlib import Path
from config import CLEAN_DATA_DIR, datasets
from data_loading import load_dataset
from utils import (
    rename_columns,
    show_missing,
    replace_close_values_with_nan
)

def clean_sleep_hours(x: float | None) -> float | None:
    """
    Checks if a sleep value is reasonable.
    
    Args:
        x: Number of hours someone reports sleeping per night.
        
    Returns:
        The original value if it's between 3 and 14 hours.
        Otherwise, returns NaN to mark it as invalid.
    """
    if pd.isna(x):
        return np.nan
    if x < 3 or x >= 14:
        return np.nan
    return x

def clean_sleep(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and processes the SLQ_L sleep dataset.
    
    Steps:
    - Renames columns for clarity.
    - Converts sleep duration columns to numeric values.
    - Replaces weird tiny float values with NaN.
    - Filters out unrealistic sleep durations.
    - Drops rows where both weekday and weekend sleep are missing.
    - Calculates a person's average weekly sleep (weighted by weekdays/weekends).
    - Saves the cleaned data to a CSV file.
    
    Args:
        df: Raw SLQ_L dataset as a pandas DataFrame.
    
    Returns:
        Cleaned DataFrame with a new column for average weekly sleep hours.
    """
    if df.empty:
        print("Warning: The dataframe is empty.")
        return df

    print("Cleaning SLQ_L dataset begins")
    print(f"Dataframe shape before cleaning: {df.shape}")

    # Rename confusing column names
    new_names = {
        "SEQN": "participant_id",
        "SLD012": "sleep_weekday_hr",
        "SLD013": "sleep_weekend_hr"
    }
    df = rename_columns(df, new_names)

    # Convert sleep hour columns to numeric (in case they’re stored as strings)
    sleep_cols = ["sleep_weekday_hr", "sleep_weekend_hr"]
    for col in sleep_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Replace weird tiny float values that shouldn’t be there
    weird_val = 5.39760534693402e-79
    tolerance = 1e-80
    df = replace_close_values_with_nan(df, weird_val, tolerance, sleep_cols)

    print("Missing values before cleaning:")
    show_missing(df, "SLQ_L")

    # Filter out unrealistic sleep values
    print("Validating sleep hour values...")
    for col in sleep_cols:
        df[col] = df[col].apply(clean_sleep_hours)

    # Drop rows where both sleep columns are missing
    df = df.dropna(subset=sleep_cols, how="all")

    # Calculate average sleep per week (5 weekday nights + 2 weekend nights)
    print("Calculating weighted average sleep hours...")
    valid_days = 7 - df[sleep_cols].isna().sum(axis=1)
    weighted_sum = (
        df["sleep_weekday_hr"].fillna(0) * 5 +
        df["sleep_weekend_hr"].fillna(0) * 2
    )
    df["sleep_avg_hr"] = weighted_sum / valid_days

    print("Summary of cleaned values:")
    print(df[["sleep_weekday_hr", "sleep_weekend_hr", "sleep_avg_hr"]].describe())
    print(f"Dataframe shape after cleaning: {df.shape}")

    # Save the cleaned data
    try:
        CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
        output_path = CLEAN_DATA_DIR / "slq_l_clean.csv"
        df.to_csv(output_path, index=False)
        print(f"Saved cleaned data to: {output_path}")
    except Exception as e:
        print(f"Error: Failed to save cleaned data: {e}")

    return df

def main() -> None:
    """
    Loads the raw sleep dataset (SLQ_L),
    runs the cleaning process,
    and saves the result to a CSV file.
    """
    print("Loading SLQ_L dataset")
    label = "SLQ_L"
    sleep_info = datasets.get(label)
    if sleep_info is None:
        print(f"{label} not found in datasets config.")
        return

    file_path = sleep_info["file_path"]
    columns = sleep_info.get("columns")
    df = load_dataset(file_path, columns)

    if df is None:
        print(f"Dataset '{label}' not found or failed to load. Exiting.")
        return

    # Clean and save the dataset
    cleaned_df = clean_sleep(df)
    print("Cleaning complete.")

if __name__ == "__main__":
    main()
