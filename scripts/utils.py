"""
utils.py

Common utility functions for NHANES project:
- Validation of SAS transport files (.xpt)
- Data exploration summaries
- Data cleaning helpers.
"""
import pandas as pd
import numpy as np
from pathlib import Path
import pyreadstat
from typing import Dict, List, Optional, Union


def validate_xpt_files(datasets: Dict[str, Dict[str, str]]) -> Dict[str, str]:
    failed_files = {}
    for name, info in datasets.items():
        file_path = Path(info["file_path"])
        if file_path.exists():
            print(f"File found for: {name}")
            try:
                data = pd.read_sas(file_path, format="xport")
                print(f"Successfully read {name} with pandas. Rows: {len(data)}")
            except Exception as e:
                print(f"Could not read {name} with pandas due to: {e}")
                try:
                    data, meta = pyreadstat.read_sas7bdat(str(file_path))
                    print(f"Successfully read {name} with pyreadstat. Rows: {len(data)}")
                except Exception as e:
                    print(f"Failed to read {name} due to: {e}")
                    failed_files[name] = f"Error reading file: {e}"
        else:
            print(f"File not found for: {name}")
            failed_files[name] = "File missing"
    return failed_files

def show_missing(df: pd.DataFrame, name: str) -> None:
    """
    Print the number of missing values for each column in a dataframe.

    Args:
        df: The dataframe to inspect.
        name: A label for the dataset (just for display purposes).
    """
    print(f"Missing values in dataset: {name}")
    print(df.isnull().sum())


def rename_columns(df: pd.DataFrame, new_names: Dict[str, str]) -> pd.DataFrame:
    """
    Rename columns in the dataframe using the provided mapping.

    Args:
        df: The original dataframe.
        new_names: Dictionary mapping current column names to new names.

    Returns:
        A new dataframe with updated column names.
    """
    return df.rename(columns=new_names)


def drop_missing(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Drop rows from the dataframe if they have missing values in any of the specified columns.

    Args:
        df: The dataframe to filter.
        columns: List of columns to check for missing values.

    Returns:
        A filtered dataframe with rows removed where specified columns had NaNs.
    """
    return df.dropna(subset=columns)


def remove_outliers(df: pd.DataFrame, column: str, min_value: float, max_value: float) -> pd.DataFrame:
    """
    Remove rows where the values in a specific column fall outside a defined range.

    Args:
        df: The input dataframe.
        column: The column to apply outlier filtering on.
        min_value: Minimum acceptable value.
        max_value: Maximum acceptable value.

    Returns:
        A dataframe with outlier rows removed.
    """
    return df[(df[column] >= min_value) & (df[column] <= max_value)]


def drop_invalid_weight(
    df: pd.DataFrame,
    weight_column: str,
    min_valid: float = 100,
    max_valid: float = 1_000_000
) -> pd.DataFrame:
    """
    Drop rows where the weight column is missing, zero, negative, or outside a valid range.

    Args:
        df: The dataframe to clean.
        weight_column: The name of the weight column.
        min_valid: Minimum acceptable value (default=100).
        max_valid: Maximum acceptable value (default=1,000,000).

    Returns:
        Filtered dataframe with only valid weights.
    """
    cleaned_df = df[
        df[weight_column].notna() &
        (df[weight_column] >= min_valid) &
        (df[weight_column] <= max_valid)
    ]
    return cleaned_df


def replace_zeros_with_nan(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Replace zeros with NaNs in selected columns.

    Args:
        df: The dataframe to update.
        columns: List of columns where 0 should be treated as missing.

    Returns:
        The updated dataframe with 0s replaced by NaNs in the specified columns.
    """
    df = df.copy()
    for col in columns:
        df[col] = df[col].replace(0, np.nan)
    return df


def replace_close_values_with_nan(
    df: pd.DataFrame,
    target: float,
    tolerance: float,
    columns: Optional[List[str]] = None
) -> pd.DataFrame:
    """
    Replace values that are within a given tolerance of a target value with NaN.

    Args:
        df: The dataframe to work on.
        target: The reference value to compare against.
        tolerance: How close a value can be to the target before being replaced.
        columns: Specific columns to apply this to. If None, it will apply to all numeric columns.

    Returns:
        The modified dataframe with close values replaced by NaN.
    """
    df = df.copy()
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns

    for col in columns:
        if col in df.columns:
            df[col] = df[col].apply(
                lambda x: np.nan if pd.notna(x) and abs(x - target) <= tolerance else x
            )
        else:
            print(f"Column '{col}' not found in dataframe.")
    return df


def explore_data(
    data: Union[pd.DataFrame, Dict[str, pd.DataFrame]],
    name: Optional[str] = None
) -> None:
    """
    Print a comprehensive summary of the dataset or datasets.

    Args:
        data: A single DataFrame or a dictionary of DataFrames to explore.
        name: Optional dataset name (used if data is a single DataFrame).
    """
    def explore_single_df(df: pd.DataFrame, dataset_name: str) -> None:
        if df is None or df.empty:
            print(f"No data to explore for {dataset_name}")
            return
        print(f"\n--- Exploring {dataset_name} ---")
        print(f"Shape: {df.shape}")
        print("First 5 rows:")
        print(df.head())
        print("\nInfo:")
        print(df.info())
        print("\nData types:")
        print(df.dtypes)
        print("\nSummary statistics (including categorical):")
        print(df.describe(include='all').T)
        print("\nMissing values per column:")
        print(df.isnull().sum())
        print("\nColumn names:")
        print(df.columns.to_list())
        print("\nUnique values per column:")
        print(df.nunique())
        print(f"\nDuplicated rows count: {df.duplicated().sum()}")
        cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        num_cols = df.select_dtypes(include=['number']).columns.tolist()
        print("\nCategorical columns:", cat_cols)
        print("Numerical columns:", num_cols)
        print("-" * 40)

    if isinstance(data, dict):
        for dataset_name, df in data.items():
            explore_single_df(df, dataset_name)
    else:
        if not name:
            name = "Dataset"
        explore_single_df(data, name)
