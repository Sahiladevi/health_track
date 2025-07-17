"""
clean_diet.py

This script processes the NHANES DR1TOT_L dietary dataset:
- Renames and standardizes key variables.
- Handles missing and zero intake values.
- Adds flags for missing data and dietary recall completeness.
- Applies multiple imputation to fill in missing intake values.
- Saves the cleaned dataset as a CSV.
"""

from typing import List
import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer  
from sklearn.impute import IterativeImputer

from config import CLEAN_DATA_DIR, datasets
from data_loading import load_dataset
from utils import (
    rename_columns,
    show_missing,
    replace_zeros_with_nan,
    drop_invalid_weight,
    replace_close_values_with_nan
)


def perform_imputation(df: pd.DataFrame, columns_to_impute: List[str]) -> pd.DataFrame:
    """
    Run multiple imputation on a subset of columns using sklearn's IterativeImputer.

    Parameters:
        df (pd.DataFrame): The dataframe containing dietary intake data.
        columns_to_impute (List[str]): Names of the columns that should be imputed.

    Returns:
        pd.DataFrame: The dataframe with missing values imputed in the specified columns.
    """
    print("Starting multiple imputation on dietary intake variables...")
    imputer = IterativeImputer(random_state=42, max_iter=10, sample_posterior=True)
    imputed_array = imputer.fit_transform(df[columns_to_impute])
    df[columns_to_impute] = imputed_array
    print("Imputation complete.")
    return df


def clean_diet(df: pd.DataFrame, do_impute: bool = True) -> pd.DataFrame:
    """
    Clean and preprocess the NHANES dietary data.

    - Renaming columns for readability
    - Converting types and handling zero values
    - Flagging missing values
    - imputation
    - Removing rows with invalid weights
    - Saving cleaned data to csv file

    Parameters:
        df (pd.DataFrame): Raw dietary dataset to be cleaned.
        do_impute (bool): Whether to perform multiple imputation on intake columns.

    Returns:
        pd.DataFrame: Cleaned dataset ready for analysis or modeling.
    """
    if df.empty:
        print("The dataframe is empty.")
        return df

    print("Cleaning process begins")
    print("Dataframe shape before cleaning:", df.shape)

    # Rename columns
    rename_map = {
        "SEQN": "participant_id",
        "DR1TKCAL": "energy_kcal",
        "DR1TSFAT": "sat_fat_g",
        "DR1TSUGR": "sugar_g",
        "DR1TFIBE": "fiber_g",
        "WTDR2D": "diet_weight"
    }
    df = rename_columns(df, rename_map)
    df['participant_id'] = df['participant_id'].apply(
    lambda x: str(int(x)) if pd.notnull(x) else np.nan
    )

    # Replace weird float values
    print("Replacing weird tiny float values (e.g., 5.39e-79) in diet data with NaN...")
    weird_val = 5.39760534693402e-79
    tolerance = 1e-80
    float_cols = ["energy_kcal", "fiber_g", "sugar_g", "sat_fat_g", "diet_weight"]
    df = replace_close_values_with_nan(df, weird_val, tolerance, float_cols)

    # Convert dietary columns to numeric
    diet_cols = ["energy_kcal", "sat_fat_g", "sugar_g", "fiber_g", "diet_weight"]
    for col in diet_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Replace zeros with NaN for intake variables
    intake_cols = ["energy_kcal", "sat_fat_g", "sugar_g", "fiber_g"]
    df = replace_zeros_with_nan(df, intake_cols)

    # Add missingness indicator flags
    for col in intake_cols:
        df[f"{col}_missing_flag"] = df[col].isna().astype(int)

    # Add flag for whether dietary recall was complete
    df["dietary_recall_complete"] = np.where(df["diet_weight"] > 0, 1, 0)

    print("Missing data BEFORE imputation:")
    show_missing(df[diet_cols], name="Dietary")

    # imputation
    if do_impute:
        df = perform_imputation(df, intake_cols)

    # Drop invalid rows based on weight
    df = drop_invalid_weight(df, "diet_weight")

    print("Missing data AFTER imputation:")
    show_missing(df[diet_cols], name="Dietary")

    print("Dataframe shape after cleaning:", df.shape)

    # Save cleaned dataset
    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
    output_path = CLEAN_DATA_DIR / "dr1tot_l_clean.csv"
    df.to_csv(output_path, index=False)
    print("Saved cleaned data to:", output_path)

    return df


def main() -> None:
    """
    Load and clean the DR1TOT_L dietary dataset.

    This function handles
    - Fetching config for the DR1TOT_L dataset
    - Loading the raw data from file
    - Running the cleaning function
    """
    print("Loading DR1TOT_L dataset")
    label = "DR1TOT_L"
    diet_info = datasets.get(label)

    if diet_info is None:
        print(f"{label} not found in datasets config.")
        return

    file_path = diet_info["file_path"]
    columns = diet_info.get("columns")
    df = load_dataset(file_path, columns)

    if df is None:
        print(f"Dataset '{label}' not found or failed to load. Exiting.")
        return

    print("Dataset loaded. Cleaning now...")
    cleaned_df = clean_diet(df, do_impute=True)

    print("Cleaning complete.")


if __name__ == "__main__":
    main()
