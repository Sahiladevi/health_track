"""
data_loading.py

Loads raw NHANES datasets, validates files, saves interim CSVs,
and calls exploration utilities from utils.py.
"""

from pathlib import Path
from typing import Optional, List, Union, Dict
import pandas as pd
import pyreadstat

from config import datasets, INTERIM_DATA_DIR
from utils import validate_xpt_files, explore_data


def load_dataset(file_path: Union[str, Path], columns: Optional[List[str]] = None) -> Optional[pd.DataFrame]:
    """
    Load data from a file into a pandas DataFrame.

    Args:
        file_path: Path to the data file.
        columns: Optional list of columns to keep; if None, keep all columns.

    Returns:
        Loaded DataFrame, or None if loading failed or columns missing.
    """
    path = Path(file_path)
    if not path.exists():
        print(f"File not found: {path}")
        return None

    ext = path.suffix.lower()

    try:
        if ext == ".csv":
            df = pd.read_csv(path)
        elif ext in [".xls", ".xlsx"]:
            df = pd.read_excel(path)
        elif ext == ".xpt":
            df = pd.read_sas(path, format="xport")
        elif ext == ".sas7bdat":
            df, _ = pyreadstat.read_sas7bdat(str(path))
        elif ext == ".json":
            df = pd.read_json(path)
        elif ext == ".parquet":
            df = pd.read_parquet(path)
        else:
            print(f"Unsupported file type: {ext}")
            return None
    except Exception as e:
        print(f"Error loading {path.name}: {e}")
        return None

    if columns:
        missing_cols = [col for col in columns if col not in df.columns]
        if missing_cols:
            print(f"Missing columns {missing_cols} in {path.name}")
            return None
        df = df[columns]

    return df


def save_interim_csv(df: Optional[pd.DataFrame], name: str) -> None:
    """
    Save a DataFrame as CSV to the interim data directory.

    Args:
        df: DataFrame to save.
        name: Dataset name, used for the file name.
    """
    if df is None or df.empty:
        print(f"No data to save for {name}")
        return

    INTERIM_DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_file = INTERIM_DATA_DIR / f"{name.lower()}_interim.csv"
    try:
        df.to_csv(out_file, index=False)
        print(f"Saved interim CSV for {name} to {out_file}")
    except Exception as e:
        print(f"Failed to save CSV for {name}: {e}")


def process_datasets(dataset_config: Dict[str, dict] = datasets) -> Dict[str, pd.DataFrame]:
    """
    Validate, load, and save all datasets as defined in the config.

    Args:
        dataset_config: Dictionary of dataset metadata with file paths and optional columns.

    Returns:
        Dictionary of loaded DataFrames keyed by dataset name.
    """
    print("Starting dataset validation...")
    failed = validate_xpt_files(dataset_config)
    if failed:
        print("\nValidation failed for these datasets:")
        for name, reason in failed.items():
            print(f" - {name}: {reason}")
    else:
        print("All dataset files validated successfully.")

    loaded_dfs = {}

    for name, info in dataset_config.items():
        print(f"\nLoading dataset: {name}")
        df = load_dataset(info["file_path"], info.get("columns"))
        if df is not None:
            save_interim_csv(df, name)
            loaded_dfs[name] = df
        else:
            print(f"Skipping {name} due to loading failure or missing columns.")

    return loaded_dfs


def main() -> Dict[str, pd.DataFrame]:
    """
    Main entry point: load and save NHANES datasets, then explore them.

    Returns:
        Dictionary of loaded DataFrames.
    """
    print("=== NHANES Data Loading ===")
    all_data = process_datasets()
    print("\nData loading complete.")

    print("\n=== Exploring Loaded Datasets ===")
    for name, df in all_data.items():
        explore_data(df, name)

    return all_data


if __name__ == "__main__":
    main()