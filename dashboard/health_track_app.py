import streamlit as st
from PIL import Image
import sys
from pathlib import Path
import pandas as pd
import streamlit.components.v1 as components  

# --- Add project root to sys.path ---
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from scripts.config import SUMMARY_DIR, PLOTS_DIR, INSIGHT_DIR

if not INSIGHT_DIR.exists():
    INSIGHT_DIR.mkdir(parents=True, exist_ok=True)

# Page setup
st.set_page_config(page_title="Health Dashboard", layout="wide")
st.title("NHANES 2021-2023: Lifestyle, Socioeconomic & Health Outcomes")

# Project Overview and Scope
st.markdown("""
### Project Overview
Explore how lifestyle habits, socioeconomic factors, and healthcare access relate to health outcomes among U.S. adults, including BMI, blood pressure, cholesterol, glucose, and chronic diseases. Differences by gender and race/ethnicity are also highlighted to support evidence-based interventions.

### Sections
- **Distribution:** Patterns of lifestyle and socioeconomic factors.
- **Associations:** Links between these factors and health outcomes.
- **Relationships:** Specific factor outcome connections (e.g., sleep → BMI).
- **Interactions:** Combined effects of multiple factors.
- **Disparities:** Differences across gender and racial/ethnic groups.
- **Modifiers:** Effect modification by gender or race/ethnicity.
- **Interventions:** Recommendations for reducing disparities and promoting health equity.
""")

# Sidebar: select objective
objective = st.sidebar.selectbox("Select Objective", [
    "Distribution", "Associations", "Relationships", "Interactions",
    "Disparities", "Modifiers", "Interventions"
])

# Objective dictionaries (abbreviated for brevity; paste your full dicts here)
obj_1_1_outcomes = {
    "Unweighted Distribution": {
        "description": "Summary of lifestyle and background factors based on raw survey data without population weighting.",
        "plot": [
            "obj_1.1_lifestyle_and_socio_economic_unweighted_stats_plots.png",
            "obj_1.1_income_treemap_unweighted.png",
            "obj_1.1_sunburst_insurance_by_gender_unweighted.html"
        ],        
        "summary": "obj_1.1_lifestyle_and_socio_economic_unweighted_stats_report.xlsx",
        "insight": "obj_1.1_unweighted_distribution.txt"
    },
    "Weighted Distribution": {
        "description": "Summary of lifestyle and background characteristics adjusted to reflect the demographic makeup of the national population using survey sampling weights.",
        "plot": "obj_1.1_lifestyle_and_socio_economic_weighted_stats_distribution_plots.png",        
        "summary": "obj_1.1_lifestyle_and_socio_economic_weighted_stats_report.xlsx",
        "insight": "obj_1.1_weighted_distribution.txt",
    }
}

# Objective 1.2 outcomes
obj_1_2_outcomes = {
    "BMI": {
        "description": "Looks at how things like diet, activity, and income relate to body weight and BMI.",        
        "plot": "obj_1.2_bmi_quantify_association_regression_analysis_plot.png",        
        "summary": "obj_1.2_bmi_quantify_association_regression_analysis_summary.txt",
        "insight": "obj_1.2_bmi.txt"
    },
    "Blood Pressure": {
        "description": "Studies how lifestyle and background factors affect blood pressure levels.",
        "plot": "obj_1.2_bp_model_diagnostics_combined_plot.png",        
        "summary": "obj_1.2_bp_model_quantify_association_summary.txt",
        "insight": "obj_1.2_bp.txt"
    },
    "Cholesterol": {
        "description": "Explores connections between personal habits and cholesterol levels.",
        "plot": "obj_1.2_total_cholesterol_quantify_association_plot.png",        
        "summary": "obj_1.2_total_cholesterol_quantify_association_regression_summary.txt",
        "insight": "obj_1.2_cholesterol.txt"
    },
    "Glucose": {
        "description": "Examines how different factors are linked to blood sugar levels.",
        "plot": "obj_1.2_fasting_glucose_quantify_association_plot.png",        
        "summary": "obj_1.2_fasting_glucose_quantify_association_regression_summary.txt",
        "insight": "obj_1.2_glucose.txt"
    },
    "Diabetes": {
        "description": "Looks at what increases or lowers the chances of having diabetes.",
        "plot": "obj_1.2_diabetes_odds_ratios_plot.png",       
        "summary": "obj_1.2_diabetes_quantify_association_regression_summary.txt",
        "insight": "obj_1.2_diabetes.txt"
    },
    "Cardiovascular Disease": {
        "description": "Explores what makes people more or less likely to have heart disease.",
        "plot": "obj_1.2_cardio_vascular_odds_ratios_plot.png",        
        "summary": "obj_1.2_cardio_vascular_quantify_association_regression_summary.txt",
        "insight": "obj_1.2_cvd.txt"
    }
}

