"""
scripts\\config.py

Defines filesystem paths for raw, interim, clean, and processed data,
and the mapping of dataset names to their file paths and columns
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file in project root
load_dotenv()

# Relative to the location of config.py
base_path_env = os.getenv("BASE_PATH", "..")
BASE_PATH = Path(__file__).parent / base_path_env

# directory paths
RAW_DATA_DIR = BASE_PATH / 'data' / 'raw'
INTERIM_DATA_DIR = BASE_PATH / 'data' / 'interim'
CLEAN_DATA_DIR = BASE_PATH / 'data' / 'clean'
PROCESSED_DATA_DIR = BASE_PATH / 'data' / 'processed'
FINAL_DATA_DIR =  BASE_PATH / 'data' / 'final'
# Path to SQLite database
DATABASE_PATH = BASE_PATH / "database" / "nhanes_2021_2023.db"

INSIGHT_DIR = BASE_PATH / 'dashboard' / 'insights'


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
        "columns": ["SEQN", "DR1TKCAL", "DR1TSFAT", "DR1TSODI","WTDRD1"],
    },

    "DR1IFF_L": {
        "file_path": RAW_DATA_DIR / "DR1IFF_L.xpt",
        "columns": ["SEQN", "DR1IGRMS", "DR1IKCAL", "WTDRD1", "DR1IFDCD"] ,   
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
        "columns": ["SEQN", "LBXTC","WTPH2YR"],
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
    "FPED_1720": {
        "file_path": RAW_DATA_DIR / "FPED_1720.xls",
        "columns": ['FOODCODE', 'DESCRIPTION', 'F_TOTAL (cup eq)', 'F_JUICE (cup eq)', 'F_CITMLB (cup eq)', 
        'F_OTHER (cup eq)', 'V_TOTAL (cup eq)', 'V_DRKGR (cup eq)', 'V_LEGUMES (cup eq)',
        'G_WHOLE (oz eq)', 'G_REFINED (oz eq)', 'D_TOTAL (cup eq)', 'D_MILK (cup eq)', 
        'D_YOGURT (cup eq)', 'D_CHEESE (cup eq)', 'PF_TOTAL (oz eq)', 'PF_MPS_TOTAL (oz eq)',
        'PF_SEAFD_HI (oz eq)', 'PF_SEAFD_LOW (oz eq)', 'SOLID_FATS (grams)', 'ADD_SUGARS (tsp eq)', 'OILS (grams)'],
        "sheet_name": "FPED_1720_"  
    },   
}

# function to ensure directory exists
def ensure_directories() -> None:
    """
    Make sure all the important folders for the project exist.
    
    This goes through a list of directories we need (like for raw data,
    processed data, outputs, etc.) and creates them if they aren't already there.
    It also prints out where the main project folder is, relative to where
    you're running the script — or gives the full path if it can't figure that out.
    """
    for directory in [
        RAW_DATA_DIR, INTERIM_DATA_DIR, CLEAN_DATA_DIR,
        PROCESSED_DATA_DIR, FINAL_DATA_DIR,
        DATABASE_PATH.parent,
        OUTPUTS_DIR, PLOTS_DIR, SUMMARY_DIR
    ]:
        # Create the directory if it doesn't exist (and create any parent folders too)
        directory.mkdir(parents=True, exist_ok=True)

    print("Project directories are ready.")


