"""
scripts\\clean_fped.py

This script cleans the NHANES FPED dataset (FPED_1720 sheet).

- Uses specified columns from config.
- Renames columns to remove units for easier use.
- Converts numeric columns to proper types.
- Drops rows with missing FOODCODE or DESCRIPTION.
- Replaces tiny float anomalies with NaN.
- Saves the cleaned dataframe as CSV.
"""

import pandas as pd
import numpy as np
from config import CLEAN_DATA_DIR, datasets
from data_loading import load_dataset
from utils import (
    drop_missing,
    replace_close_values_with_nan,
    pretty_path
)

def rename_columns_remove_units(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename columns to remove units in parentheses.
    E.g., 'F_TOTAL (cup eq)' -> 'F_TOTAL'
    """
    new_names = {}
    for col in df.columns:
        # Remove unit parentheses and trim spaces
        new_col = col.split('(')[0].strip()
        new_names[col] = new_col
    return df.rename(columns=new_names)

def clean_fped(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean FPED_1720 dataset.

    Args:
        df (pd.DataFrame): Raw FPED dataframe.

    Returns:
        pd.DataFrame: Cleaned dataframe.
    """
    if df.empty:
        print("The dataframe is empty.")
        return df

    print("Cleaning FPED dataset...")
    print("Initial shape:", df.shape)

    # Rename columns to remove units
    df = rename_columns_remove_units(df)

    # Define numeric columns (exclude FOODCODE and DESCRIPTION)
    numeric_cols = df.columns.drop(['FOODCODE', 'DESCRIPTION']).tolist()

    # Convert numeric columns
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Replace tiny float anomalies with NaN
    weird_val = 5.39760534693402e-79
    tolerance = 1e-80
    df = replace_close_values_with_nan(df, weird_val, tolerance, numeric_cols)

    # Drop rows missing FOODCODE or DESCRIPTION
    print("Dropping rows missing FOODCODE or DESCRIPTION...")
    df = drop_missing(df, ['FOODCODE', 'DESCRIPTION'])

    # Drop rows where all numeric columns are missing
    print("Dropping rows where all numeric columns are missing...")
    df = df.dropna(subset=numeric_cols, how='all')

    print("Final shape after cleaning:", df.shape)

    # Save cleaned data
    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
    output_path = CLEAN_DATA_DIR / "fped_1720_clean.csv"
    df.to_csv(output_path, index=False)
    print("Saved cleaned data to:", pretty_path(output_path))

    return df

def main() -> None:
    print("Loading FPED_1720 dataset...")
    label = "FPED_1720"
    fped_info = datasets.get(label)
    if fped_info is None:
        print(f"{label} not found in datasets config.")
        return

    file_path = fped_info["file_path"]
    columns = fped_info.get("columns")
    df = load_dataset(file_path, columns, sheet_name=fped_info.get("sheet_name"))

    if df is None:
        print(f"Dataset '{label}' not found or failed to load. Exiting.")
        return

    print("Dataset loaded. Cleaning now...")
    cleaned_df = clean_fped(df)
    print("Cleaning complete.")

if __name__ == "__main__":
    main()