# Objective 1.3 outcomes
obj_1_3_outcomes = {
    "Sleep duration & BMI/BP": {
        "description": "Looks at how the amount of sleep people get relates to their weight and blood pressure.",
        "plot": "obj_1.3_sleep_vs_bmi_bp_specific_relationship_plot.png",        
        "summary": [
            "obj_1.3_sleep_duration_and_bmi_specific_relationship_summary.txt",
            "obj_1.3_sleep_duration_and_systolic_bP_specific_relationship_summary.txt",
            "obj_1.3_sleep_duration_and_diastolic_bP_specific_relationship_summary.txt"
        ],
        "insight": "obj_1.3_sleep_duration_bmi_bp_specific_relationship.txt"
    },
    "Sleep category & BMI/BP": {
        "description": "Compares how different types of sleep habits relate to weight and blood pressure.",
        "plot": "obj_1.3_bmi_bp_sleep_category_specific_relationship_plot.png",        
        "summary": "obj_1.3_sleep_category_bmi_bp_specific_relationship_regression_summary.txt",
        "insight": "obj_1.3_sleep_category_bmi_bp_specific_relationship.txt"
    },
    "Income/Education & Cholesterol": {
        "description": "Shows how income and education levels are connected to cholesterol levels.",
        "plot": "obj_1.3_chol_vs_pir_edu_bar_plot.png",        
        "summary": "obj_1.3_pir_education_vs_cholesterol_summary.txt",
        "insight": "obj_1.3_income_education_cholesterol_specific_relationship.txt"
    },
    "Income/Education & Obesity": {
        "description": "Explores how income and education affect the chances of being obese.",
        "plot": "obj_1.3_obesity_probability_by_pir_edu_specific_relationship_plot.png",        
        "summary": "obj_1.3_Obesity_by_PIR_and_Education_Level_specific_relationship_summary.txt",
        "insight": "obj_1.3_income_education_and_obesity_specific_relationship.txt"
    },
    "Income/Education/Sleep duration & Diabetes": {
        "description": "Looks at how income, education, and sleep habits together influence diabetes risk.",
        "plot": "obj_1.3_diabetes_probability_by_pir_edu_specific_relationship.png",        
        "summary": "obj_1.3_diabetes_by_PIR_and_Education_Level_specific_relation_summary.txt",
        "insight": "obj_1.3_sleep_income_education_and_diabetes_specific_relationship.txt"
    },
}

