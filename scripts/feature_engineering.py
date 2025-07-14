import pandas as pd
import numpy as np

# Categorizes the poverty-income ratio
def get_pir_category(pir: float) -> str:
    """
    Categorizes the poverty-income ratio into bands.

    Args:
        pir (float): The original poverty-income ratio value.

    Returns:
        str: Category label (e.g., 'Low', 'Mid', 'High', etc.).
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


# Activity_level categorization
def categorize_activity_level(total_weekly_min: float) -> str:
    """
    Categorizes physical activity level based on total weekly minutes.

    Args:
        minutes (float): Total weekly minutes of physical activity.

    Returns:
        str: Category label ('Low active', 'Moderately active', or 'Highly active').
    """
    if pd.isna(total_weekly_min):
        return np.nan
    if total_weekly_min < 150:
        return "Low active"
    elif total_weekly_min < 300:
        return "Moderately active"
    else:
        return "Highly active"

# Diet score 
def compute_diet_score(row: pd.Series) -> float:
    """
    Compute a basic diet score based on fiber, sugar, and saturated fat.
    
    Parameters:
        row (pd.Series): A row from the dietary DataFrame.
    
    Returns:
        float: A composite diet quality score (higher = better).
    """
    score = 0
    # More fiber = better, more sugar/fat = worse
    if row['fiber_g'] > 25:
        score += 2
    elif row['fiber_g'] >= 15:
        score += 1

    if row['sugar_g'] < 50:
        score += 1
    if row['sat_fat_g'] < 20:
        score += 1

    return score

def label_diet_score(score: int) -> str:
    if score >= 3:
        return "Healthy"
    elif score == 2:
        return "Moderate"
    else:
        return "Unhealthy"


# Sleep categorization
def categorize_sleep(sleep_avg_hr: float) -> str:
    """
    Categorize sleep duration into quality bands.
    
    Parameters:
        sleep_avg_hr (float): Average sleep duration in hours.
    
    Returns:
        str: 'Short', 'Recommended Sleep', 'Long Sleep', or NAN
    """
    if pd.isna(sleep_avg_hr):
        return 'Missing'
    if sleep_avg_hr < 6:
        return "Short Sleep"
    elif 6 <= sleep_avg_hr <= 9:
        return "Normal Sleep"
    else:
        return "Long Sleep"   


def flag_obesity(bmi: float) -> bool:
    """
    Determine whether a participant is obese.
    
    Parameters:
        bmi (float): Body Mass Index
    
    Returns:
        bool: True if obese, False otherwise
    """
    return bmi >= 30 if not pd.isna(bmi) else False

# BMI Categorization
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
    
# Blood Pressure Categorization
def categorize_bp(systolic: float, diastolic: float) -> str:
    """
    Categorize blood pressure based on systolic and diastolic averages.

    Categories:
    - Normal
    - Elevated
    - Hypertension Stage 1
    - Hypertension Stage 2
    - Hypertensive Crisis

    Args:
        systolic (float): Average systolic blood pressure.
        diastolic (float): Average diastolic blood pressure.

    Returns:
        str: BP category label.
    """ 
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



    


