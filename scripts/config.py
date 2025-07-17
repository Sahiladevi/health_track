"""
config.py

Defines filesystem paths for raw, interim, clean, and processed data,
and the mapping of dataset names to their file paths and columns.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file in project root
load_dotenv()

# Use BASE_PATH from .env if available, otherwise default to parent of scripts/
BASE_PATH = Path(os.getenv("BASE_PATH", Path(__file__).resolve().parents[1]))

# directory paths
RAW_DATA_DIR = BASE_PATH / 'data' / 'raw'
INTERIM_DATA_DIR = BASE_PATH / 'data' / 'interim'
CLEAN_DATA_DIR = BASE_PATH / 'data' / 'clean'
PROCESSED_DATA_DIR = BASE_PATH / 'data' / 'processed'
FINAL_DATA_DIR =  BASE_PATH / 'data' / 'final'
# Path to SQLite database
DATABASE_PATH = BASE_PATH / "database" / "nhanes_2021_2023.db"


OUTPUTS_DIR = BASE_PATH / 'outputs'
PLOTS_DIR = OUTPUTS_DIR / 'plots'
SUMMARY_DIR = OUTPUTS_DIR / 'summary'

"""
Dictionary mapping dataset keys to file paths and selected columns.
Keys correspond to NHANES file prefixes.
To add a new dataset, include its key with file_path and columns.
"""

datasets = {
    "DEMO_L": {
        "file_path": RAW_DATA_DIR / "DEMO_L.xpt",
        "columns": [
            "SEQN", "RIAGENDR", "RIDAGEYR", "RIDRETH3", "DMDEDUC2",
            "INDFMPIR", "WTINT2YR", "WTMEC2YR", "SDMVSTRA", "SDMVPSU"
        ],
    },
    "PAQ_L": {
        "file_path": RAW_DATA_DIR / "PAQ_L.xpt",
        "columns": ["SEQN", "PAD680", "PAD790Q", "PAD790U", "PAD800"],
    },
    "SLQ_L": {
        "file_path": RAW_DATA_DIR / "SLQ_L.xpt",
        "columns": ["SEQN", "SLD012", "SLD013"],
    },
    "DR1TOT_L": {
        "file_path": RAW_DATA_DIR / "DR1TOT_L.xpt",
        "columns": ["SEQN", "DR1TKCAL", "DR1TSFAT", "DR1TSUGR", "DR1TFIBE", "WTDR2D"],
    },
    "HIQ_L": {
        "file_path": RAW_DATA_DIR / "HIQ_L.xpt",
        "columns": ["SEQN", "HIQ011"],
    },
    "BMX_L": {
        "file_path": RAW_DATA_DIR / "BMX_L.xpt",
        "columns": ["SEQN", "BMXBMI"],
    },
    "BPXO_L": {
        "file_path": RAW_DATA_DIR / "BPXO_L.xpt",
        "columns": ["SEQN", "BPXOSY1", "BPXOSY2", "BPXOSY3", "BPXODI1", "BPXODI2", "BPXODI3"],
    },
    "TCHOL_L": {
        "file_path": RAW_DATA_DIR / "TCHOL_L.xpt",
        "columns": ["SEQN", "LBXTC"],
    },  
    "GLU_L": {
        "file_path": RAW_DATA_DIR / "GLU_L.xpt",
        "columns": ["SEQN", "LBXGLU", "LBDGLUSI", "WTSAF2YR"],
    },
    "DIQ_L": {
        "file_path": RAW_DATA_DIR / "DIQ_L.xpt",
        "columns": ["SEQN", "DIQ010","DIQ070"],
    },
    "MCQ_L": {
        "file_path": RAW_DATA_DIR / "MCQ_L.xpt",
        "columns": ["SEQN", "MCQ160B", "MCQ160C", "MCQ160D", "MCQ160E"],
    },    
}

def ensure_directories():
    """Create all required directories if they don't exist."""
    for directory in [
        RAW_DATA_DIR, INTERIM_DATA_DIR, CLEAN_DATA_DIR,
        PROCESSED_DATA_DIR, FINAL_DATA_DIR,
        DATABASE_PATH.parent,  
        OUTPUTS_DIR, PLOTS_DIR, SUMMARY_DIR
    ]:
        directory.mkdir(parents=True, exist_ok=True)
    print("All required directories are ready.")


# Automatically ensure output dirs when this module is imported/run
ensure_directories()