# Objective 1.4 outcomes
obj_1_4_outcomes = {
    "Diet & Activity Effects on Clinical Indicators": {
        "description": "Shows how eating well and staying active work together to affect things like blood pressure and cholesterol.",
        "plot": [
            "obj_1.4_combined_effects_diet_activity_all_outcomes.png",
            "obj_1.4_interaction_effects_diet_activity_clinical_indicators.png"
        ],        
        "summary": ["obj_1.4_combined_effects_of_diet_quality_and_physical_activity_on_systolic_bp.txt","obj_1.4_combined_effects_of_diet_quality_and_physical_activity_on_bmi.txt","obj_1.4_combined_effects_of_diet_quality_and_physical_activity_on_cholestrol.txt"],
        "insight": "obj_1.4_sbp_dbp_bmi_cholesterol.txt",

    },
    "Combined Effects of BP & Glucose on CVD": {
        "description": "Explores how blood pressure and blood sugar levels together impact heart disease risk.",
        "plot": "obj_1.4_combined_effects_of_blood_pressure_and_glucose_levels_on_cardiovascular_disease_plot.png",
        "summary": "obj_1.4_combined_effects_of_blood_pressure_and_glucose_levels_on_cardiovascular_disease_summary.txt",
        "insight": "obj_1.4_cvd.txt"
    }
}

# Objective 2.1 outcomes
obj_2_1_outcomes = {
    "Distribution by Gender & Race (Unweighted)": {
        "description": "Shows how key health and lifestyle factors vary between men and women and across racial groups, without adjusting for population size.",
        "plot": "obj_2.1_distribution_across_gender_and_race_without_weight.png",
        "summary": "obj_2.1_summary_by_gender_race_without_weight.csv",
        "insight": "obj_2.1_group_comparison_unweighted.txt"
    },
    "Distribution by Gender & Race (Weighted)": {
        "description": "Shows how key health and lifestyle factors vary between men and women and across racial groups, with adjusting for population size.",
        "plot": [
            "obj_2.1_weighted_distribution_across_gender_and_race.png",
            "obj_2.1_compare_distributions_across_gender_and_race_combined_plots.html"
        ],
        "summary": "obj_2.1_weighted_summary_by_gender_race_with_weight.csv",
        "insight": "obj_2.1_group_comparison_weighted.txt"
    }
}
# Objective 2.2 outcomes
obj_2_2_outcomes = {
    "PIR, Gender & Obesity Interaction": {
        "description": "Explores how income level and gender together affect the chances of being obese.",
        "plot": "obj_2.2_pir_gender_obesity_interaction_analysis.png",
        "summary": "obj_2.2_pir_gender_obesity_interaction_analysis.txt",
        "insight": "obj_2.2_income_and_obesity_and_gender.txt"
    },
    "Sleep & Race Relationship to BMI": {
        "description": "Looks at how sleep patterns and race may combine to affect body weight.",
        "plot": "obj_2.2_combined_sleep_bmi_interaction_plot.png",
        "summary": "obj_2.2_sleep_bmi_by_race.txt",
        "insight": "obj_2.2_sleep_and_race_with_bmi.txt"
        
    },
    "Diet and Cholesterol — Gender Differences": {
        "description": "Shows how the link between diet and cholesterol may differ for men and women.",
        "plot": "obj_2.2_combined_diet_cholesterol_by_gender.png",
        "summary": "obj_2.2_diet_cholesterol_by_gender.txt",
        "insight": "obj_2.2_diet_and_cholesterol_and_gender.txt"
        
    },
    "Diet Quality & Diabetes Risk by Gender": {
        "description": "Explores how good or poor diet affects diabetes risk for men and women separately.",
        "plot": "obj_2.2_combined_diet_score_and_gender_on_diabetes.png",
        "summary": "obj_2.2_diet_score_and_gender_on_diabetes.txt", 
        "insight": "obj_2.2_diet_and_diabetes_by_gender.txt"       
    }
}
obj_2_3_outcomes = {
    "Data-driven Recommendations": {
        "description": "Highlights key findings and practical suggestions to improve public health based on the data.",
        "insight": "obj_2.3_data_driven_recommendation.txt"
    }
}

# Map objectives to outcome dicts
objective_outcomes_map = {
    "Distribution": obj_1_1_outcomes,
    "Associations": obj_1_2_outcomes,
    "Relationships": obj_1_3_outcomes,
    "Interactions": obj_1_4_outcomes,
    "Disparities": obj_2_1_outcomes,
    "Modifiers": obj_2_2_outcomes,
}

