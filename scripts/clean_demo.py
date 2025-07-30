"""
scripts\\clean_demo.py

This script cleans the NHANES DEMO_L dataset, which includes demographics data.

- Renames columns for readability.
- Converts and validates numeric data.
- Drops rows with missing or invalid values.
- Maps coded values (e.g., gender, race, education) to human-readable text.
- Replaces tiny float values with NaN (e.g., 5.39e-79).
- Imputes missing poverty-income ratio using median values within race/education groups.
- Flags missing interview weights and removes low-weight samples.
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
from scripts.utils import (
    rename_columns,
    drop_missing,
    remove_outliers,
    drop_invalid_weight,
    replace_close_values_with_nan,
    pretty_path
)

# Mapping dictionaries for converting numeric codes to readable labels
gender_map = {
    1: "Male",
    2: "Female"
}

race_map = {
    1: "Mexican American",
    2: "Other Hispanic",
    3: "Non-Hispanic White",
    4: "Non-Hispanic Black",
    6: "Non-Hispanic Asian",
    7: "Other/Multi-Racial"
}

edu_map = {
    1: "<9th grade",
    2: "9-11th grade",
    3: "High school/GED",
    4: "Some college/AA degree",
    5: "College graduate or above"
}


def clean_demo(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the DEMO_L dataset.

    Applies column renaming, handles missing and invalid data,
    maps codes to readable labels, and imputes missing PIR values.

    Args:
        df (pd.DataFrame): Raw DEMO_L dataframe.

    Returns:
        pd.DataFrame: Cleaned dataframe, ready for analysis or merging.
    """
    if df.empty:
        print("The dataframe is empty.")
        return df

    print("Cleaning process begins") 
    print("DEMO_L dataset rows and columns before cleaning:", df.shape)

    # Rename columns
    new_names = {
        "SEQN": "participant_id",
        "RIDAGEYR": "age",
        "RIAGENDR": "gender",
        "RIDRETH3": "race_ethnicity",
        "DMDEDUC2": "education_level",
        "INDFMPIR": "poverty_income_ratio",
        "WTMEC2YR": "exam_sample_weight",
        "WTINT2YR": "interview_sample_weight",
        "SDMVSTRA": "strata",
        "SDMVPSU": "psu"
    }
    df = rename_columns(df, new_names) 
    df['participant_id'] = df['participant_id'].apply(
    lambda x: str(int(x)) if pd.notnull(x) else np.nan
    )

    # Ensure key columns are numeric
    numeric_cols = ["age", "poverty_income_ratio", "exam_sample_weight", 
                    "interview_sample_weight", "strata", "psu"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows with missing key values
    print("Dropped rows with missing age...")
    df = drop_missing(df, ["age"])

    # Filter out participants under 20 years old
    print("Removed people under 20 years old...")
    df = remove_outliers(df, "age", 20, np.inf)

    print("Dropping rows missing gender, race, strata, or PSU...")
    df = drop_missing(df, ["gender", "race_ethnicity", "strata", "psu"])

    # Map numeric codes to text
    print("Mapping gender, race, and education level to text...")
    df["gender"] = df["gender"].map(gender_map)
    df["race_ethnicity"] = df["race_ethnicity"].map(race_map)
    df["education_level"] = df["education_level"].map(edu_map).fillna("Missing")

    # Replace weird tiny float values
    print("Replacing weird tiny float values (e.g., 5.39e-79) with NaN...")
    weird_val = 5.39760534693402e-79
    tolerance = 1e-80
    float_cols = ["age", "poverty_income_ratio", "exam_sample_weight", 
                  "interview_sample_weight", "strata", "psu"]
    df = replace_close_values_with_nan(df, weird_val, tolerance, float_cols)

    # Convert age to integer after cleaning float artifacts
    df["age"] = df["age"].round().astype("Int64")

   # Impute missing PIR values safely
    print("Imputing missing poverty_income_ratio (PIR) within education_level + race_ethnicity groups...")
    missing_before = df["poverty_income_ratio"].isna().sum()

    # Step 1: Groupwise median PIR
    group_median = df.groupby(["education_level", "race_ethnicity"])["poverty_income_ratio"].transform("median")
    
    # Step 2: Fill NaNs with group median
    df["poverty_income_ratio"] = df["poverty_income_ratio"].fillna(group_median)

    # Step 3: Fill remaining with overall median
    df["poverty_income_ratio"] = df["poverty_income_ratio"].fillna(df["poverty_income_ratio"].median())

    missing_after = df["poverty_income_ratio"].isna().sum()
    print(f"Imputed PIR: {missing_before - missing_after} filled, {missing_after} still missing")
    
    # Remove invalid weights
    print("Removing missing and invalid sample weights")
    df = drop_invalid_weight(df, "exam_sample_weight")

    # Flag missing interview weights
    print("Checking for missing interview sample weight...")
    df["interview_sample_weight_missing"] = df["interview_sample_weight"].isna()

    print("DEMO_L dataset rows and columns after cleaning:", df.shape)

    # Save cleaned data
    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
    output_path = CLEAN_DATA_DIR / "demo_l_clean.csv"
    df.to_csv(output_path, index=False)
    print("Saved cleaned data to:", pretty_path(output_path))
    return df


def main() -> None:
    """
    Loads and cleans the DEMO_L dataset using the cleaning pipeline.
    """
    print("Loading DEMO_L dataset...")
    label = "DEMO_L"
    demo_info = datasets.get(label)
    if demo_info is None:
        print(f"{label} not found in datasets config.")
        return

    file_path = demo_info["file_path"]
    columns = demo_info.get("columns")
    df = load_dataset(file_path, columns)

    if df is None:
        print(f"Dataset '{label}' not found or failed to load. Exiting.")
        return

    print("Dataset loaded. Cleaning now...")
    cleaned_df = clean_demo(df)    
    print("Cleaning complete.")


if __name__ == "__main__":
    main()
