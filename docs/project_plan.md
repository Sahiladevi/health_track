
# Project Plan

## Project Title

**Analyzing the Impact of Lifestyle, Socioeconomic Status, and Healthcare Access on Chronic Health Conditions Among U.S. Adults: Insights from NHANES 2021–2023**

---

## Project Overview
- This project looks at how everyday habits, income and education levels, and access to healthcare relate to chronic health issues like diabetes, high blood pressure, and obesity among adults in the U.S. I’ll be using the most recent data from the NHANES 2021–2023 survey, which is designed to represent the U.S. population.

- Specifically, I’ll explore how things like physical activity, sleep, and diet — along with factors like income, insurance coverage, and medication use — are linked to health indicators such as BMI, blood pressure, cholesterol, and chronic disease status. I’ll also look at whether these relationships differ based on gender or race/ethnicity.

- The goal is to better understand which groups are most at risk and what social or behavioral factors might be driving those risks — ultimately helping to guide strategies that promote health equity and reduce health disparities.

---

## Purpose
- The purpose of this project is to dig into how health outcomes — like obesity, high blood pressure, and diabetes — are shaped by a mix of lifestyle choices, socioeconomic background, and access to healthcare. I’ll use data from NHANES (2021–2023) to examine these links and look at how things like sleep duration, physical activity, diet quality, education, income, and insurance status interact.

- By analyzing this data, I hope to identify patterns and disparities — especially those that affect specific groups by gender or race/ethnicity — and use that insight to help inform public health policies that are both inclusive and effective.

---

## Scope and Analysis Plan
I’ll be combining several NHANES datasets, including information on demographics, socioeconomic status, lifestyle habits, healthcare access, and clinical health measurements.

The main variables I’ll focus on are things like age, gender, race and ethnicity, education, income compared to poverty level, physical activity, sleep, diet, health insurance, medication use, and key health indicators such as BMI, blood pressure, cholesterol, blood sugar, and chronic disease status.

For the analysis, I’ll use survey-weighted regression models to account for the survey design and look for interactions between variables to understand how different factors influence health together.

I’ll also explore how combinations of behaviors—like diet and exercise—affect health outcomes.

All the data processing, modeling, and visualizations will be done using Python, with tools like SQLite for managing the data and libraries for statistics and plotting.


---

## Objectives

### Goal 1: Understand how lifestyle and social factors affect health
- Describe how lifestyle habits, socioeconomic status, and insurance coverage vary among U.S. adults.

- Measure how these factors relate to BMI, blood pressure, cholesterol, blood sugar, and chronic diseases like diabetes, obesity and hypertension.

- Look closely at specific links—for example, how sleep duration influences BMI.

- Examine how diet and physical activity together impact health outcomes.

### Goal 2: Highlight health disparities by gender and race/ethnicity
- Compare health behaviors and outcomes across different gender and racial/ethnic groups.

- Check whether gender or race/ethnicity changes how lifestyle or socioeconomic factors affect health.

- Use these insights to suggest focused public health strategies that address these disparities.

---

## Features

### Core
- Cleaned and merged multiple NHANES datasets using Python and Pandas

- Saved the processed data in an SQLite database for easy querying and reuse

- Explored the data through descriptive statistics and visualizations to find initial patterns

- Ran survey-weighted regression models to account for NHANES’s complex sampling design

- Investigated interactions between variables to understand how different factors influence each other

= Analyzed how lifestyle behaviors, taken together, relate to chronic health conditions

### Stretch
- Experimented with machine learning models to identify more complex patterns

- Built interactive dashboards using Plotly Dash and/or Streamlit to share insights

- Ran basic simulations to explore how policy changes might impact population health

---

## Technologies
- Python, Pandas, SQLite, Jupyter Notebook

- Matplotlib, Seaborn, Plotly for data visualization

- Statsmodels for survey-weighted analysis

- Scikit-learn for optional machine learning tasks