# --------- Helper Functions ---------

def render_plots(plots):
    if not plots:
        st.warning("Plot data not found for this outcome.")
        return
    if not isinstance(plots, list):
        plots = [plots]

    for i, plot_file in enumerate(plots, 1):
        plot_path = PLOTS_DIR / plot_file
        if not plot_path.exists():
            st.warning(f"Plot {i} not found: {plot_file}")
            continue

        suffix = plot_path.suffix.lower()
        if suffix == ".png":
            st.image(Image.open(plot_path), caption=f"Plot {i}", use_container_width=True)
        elif suffix == ".html":
            try:
                with open(plot_path, "r", encoding="utf-8") as f:
                    html_content = f.read()
                components.html(html_content, height=600, scrolling=True)
            except Exception as e:
                st.error(f"Error loading HTML plot {i}: {e}")
        else:
            st.warning(f"Unsupported plot file type: {plot_file}")

def render_summaries(summaries):
    if not summaries:
        st.warning("Summary file not specified for this outcome.")
        return
    if not isinstance(summaries, list):
        summaries = [summaries]

    for i, summary_file in enumerate(summaries, 1):
        summary_path = SUMMARY_DIR / summary_file
        st.markdown(f"**Summary {i}: {summary_file}**")
        if not summary_path.exists():
            st.warning(f"Summary file not found: {summary_file}")
            continue

        suffix = summary_path.suffix.lower()
        try:
            if suffix == ".txt":
                with open(summary_path, "r", encoding="utf-8") as f:
                    st.text(f.read())
            elif suffix == ".xlsx":
                xls = pd.ExcelFile(summary_path)
                for sheet in xls.sheet_names:
                    with st.expander(f"Sheet: {sheet} ({summary_file})", expanded=False):
                        df = pd.read_excel(xls, sheet_name=sheet)
                        st.dataframe(df, use_container_width=True)
            elif suffix == ".csv":
                df = pd.read_csv(summary_path)
                st.dataframe(df, use_container_width=True)
            else:
                st.warning(f"Unsupported summary file type: {summary_file}")
        except Exception as e:
            st.error(f"Error loading summary {summary_file}: {e}")

def render_insight(insight_file):
    insight_path = INSIGHT_DIR / insight_file
    if not insight_path.exists():
        st.warning("Insight summary not available.")
        return
    try:
        with open(insight_path, "r", encoding="utf-8") as f:
            content = f.read()
        st.markdown(content)
        st.download_button("Download Insight", content, file_name=insight_file)
    except Exception as e:
        st.error(f"Error reading insight file: {e}")

# --------- Main UI Logic ---------

if objective in objective_outcomes_map:
    outcomes = objective_outcomes_map[objective]
    selected_outcome = st.sidebar.selectbox(f"Select Outcome for {objective}", list(outcomes.keys()))
    data = outcomes.get(selected_outcome, {})
    if not data:
        st.warning("No data available for this outcome.")
        st.stop()

    st.subheader(f"{objective} - {selected_outcome}")

    # Show description if available
    description = data.get("description")
    if description:
        st.markdown(f"**Description:** {description}")


    tab1, tab2, tab3 = st.tabs(["Plots", "Summary Report", "Key Findings"])

    with tab1:
        render_plots(data.get("plot"))

    with tab2:
        render_summaries(data.get("summary"))

    with tab3:
        insight_file = data.get("insight")
        if insight_file:
            render_insight(insight_file)
        else:
            st.warning("Insight file not specified for this outcome.")

elif objective == "Interventions":
    st.markdown("### Objective 2.3: Data-driven Recommendations")
    insight_file = obj_2_3_outcomes["Data-driven Recommendations"]["insight"]
    render_insight(insight_file)

else:
    st.warning("No data available for this objective.")
