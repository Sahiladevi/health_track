"""
scripts\\data_loading.py

This script handles loading the raw NHANES data files with the required columns/fields,
checks if they're valid, saves cleaned-up versions to interim CSVs,
and then runs some quick exploration using helper functions.
"""

from pathlib import Path
from typing import Optional, List, Union, Dict
import pandas as pd
import pyreadstat

from config import datasets, INTERIM_DATA_DIR
from utils import validate_xpt_files, explore_data, pretty_path

# 1. function for load_file_as_dataframe 
def load_dataset(
    file_path: Union[str, Path], 
    columns: Optional[List[str]] = None, 
    sheet_name: Optional[str] = None
) -> Optional[pd.DataFrame]:
    """
    Loads a dataset from a file into a pandas DataFrame.

    You can optionally tell it which columns you care about. 
    If anything goes wrong (like the file doesn't exist, 
    or it's missing columns you asked for), it'll just return None.

    Args:
        file_path: Where the file is located (CSV, Excel, XPT, etc.).
        columns: A list of columns you want to keep (optional).

    Returns:
        A DataFrame if it loads correctly, otherwise None.
    """
    path = Path(file_path)
    if not path.exists():
        print(f"File not found: {pretty_path(path)}")
        return None

    ext = path.suffix.lower()

    try:
        if ext == ".csv":
            df = pd.read_csv(path)
        elif ext in [".xls", ".xlsx"]:
            df = pd.read_excel(path, sheet_name=sheet_name)
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
        print(f"Error loading {pretty_path(path)}: {e}")
        return None

    # If you only want certain columns, check that they exist first
    if columns:
        missing_cols = [col for col in columns if col not in df.columns]
        if missing_cols:
            print(f"Missing columns {missing_cols} in {pretty_path(path)}")
            return None
        df = df[columns]

    return df

# 2. function for saving file in interim data folder
def save_interim_file(df: Optional[pd.DataFrame], name: str, original_ext: str) -> None:
    """
    Saves a DataFrame as a CSV or Excel file in the interim data folder,
    depending on the original file extension.

    Args:
        df: The data you want to save.
        name: A short name for the dataset (used for the filename).
        original_ext: The original file extension (like '.xls', '.xlsx', '.xpt', etc.).
    """
    if df is None or df.empty:
        print(f"No data to save for {name}")
        return

    INTERIM_DATA_DIR.mkdir(parents=True, exist_ok=True)

    ext = original_ext.lower()

    if ext in ['.xls', '.xlsx']:
        out_file = INTERIM_DATA_DIR / f"{name.lower()}_interim.xlsx"
        try:
            df.to_excel(out_file, index=False)
            print(f"Saved interim Excel file for {name} to {pretty_path(out_file)}")
        except Exception as e:
            print(f"Failed to save Excel file for {name}: {e}")
    else:
        # Default to CSV for other types
        out_file = INTERIM_DATA_DIR / f"{name.lower()}_interim.csv"
        try:
            df.to_csv(out_file, index=False)
            print(f"Saved interim CSV for {name} to {pretty_path(out_file)}")
        except Exception as e:
            print(f"Failed to save CSV for {name}: {e}")
            

# 3. function for loading data from config file
def process_datasets(dataset_config: Dict[str, dict] = datasets) -> Dict[str, pd.DataFrame]:
    """
    Goes through all datasets in the config:
    - validates them,
    - loads the data,
    - saves interim versions,
    - and collects everything into a dictionary.

    Args:
        dataset_config: Info about all the datasets — paths, columns to keep, etc.

    Returns:
        A dictionary of the loaded DataFrames, keyed by their names.
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
        sheet_name = info.get("sheet_name")  # <-- NEW
        df = load_dataset(info["file_path"], info.get("columns"), sheet_name=sheet_name)
        if df is not None:
            file_ext = Path(info["file_path"]).suffix.lower()
            save_interim_file(df, name, file_ext)
            loaded_dfs[name] = df
        else:
            print(f"Skipping {name} due to loading failure or missing columns.")

    return loaded_dfs

# 4. function for load_validated_datasets_from_config
def load_raw_datasets() -> Dict[str, pd.DataFrame]:
    """
    Loads and returns raw NHANES datasets from config.

    This function is designed for reuse across scripts.
    """
    return process_datasets()


def main() -> Dict[str, pd.DataFrame]:
    """
    Main function that kicks off everything:
    - Loads all datasets
    - Saves interim versions
    - Runs some basic exploration on each

    Returns:
        A dictionary of all the loaded DataFrames.
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
