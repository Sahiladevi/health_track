import pandas as pd
import numpy as np
from typing import Optional

# 1. Categorizes the poverty-income ratio
def get_pir_category(pir: float) -> str:
    """
    Categorizes the poverty-income ratio into bands.

    Args:
        pir (float): The original poverty-income ratio value.

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
def categorize_activity_level(total_weekly_min: float) -> str:
    """
    Categorizes physical activity level based on total weekly minutes.

    Args:
        total_weekly_min (float): Total weekly minutes of physical activity.

    Returns:
        str: Activity level ('Low active', 'Moderately active', 'Highly active', or NaN).
    """
    if pd.isna(total_weekly_min):
        return np.nan
    elif total_weekly_min < 150:
        return "Low active"
    elif total_weekly_min < 300:
        return "Moderately active"
    else:
        return "Highly active"

# 3. Diet Score Calculation
def compute_diet_score(row: pd.Series) -> float:
    """
    Compute a basic diet score based on fiber, sugar, and saturated fat.

    Args:
        row (pd.Series): A row containing 'fiber_g', 'sugar_g', and 'sat_fat_g' fields.

    Returns:
        float: A composite diet quality score (higher = better).
    """
    score = 0
    if row['fiber_g'] > 25:
        score += 2
    elif row['fiber_g'] >= 15:
        score += 1

    if row['sugar_g'] < 50:
        score += 1
    if row['sat_fat_g'] < 20:
        score += 1

    return score

# 4. Diet Score Labeling
def label_diet_score(score: float) -> str:
    """
    Label diet score into categories.

    Args:
        score (float): The computed diet score.

    Returns:
        str: Diet category ('Healthy', 'Moderate', or 'Unhealthy').
    """
    if score >= 3:
        return "Healthy"
    elif score == 2:
        return "Moderate"
    else:
        return "Unhealthy"

# 5. Sleep Duration Categorization
def categorize_sleep(sleep_avg_hr: float) -> str:
    """
    Categorize sleep duration into quality bands.

    Args:
        sleep_avg_hr (float): Average sleep duration in hours.

    Returns:
        str: Sleep category ('Short Sleep', 'Normal Sleep', 'Long Sleep', or 'Missing').
    """
    if pd.isna(sleep_avg_hr):
        return 'Missing'
    elif sleep_avg_hr < 6:
        return "Short Sleep"
    elif 6 <= sleep_avg_hr <= 9:
        return "Normal Sleep"
    else:
        return "Long Sleep"

# 6. Obesity Flag
def flag_obesity(bmi: float) -> bool:
    """
    Determine whether a participant is obese based on BMI.

    Args:
        bmi (float): Body Mass Index.

    Returns:
        bool: True if BMI >= 30, False otherwise.
    """
    return bmi >= 30 if not pd.isna(bmi) else False

# 7. BMI Categorization
def categorize_bmi(bmi: float) -> str:
    """
    Categorize Body Mass Index into standard weight classes.

    Args:
        bmi (float): Body Mass Index.

    Returns:
        str: BMI category ('Underweight', 'Normal', 'Overweight', 'Obese').
    """
    if pd.isna(bmi):
        return 'Missing'
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# 8. Blood Pressure Categorization
def categorize_bp(systolic: float, diastolic: float) -> str:
    """
    Categorize blood pressure based on systolic and diastolic values.

    Args:
        systolic (float): Systolic blood pressure.
        diastolic (float): Diastolic blood pressure.

    Returns:
        str: Blood pressure category.
    """
    if pd.isna(systolic) or pd.isna(diastolic):
        return 'Unknown'
    if systolic >= 180 or diastolic >= 120:
        return 'Hypertensive Crisis'
    elif systolic >= 140 or diastolic >= 90:
        return 'Hypertension Stage 2'
    elif 130 <= systolic < 140 or 80 <= diastolic < 90:
        return 'Hypertension Stage 1'
    elif 120 <= systolic < 130 and diastolic < 80:
        return 'Elevated'
    elif systolic < 120 and diastolic < 80:
        return 'Normal'
    else:
        return 'Unknown'

# 9. Cholesterol Categorization
def cholesterol_category(value: float) -> str:
    """
    Categorize total cholesterol levels.

    Args:
        value (float): Total cholesterol in mg/dL.

    Returns:
        str: Category ('Desirable', 'Borderline high', 'High').
    """
    if pd.isna(value):
        return 'Missing'
    elif value < 200:
        return 'Desirable'
    elif value < 240:
        return 'Borderline high'
    else:
        return 'High'

# 10. Fasting Glucose Categorization
def glucose_category(value: float) -> str:
    """
    Categorize fasting blood glucose levels.

    Args:
        value (float): Fasting glucose in mg/dL.

    Returns:
        str: Glucose category ('Normal', 'Prediabetes', 'Diabetes').
    """
    if pd.isna(value):
        return 'Missing'
    elif value < 100:
        return 'Normal'
    elif value < 126:
        return 'Prediabetes'
    else:
        return 'Diabetes'

# 11. Glucose Abnormal Flags
def glucose_flags(value: float) -> pd.Series:
    """
    Flags hypo- and hyperglycemia based on fasting glucose levels.

    Args:
        value (float): Fasting glucose level.

    Returns:
        pd.Series: Two binary flags — 'hypoglycemia_flag' and 'hyperglycemia_flag'.
    """
    hypo = 1 if value < 70 else 0
    hyper = 1 if value > 140 else 0
    return pd.Series({'hypoglycemia_flag': hypo, 'hyperglycemia_flag': hyper})

# 12. medication 
def label_meds(val: Optional[int]) -> str:
    if val == 1:
        return 'Taking meds'
    elif val == 0:
        return 'Not taking meds'
    else:
        return 'Unknown'
    
# 13.Diabetes
def engineer_diq_features(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        print("DIQ features: Input dataframe empty. Skipping...")
        return df

    df['diabetes_meds_cat'] = df['diabetes_meds'].apply(label_meds)

    dx_1 = df['diabetes_dx'] == 1
    meds_1 = df['diabetes_meds'] == 1
    dx_0 = df['diabetes_dx'] == 0
    meds_0 = df['diabetes_meds'] == 0

    dx_1 = dx_1.fillna(False)
    meds_1 = meds_1.fillna(False)
    dx_0 = dx_0.fillna(False)
    meds_0 = meds_0.fillna(False)

    df['diabetes_status'] = np.where(dx_1 | meds_1, 1, np.where(dx_0 & meds_0, 0, np.nan))
    return df

# 14. CVD
def engineer_mcq_features(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        print("MCQ features: Input dataframe empty. Skipping...")
        return df

    # Create combined indicator: any cardiovascular condition
    df_conditions_filled = df.drop(columns=['participant_id']).fillna(0)
    df['any_cvd'] = df_conditions_filled.max(axis=1)

    return df