"""
scripts\\clean_healthcare_access.py
Cleans the HIQ_L dataset, which contains information about health insurance coverage.

"""
import pandas as pd
import numpy as np
from config import CLEAN_DATA_DIR, datasets
from data_loading import load_dataset
from utils import rename_columns, show_missing, drop_missing, pretty_path


def clean_insurance_coverage(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the HIQ_L dataset, which contains information about health insurance coverage.

    - Renames columns for readability.
    - Replaces invalid responses (e.g., 'Refused', 'Don't know') with NaN.
    - Drops rows where the insurance status is missing.
    - Maps numeric codes to "Yes"/"No" strings.
    - Saves the cleaned data to a CSV file.

    Args:
        df: Raw DataFrame loaded from the HIQ_L dataset.

    Returns:
        A cleaned DataFrame with standardized health insurance data.
    """
    label = "HIQ_L"
    print(f"Cleaning {label} dataset")
    print("Insurance dataset rows and columns size before cleaning:", df.shape)
    
    # Rename Columns
    df = rename_columns(df, {"SEQN": "participant_id", "HIQ011": "has_health_insurance"})
    df['participant_id'] = df['participant_id'].apply(
    lambda x: str(int(x)) if pd.notnull(x) else np.nan
    )

    df["has_health_insurance"] = df["has_health_insurance"].replace([7, 9, "."], pd.NA)

    show_missing(df, label + " before dropping missing")

    # drop missing values
    df = drop_missing(df, ["has_health_insurance"])

    # Mapping
    df["has_health_insurance"] = df["has_health_insurance"].map({1: "Yes", 2: "No"})

    print(f"Unique values in 'has_health_insurance':", df["has_health_insurance"].unique())
    print("Health insurance dataset rows and columns size after cleaning:", df.shape)

    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
    output_file = CLEAN_DATA_DIR / f"{label.lower()}_clean.csv"
    df.to_csv(output_file, index=False)
    print(f"Saved cleaned data to: {pretty_path(output_file)}")


    return df

def main() -> None:
    """
    Main function to load, clean, and save both the HIQ_L (insurance)
    and RXQ_RX_L (medication use) datasets.

    - Data loading via config
    - Validity checks
    """
    hiq_info = datasets.get("HIQ_L")
    if hiq_info:
        df_ins = load_dataset(hiq_info["file_path"], hiq_info.get("columns"))
        if not df_ins.empty:
            clean_insurance_coverage(df_ins)

    print("Cleaning complete.")


if __name__ == "__main__":
    main()