- Streamlit or Plotly Dash for interactive dashboards

- VS Code for development, GitHub for version control

---

## Architecture Overview

1. **Set Up Environment**  
   Create a virtual Python environment and install dependencies using `requirements.txt`

2. **Get the Data**  
   Download NHANES files, load them, and set up an SQLite database to store the data

3. **Clean and Prepare**  
   Tidy up the data, normalize formats, engineer useful features, and merge datasets

4. **Explore the Data**  
   Use summary statistics and visualizations to identify patterns and trends  
   Apply survey-weighted estimates where appropriate

5. **Build Models**  
   Run survey-weighted regression models, including interaction terms

6. **Go Deeper** *(Optional)*  
   Apply machine learning models to uncover more complex relationships

7. **Build a Dashboard**  
   Create interactive charts and filters to help users explore the findings

8. **Share Results**  
   Provide clear, well-documented notebooks  
   Optionally deploy the dashboard for public or stakeholder access

9. **Refine with Feedback**  
   Gather input from stakeholders and make iterative improvements

---

## Project Timeline (10 Weeks)

## Project Timeline

| Week | What’s Happening                                       |
|------|--------------------------------------------------------|
| 1    | Kick things off: set up the project, outline key questions, and create the repo and environment |
| 2    | Download the NHANES data and build the initial database structure |
| 3    | Clean up the data, combine datasets, and apply survey weights |
| 4    | Start creating features, write reusable code, and begin exploring the data |
| 5    | Dig deeper into the data and create visual summaries    |
| 6    | Run regression models with survey weights and look at interaction effects |
| 7    | *(Optional)* Try out machine learning models if time allows |
| 8    | Build an interactive dashboard to present the findings  |
| 9    | Pull everything together—finalize notebooks and prep the report |
| 10   | Share with others, collect feedback, make any final edits, and wrap it up |

---

## Risks and Mitigation Strategies

| **Potential Issue**             | **What I'm Doing About It**                                             |
|---------------------------------|--------------------------------------------------------------------------|
| Missing or incomplete data      | I'm checking the data early on and filling in missing parts when I can. Also doing sensitivity checks to see how it affects results. |
| Survey data is complicated      | I'm following NHANES guidelines and applying survey weights properly.   |
| Too much data or hard to merge  | Using participant IDs to link datasets and only keeping the important columns. |
| Privacy and ethics              | Being careful with how I talk about the data and keeping equity in mind. |
| Dashboard might lag             | Keeping the data lightweight and using filters or pagination to speed things up. |
| Not an expert in health topics  | Reading NHANES documentation and referring to trusted sources when needed. |
| Not sure what others expect     | Trying to define who the project is for early on and getting feedback along the way. |
| Time might be tight             | Focusing on the most important parts first, and treating things like ML as optional. |


---

## Test and Evaluation Plan

- **Checking the Data** – Making sure there aren’t any missing values, everything's the right data type, merges went well, and survey weights and new variables make sense.

- **Looking at the Plots** – Using visualizations to spot any weird patterns or outliers that don’t quite fit.

- **Testing the Stats** – Running diagnostics on regression models and checking how well things are working using validation and performance metrics.

- **Testing the Dashboard** – Making sure everything works as expected, checking the backend data, and seeing if it’s easy to use.

- **Getting Feedback** – Having classmates, mentors, or stakeholders take a look and give input on what could be improved.

- **Making It Better** – Keeping track of feedback, updating things as needed, and using version control so everything stays organized.


---
## Contact & Collaboration

- **Repository:** [https://github.com/Sahiladevi/health_track](https://github.com/Sahiladevi/health_track)  
- **Main Contact:** Sahiladevi Deenadayalu — [sahiladevi2003@gmail.com](mailto:sahiladevi2003@gmail.com)  
- **Collaboration:** Regular sync meetings and tracking issues on GitHub  

---

*End of Project Plan*
