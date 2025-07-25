"""
scripts/feature_engineering.py

This script contains functions to create new features or categorize existing variables
from NHANES health survey data. These features help simplify complex measurements into
meaningful categories (e.g., BMI groups, sleep quality) that are easier
to analyze and interpret.

Key functionalities include:
- Categorizing poverty-income ratio, physical activity, sleep, BMI, blood pressure, cholesterol, and glucose levels.
- Creating flags and labels for diabetes and cardiovascular disease status.
- Adding binary indicators and categorical labels to improve data usability for analysis.

"""

import pandas as pd
import numpy as np
from typing import Optional


# 1. Categorizes the poverty-income ratio
def get_pir_category(pir: Optional[float]) -> str:
    """
    Categorizes the poverty-income ratio into bands.

    Args:
        pir (Optional[float]): The original poverty-income ratio value.

    Returns:
        str: Category label ('Low', 'Mid', 'High', 'Very High', or 'Missing').
    """
    if pd.isna(pir):
        return "Missing"
    elif pir < 1:
        return "Low"
    elif pir < 2:
        return "Mid"
    elif pir < 5:
        return "High"
    else:
        return "Very High"


# 2. Physical Activity Level Categorization
def categorize_activity_level(total_weekly_min: Optional[float]) -> str:
    """
    Categorizes physical activity level based on total weekly minutes.

    Args:
        total_weekly_min (Optional[float]): Total weekly minutes of physical activity.

    Returns:
        str: Activity level ('Low active', 'Moderately active', 'Highly active', or 'Missing').
    """
    if pd.isna(total_weekly_min):
        return "Missing"
    elif total_weekly_min < 150:
        return "Low active"
    elif total_weekly_min < 300:
        return "Moderately active"
    else:
        return "Highly active"

# 3. Sleep Duration Categorization
def categorize_sleep(sleep_avg_hr: Optional[float]) -> str:
    """
    Categorize sleep duration into quality bands.

    Args:
        sleep_avg_hr (Optional[float]): Average sleep duration in hours.

    Returns:
        str: Sleep category ('Short Sleep', 'Normal Sleep', 'Long Sleep', or 'Missing').
    """
    if pd.isna(sleep_avg_hr):
        return "Missing"
    elif sleep_avg_hr < 6:
        return "Short Sleep"
    elif 6 <= sleep_avg_hr <= 9:
        return "Normal Sleep"
    else:
        return "Long Sleep"


# 4. Obesity Flag
def flag_obesity(bmi: Optional[float]) -> bool:
    """
    Determine whether a participant is obese based on BMI.

    Args:
        bmi (Optional[float]): Body Mass Index.

    Returns:
        bool: True if BMI >= 30, False otherwise or missing.
    """
    if pd.isna(bmi):
        return False
    return bmi >= 30


# 5. BMI Categorization
def categorize_bmi(bmi: Optional[float]) -> str:
    """
    Categorize Body Mass Index into standard weight classes.

    Args:
        bmi (Optional[float]): Body Mass Index.

    Returns:
        str: BMI category ('Underweight', 'Normal', 'Overweight', 'Obese', or 'Missing').
    """
    if pd.isna(bmi):
        return "Missing"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# 6. Blood Pressure Categorization
def categorize_bp(systolic: Optional[float], diastolic: Optional[float]) -> str:
    """
    Categorize blood pressure based on systolic and diastolic values.

    Args:
        systolic (Optional[float]): Systolic blood pressure.
        diastolic (Optional[float]): Diastolic blood pressure.

    Returns:
        str: Blood pressure category.
    """
    if pd.isna(systolic) or pd.isna(diastolic):
        return "Unknown"
    if systolic >= 180 or diastolic >= 120:
        return "Hypertensive Crisis"
    elif systolic >= 140 or diastolic >= 90:
        return "Hypertension Stage 2"
    elif 130 <= systolic < 140 or 80 <= diastolic < 90:
        return "Hypertension Stage 1"
    elif 120 <= systolic < 130 and diastolic < 80:
        return "Elevated"
    elif systolic < 120 and diastolic < 80:
        return "Normal"
    else:
        return "Unknown"


