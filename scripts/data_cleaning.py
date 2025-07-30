"""
scripts\\cleaning.py

Cleans raw NHANES datasets using specific functions tailored for each dataset type.
1. Applies the appropriate cleaning function to each raw dataset.
2. Returns a dictionary of all cleaned datasets.
3. Explores the cleaned datasets using the shared explore_data utility.
"""

import sys
from pathlib import Path
import pandas as pd
from typing import Dict

# Add project root to sys.path 
project_root = Path(__file__).parent.parent.resolve()
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from scripts.clean_demo import clean_demo
from scripts.clean_clinical_exam import clean_bmi, clean_bp, clean_total_cholesterol, clean_glucose
from scripts.clean_sleep import clean_sleep
from scripts.clean_physical import clean_physical_activity
from scripts.clean_diet import clean_individual_diet,clean_total_diet
from scripts.clean_healthcare_access import clean_insurance_coverage
from scripts.clean_chronic_disease import clean_diq, clean_mcq
from scripts.clean_fped import clean_fped
from scripts.utils import explore_data


def clean_datasets(raw_dfs: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
    """
    Cleans each dataset using the appropriate cleaning function.

    Args:
        raw_dfs (Dict[str, pd.DataFrame]): Raw datasets keyed by dataset name.

    Returns:
        Dict[str, pd.DataFrame]: Cleaned datasets keyed by dataset name.
    """
    cleaning_functions = {
        "DEMO_L": clean_demo,
        "SLQ_L": clean_sleep,
        "PAQ_L": clean_physical_activity,
        "DR1TOT_L": clean_total_diet,
        "DR1IFF_L": clean_individual_diet,
        "HIQ_L": clean_insurance_coverage,
        "BMX_L": clean_bmi,
        "BPXO_L": clean_bp,
        "TCHOL_L": clean_total_cholesterol,
        "GLU_L": clean_glucose,
        "DIQ_L": clean_diq,
        "MCQ_L": clean_mcq,
        "FPED_1720": clean_fped,
    }

    cleaned_data: Dict[str, pd.DataFrame] = {}

    for name, func in cleaning_functions.items():
        if name in raw_dfs:
            print(f"Cleaning dataset: {name}")
            try:
                cleaned_data[name] = func(raw_dfs[name])
            except Exception as e:
                print(f"cleaning dataset '{name}': {e}")
        else:
            print(f"Dataset '{name}' missing from input raw datasets.")

    return cleaned_data


def main(raw_dfs: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
    """
    Run the cleaning process and explore cleaned datasets.

    Args:
        raw_dfs (Dict[str, pd.DataFrame]): Raw input datasets.

    Returns:
        Dict[str, pd.DataFrame]: Cleaned datasets.
    """
    print("Starting cleaning process...\n")
    cleaned = clean_datasets(raw_dfs)
    print("\nCleaning complete. Exploring cleaned datasets:\n")
    explore_data(cleaned) 
    return cleaned


if __name__ == "__main__":
    from data_loading import load_raw_datasets

    raw_data = load_raw_datasets()
    cleaned_data = main(raw_data)
