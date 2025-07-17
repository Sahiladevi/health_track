import pandas as pd
import sqlite3
from pathlib import Path


# Database Connection Utilities
def create_connection_from_script(relative_path_to_db: str) -> sqlite3.Connection | None:
    try:
        script_dir = Path(__file__).parent
        db_path = (script_dir / relative_path_to_db).resolve()
        conn = sqlite3.connect(db_path)
        print(f"Connected to database at: {db_path}")
        return conn
    except sqlite3.Error as e:
        print(f"Failed to connect to database: {e}")
        return None

def create_connection(db_file: str) -> sqlite3.Connection:
    return sqlite3.connect(db_file)

def close_connection(conn: sqlite3.Connection) -> None:
    if conn:
        conn.commit()
        conn.close()
        print("Database connection closed.")


# NHANES Table Schemas 
NHANES_TABLE_SCHEMAS = {
    "demographics": """
        CREATE TABLE IF NOT EXISTS demographics (
            participant_id TEXT PRIMARY KEY,
            gender TEXT,
            age INTEGER,
            race_ethnicity TEXT,
            education_level TEXT,
            poverty_income_ratio REAL,
            interview_sample_weight REAL,
            exam_sample_weight REAL,
            strata REAL,
            psu REAL,
            pir_category TEXT
        );
    """,
    "health_insurance": """
        CREATE TABLE IF NOT EXISTS health_insurance (
            participant_id TEXT PRIMARY KEY,
            has_health_insurance TEXT
        );
    """,
    "sleep": """
        CREATE TABLE IF NOT EXISTS sleep (
            participant_id TEXT PRIMARY KEY,
            sleep_avg_hr REAL,
            sleep_category TEXT
        );
    """,
    "physical_activity": """
        CREATE TABLE IF NOT EXISTS physical_activity (
            participant_id TEXT PRIMARY KEY,
            activity_level TEXT,
            sedentary_min_per_week REAL,
            total_weekly_min REAL
        );
    """,
    "diet": """
        CREATE TABLE IF NOT EXISTS diet (
            participant_id TEXT PRIMARY KEY,
            diet_weight REAL,
            diet_score REAL,
            diet_category TEXT
        );
    """,
    "bmi": """
        CREATE TABLE IF NOT EXISTS bmi (
            participant_id TEXT PRIMARY KEY,
            bmi REAL,
            obese INTEGER
        );
    """,
    "bp": """
        CREATE TABLE IF NOT EXISTS bp (
            participant_id TEXT PRIMARY KEY,
            systolic_avg REAL,
            diastolic_avg REAL,
            bp_category TEXT
        );
    """,
    "total_cholestrol": """
        CREATE TABLE IF NOT EXISTS total_cholestrol (
            participant_id TEXT PRIMARY KEY,
            total_cholesterol REAL,
            cholesterol_category TEXT
        );
    """,
    "glucose": """
        CREATE TABLE IF NOT EXISTS glucose (
            participant_id TEXT PRIMARY KEY,
            fasting_glucose_mg_dl REAL,
            fasting_subsample_weight REAL,
            glucose_category TEXT,
            hypoglycemia_flag INTEGER,
            hyperglycemia_flag INTEGER,
            log_fasting_glucose_mg_dl REAL
        );
    """,
    "diabetes": """
        CREATE TABLE IF NOT EXISTS diabetes (
            participant_id TEXT PRIMARY KEY,
            diabetes_dx INTEGER,
            diabetes_meds INTEGER,
            diabetes_meds_cat TEXT,
            diabetes_status TEXT
        );
    """,
    "cardio_vascular": """
        CREATE TABLE IF NOT EXISTS cardio_vascular (
            participant_id TEXT PRIMARY KEY,
            congestive_heart_failure INTEGER,
            coronary_heart_disease INTEGER,
            angina INTEGER,
            heart_attack INTEGER,
            any_cvd INTEGER
        );
    """
}

def create_nhanes_tables(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    for table, schema in NHANES_TABLE_SCHEMAS.items():
        cursor.execute(schema)
        print(f"Created table '{table}'")
    conn.commit()
    print("All required NHANES tables created successfully.")


# DataFrame to SQLite Saver

def save_to_sqlite(
    df: pd.DataFrame,
    conn: sqlite3.Connection,
    table_name: str,
    if_exists: str = "append",
    recreate: bool = False
) -> None:
    """
    Save a DataFrame to a SQLite table.

    Parameters:
        df: pandas DataFrame
        conn: sqlite3.Connection object
        table_name: Target table name
        if_exists: Use 'append' or 'fail'
        recreate: If True, drops and recreates the table before inserting
    """
    cursor = conn.cursor()

    try:
        if recreate:
            if table_name in NHANES_TABLE_SCHEMAS:
                cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
                cursor.execute(NHANES_TABLE_SCHEMAS[table_name])
                conn.commit()
                print(f"Recreated table '{table_name}'")
            else:
                raise ValueError(f"No schema found for table '{table_name}'")

        # Get table schema columns
        cursor.execute(f"PRAGMA table_info({table_name});")
        table_info = cursor.fetchall()

        if not table_info:
            raise ValueError(f"Table '{table_name}' does not exist in the database.")

        table_columns = [col[1] for col in table_info]

        matching_columns = [col for col in df.columns if col in table_columns]
        if not matching_columns:
            raise ValueError(f"None of the DataFrame columns match '{table_name}'")

        filtered_df = df[matching_columns]
        dropped = set(df.columns) - set(filtered_df.columns)
        if dropped:
            print(f"Dropping columns not in table '{table_name}': {sorted(dropped)}")

        filtered_df.to_sql(table_name, conn, if_exists=if_exists, index=False)
        print(f"Inserted {len(filtered_df)} rows into '{table_name}'")

    except sqlite3.IntegrityError as e:
        print(f"Integrity constraint error for '{table_name}': {e}")
    except sqlite3.Error as e:
        print(f"SQLite error while saving to '{table_name}': {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# SQL Query Runner

def run_query(conn: sqlite3.Connection, query: str) -> pd.DataFrame:
    return pd.read_sql_query(query, conn)