# 7. Cholesterol Categorization
def cholesterol_category(value: Optional[float]) -> str:
    """
    Categorize total cholesterol levels.

    Args:
        value (Optional[float]): Total cholesterol in mg/dL.

    Returns:
        str: Category ('Desirable', 'Borderline high', 'High', or 'Missing').
    """
    if pd.isna(value):
        return "Missing"
    elif value < 200:
        return "Desirable"
    elif value < 240:
        return "Borderline high"
    else:
        return "High"


# 8. Fasting Glucose Categorization
def glucose_category(value: Optional[float]) -> str:
    """
    Categorize fasting blood glucose levels.

    Args:
        value (Optional[float]): Fasting glucose in mg/dL.

    Returns:
        str: Glucose category ('Normal', 'Prediabetes', 'Diabetes', or 'Missing').
    """
    if pd.isna(value):
        return "Missing"
    elif value < 100:
        return "Normal"
    elif value < 126:
        return "Prediabetes"
    else:
        return "Diabetes"


# 9. Glucose Abnormal Flags
def glucose_flags(value: Optional[float]) -> pd.Series:
    """
    Flags hypo- and hyperglycemia based on fasting glucose levels.

    Args:
        value (Optional[float]): Fasting glucose level.

    Returns:
        pd.Series: Two binary flags — 'hypoglycemia_flag' and 'hyperglycemia_flag'.
    """
    if pd.isna(value):
        hypo = 0
        hyper = 0
    else:
        hypo = 1 if value < 70 else 0
        hyper = 1 if value > 140 else 0
    return pd.Series({'hypoglycemia_flag': hypo, 'hyperglycemia_flag': hyper})


# 10. Medication Labeling
def label_meds(val: Optional[int]) -> str:
    """
    Label medication status.

    Args:
        val (Optional[int]): Medication flag (1, 0, or missing).

    Returns:
        str: Medication status label.
    """
    if val == 1:
        return "Taking meds"
    elif val == 0:
        return "Not taking meds"
    else:
        return "Unknown"


# 11. Diabetes Feature Engineering
def engineer_diq_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Engineer diabetes-related features from diagnosis and medication indicators.

    Args:
        df (pd.DataFrame): Input dataframe containing 'diabetes_dx' and 'diabetes_meds' columns.

    Returns:
        pd.DataFrame: DataFrame with added 'diabetes_meds_cat' and 'diabetes_status' columns.
    """
    if df.empty:
        print("DIQ features: Input dataframe empty. Skipping...")
        return df

    if not {'diabetes_dx', 'diabetes_meds'}.issubset(df.columns):
        raise KeyError("Input DataFrame must contain 'diabetes_dx' and 'diabetes_meds' columns.")

    df['diabetes_meds_cat'] = df['diabetes_meds'].apply(label_meds)

    dx_1 = df['diabetes_dx'].fillna(0) == 1
    meds_1 = df['diabetes_meds'].fillna(0) == 1
    dx_0 = df['diabetes_dx'].fillna(0) == 0
    meds_0 = df['diabetes_meds'].fillna(0) == 0

    df['diabetes_status'] = np.where(dx_1 | meds_1, 1, np.where(dx_0 & meds_0, 0, np.nan))
    return df


# 12. Cardiovascular Disease Feature Engineering
def engineer_mcq_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Engineer cardiovascular disease indicator from multiple condition flags.

    Args:
        df (pd.DataFrame): Input dataframe containing condition indicator columns.

    Returns:
        pd.DataFrame: DataFrame with added 'any_cvd' column.
    """
    if df.empty:
        print("MCQ features: Input dataframe empty. Skipping...")
        return df

    # Exclude non-condition columns if present
    exclude_cols = ['participant_id']
    condition_cols = [col for col in df.columns if col not in exclude_cols]

    # Check if all condition columns are numeric or boolean, else coerce or fillna
    cond_df = df[condition_cols].fillna(0)

    df['any_cvd'] = cond_df.max(axis=1)

    return df
