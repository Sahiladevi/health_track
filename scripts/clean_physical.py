"""
scripts\\clean_physical.py

This script cleans the NHANES PAQ_L physical activity dataset, which includes data 
on physical and sedentary behaviors.

- Renames columns for readability.
- Normalizes activity frequency units (e.g., per day, per week).
- Replaces invalid or implausible values with NaN.
- Caps frequency and duration based on plausible physical limits.
- Calculates weekly total and sedentary activity time.
- Saves the cleaned dataframe as a CSV.
"""

import sys
from pathlib import Path

# Add project root to sys.path 
project_root = Path(__file__).parent.parent.resolve()
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

import pandas as pd
import numpy as np
from scripts.config import CLEAN_DATA_DIR, datasets
from scripts.data_loading import load_dataset
from scripts.utils import rename_columns, show_missing, drop_missing, pretty_path

# Max plausible frequencies per unit
FREQ_LIMITS = {'D': 4, 'W': 28, 'M': 31, 'Y': 365}

# Weekly conversion factors
WEEKLY_CONVERSION = {'D': 7, 'W': 1, 'M': 1 / 4.345, 'Y': 1 / 52}

VALID_UNITS = set(FREQ_LIMITS.keys())
INVALID_VALUES = [7777, 9999]

def clean_physical_activity(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the PAQ_L physical activity dataset.

    Performs column renaming, unit normalization, filtering of invalid data and
    calculation of weekly activity totals.

    Args:
        df (pd.DataFrame): Raw PAQ_L dataframe.

    Returns:
        pd.DataFrame: Cleaned dataframe ready for analysis.
    """
    if df.empty:
        print("[PAQ_L] The dataframe is empty. Nothing to clean.")
        return df

    print("cleaning process begins")
    print("Dataframe rows and columns size before cleaning:", df.shape)

    # Rename columns
    rename_map = {
        'SEQN': 'participant_id',
        'PAD790Q': 'freq',
        'PAD790U': 'freq_unit',
        'PAD800': 'duration_min',
        'PAD680': 'sedentary_min_per_day'
    }
    df = rename_columns(df, rename_map)
    df['participant_id'] = df['participant_id'].apply(
    lambda x: str(int(x)) if pd.notnull(x) else np.nan
    )

    # Convert columns to numeric, coercing errors to NaN
    for col in ['freq', 'duration_min', 'sedentary_min_per_day']:
        df[col] = pd.to_numeric(df.get(col), errors='coerce')

    # Clean frequency unit column
    df['freq_unit'] = df['freq_unit'].astype(str).str.strip().str.upper()

    # Replace invalid values with NaN
    for col in ['freq', 'duration_min', 'sedentary_min_per_day']:
        df.loc[df[col].isin(INVALID_VALUES), col] = np.nan

    # Remove invalid frequency units
    df.loc[~df['freq_unit'].isin(VALID_UNITS), 'freq_unit'] = np.nan

    # Apply plausible limits
    df.loc[df['sedentary_min_per_day'] >= 1440, 'sedentary_min_per_day'] = np.nan
    df.loc[df['duration_min'] > 120, 'duration_min'] = np.nan
    df.loc[df['freq'] == 0, 'freq'] = np.nan

    # Cap frequency at max plausible per unit
    def cap_frequency(row):
        freq, unit = row['freq'], row['freq_unit']
        if pd.isna(freq) or pd.isna(unit):
            return np.nan
        return freq if freq <= FREQ_LIMITS.get(unit, np.inf) else np.nan

    df['freq'] = df.apply(cap_frequency, axis=1)

    # Calculate weekly frequency
    def to_weekly(row):
        freq, unit = row['freq'], row['freq_unit']
        if pd.isna(freq) or pd.isna(unit):
            return np.nan
        return freq * WEEKLY_CONVERSION.get(unit, np.nan)

    df['freq_per_week'] = df.apply(to_weekly, axis=1)

    # Calculate total weekly minutes and sedentary minutes per week
    df['total_weekly_min'] = df['freq_per_week'] * df['duration_min']
    df['sedentary_min_per_week'] = df['sedentary_min_per_day'] * 7

    # Drop rows missing any of the critical columns
    needed_cols = ['freq', 'duration_min', 'freq_per_week', 'total_weekly_min', 'sedentary_min_per_day']
    df = drop_missing(df, needed_cols)  

    # Show missing data summary
    show_missing(df, "PAQ_L")

    # Save cleaned data
    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
    output_file = CLEAN_DATA_DIR / "paq_l_clean.csv"
    df.to_csv(output_file, index=False)
    print("Dataframe rows and columns size after cleaning:", df.shape)
    print(f"[PAQ_L] Cleaned data saved to: {pretty_path(output_file)}")

    return df


def main():
    label = "PAQ_L"
    paq_info = datasets.get(label)
    if paq_info is None:
        print(f"[{label}] Dataset info not found in datasets config.")
        return

    file_path = paq_info.get("file_path")
    columns = paq_info.get("columns")

    print(f"[{label}] Loading dataset from {file_path}")
    df = load_dataset(file_path, columns)

    if df is None or df.empty:
        print(f"[{label}] Failed to load or empty dataset.")
        return

    print(f"[{label}] Dataset loaded. Starting cleaning...")
    cleaned_df = clean_physical_activity(df)
    print(f"[{label}] Cleaning complete.")


if __name__ == "__main__":
    main()
