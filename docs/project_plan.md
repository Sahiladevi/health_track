
# Project Plan

## Project Title

**Analyzing the Impact of Lifestyle, Socioeconomic Status, and Healthcare Access on Chronic Health Conditions Among U.S. Adults: Insights from NHANES 2021–2023**

---

## Project Overview

This project looks at how daily habits, income, and access to healthcare affect common health problems in U.S. adults. It uses national data from the 2021–2023 NHANES survey, which includes health interviews, physical exams, and lab results. To better understand what people eat, I also used data from the USDA ARS FPED (Food Patterns Equivalents Database), this helps break down complex food intake into clear diet components, like how many fruits, veggies, or added sugars someone eats. The project focuses on key health issues like obesity, high blood pressure, diabetes, and high cholesterol. The goal is to see how lifestyle factors—like diet, physical activity, and sleep are linked to these conditions. It also looks at how income, education, and health insurance shape health outcomes, and how these patterns differ between men and women, and across racial and ethnic groups. In the end, the hope is to turn these insights into useful ideas for improving public health policies.

---

## Purpose

The purpose of this project is to explore how health conditions—like obesity, high blood pressure, diabetes, and high cholesterol—are influenced by everyday habits, income, education, and access to healthcare. Using the 2021–2023 NHANES survey data, along with detailed diet info from the USDA FPED database, I’m looking at how factors like sleep, physical activity, diet quality, income level, and insurance coverage all connect to health.

By studying these links, I want to uncover patterns and inequalities—especially those that show up differently between men and women or across racial and ethnic groups. The goal is to use these insights to support better, more inclusive public health policies that are grounded in real-world evidence.

---

## Scope 

This project is all about looking at how everyday habits—like what people eat, how much they exercise, and how well they sleep along with things like income, education, and healthcare access, affect health problems in adults across the U.S.

I’m focusing on common issues like obesity, high blood pressure, diabetes, and high cholesterol.

To do this, I used health survey data from NHANES (2021–2023) combined with detailed food data from USDA to get a clearer picture of people’s diets.

The big idea is to find out how these lifestyle and social factors work together to influence health, and also to see how this might be different for men vs. women or among different racial and ethnic groups.

## How I Planned to Analyze the Data

**Getting the Data Ready**

I started by cleaning up all the messy data, putting it in order, and creating new useful info—like scores that show how healthy someone’s diet is, or grouping incomes into categories. Everything is saved nicely so it’s easy to work with.

**Looking at the Basics**

I checked how lifestyle habits and social factors are spread out in the data like who exercises more, who eats healthier, and how income and education look across the group.

**Finding Connections**

Next, I looked at how these habits are linked to health problems. For example, how does exercise or diet relate to obesity or diabetes?

**Checking Differences Between Groups**

I also explored how these connections might be different for men and women or for people from different racial or ethnic backgrounds.

**Running the Right Statistical model**
The data comes from a special kind of survey, so I had to use methods that account for that. Since the usual tools didn’t fully support this, I used a trusted workaround that still gives reliable results by using weights and corrected models.

**Making Sense of It All**

Finally, I pulled together the important findings to help understand what lifestyle or social factors are most important for health. This can help guide better health advice and policies.

---

## Objectives

**Goal 1: See How Lifestyle and Social Factors Affect Health**

- First, I want to understand how things like people’s daily habits (what they eat, how they sleep, how active they are), their income and education, and whether they have health insurance, differ across adults in the U.S.

- Then, I’ll look at how these factors relate to key health measures like body weight (BMI), blood pressure, cholesterol, blood sugar, and common health problems like diabetes, obesity, and high blood pressure.

- I’ll also zoom in on specific connections, for example, how the amount of sleep someone gets might affect their body weight.

- Plus, I want to see how different habits work together, like diet and exercise, to impact health.

**Goal 2: Understand Health Differences by Gender and Race**

- Next, I’ll compare these habits and health results between men and women, and among different racial and ethnic groups.

- I’ll check if being a certain gender or race changes how lifestyle or social factors influence health.

- Finally, I want to use what I find to suggest ways to improve health policies so they better support groups who face the biggest challenges.

---

## Features

- **Cleaned and Combined Data:** Took multiple messy NHANES and USDA FPED files and cleaned them up using Python scripts, making the data easy to understand and work with.

- **Organized Data in Steps:** Saved the data at different stages — raw, interim, clean, and processed, so everything is well-organized and easy to track.

- **Created New Useful Info:** Added new columns like income groups, physical activity levels, and a Healthy Eating Index score to better understand diet quality and lifestyle.

- **Automated Data Processing:** Used a master Jupyter Notebook to run all the cleaning and organizing scripts in the right order, turning raw data into clean, ready-to-use datasets.

- **Stored Data in a Database:** Put the cleaned and processed data into an SQLite database, loading it into their tables by topic (like diet, exercise, health) for easy access.

- **Merged Data for Analysis:** Combined tables into larger datasets, one focusing on lifestyle and social factors, and another with all health info—saved as CSV files for further study.

- **Used Survey Weights:** Applied NHANES survey weights during analysis to make sure the results represent the whole U.S. population, even though the survey design is complex.

- **Handled Complex Survey Challenges:** Since some Python tools don’t fully support NHANES’s survey design, used trusted workarounds like Weighted Least Squares and Generalized Linear Models with HC3 correction to get reliable results.

- **Analyzed Data with Multiple Notebooks:** Ran focused analyses using different Jupyter Notebooks, looking at lifestyle habits, health outcomes, and differences across gender and race.

---

## Technologies

| What I Used         | Tools / Programs             | How I Used It                                                     |
| ------------------- | ---------------------------- | ----------------------------------------------------------------- |
| Programming         | Python (version 3.13.1)      | I wrote all the code for the project using Python.                |
| Handling Data       | Pandas, NumPy                | I used these to organize and work with the data.                  |
| Making Graphs       | Seaborn, Matplotlib, Plotly  | I created charts and graphs to help explain my results.           |
| Statistics          | Statsmodels (for regression) | I analyzed data patterns and relationships with this.             |
| Storing Data        | SQLite                       | I saved and managed the data using this database.                 |
| Writing and Sharing | Jupyter Notebooks            | I combined my code and notes in one interactive file.             |
| Project Setup       | Virtualenv                   | I kept all the project’s tools and packages separate from others. |

---

## Architecture Overview

1. **Set Up Environment**  
   
   Start by creating a virtual Python environment and installing all required libraries from `requirements.txt`. This ensures everything runs smoothly and stays consistent.

2. **Getting the Raw Data**  

   Download raw datasets from official government websites.

   - NHANES (2021–2023): A big national health survey with data on diet, exercise, sleep, medical conditions, etc.

   - USDA FPED: A dataset that breaks down the types of foods people ate.

   Save all files in a structured folder: data/raw.

3. **Data Cleaning and Organization**  
   
   Write Python scripts to:

   - Clean and prepare each dataset (e.g., diet, sleep, exercise, etc.).

   - Fix missing or messy entries.

   - Standardize columns and formats.

   - Calculate a Healthy Eating Index (HEI) score.

   - Engineer new features (e.g., group income levels, categorize physical activity).

   Organize this cleaned data into:

   - data/interim for lightly cleaned files

   - data/clean for cleaned individual datasets

   - data/processed for fully prepared datasets with features

   Use a central notebook (data_ingestion_and_cleaning.ipynb) to run all scripts in the correct order.

4. **Save into a Database**

   Use an SQLite database to store all processed data in separate tables (diet, exercise, etc.).

   Create two combined datasets:

   - One for lifestyle + social factors

   - One full dataset for complete analysis

   Export final files into data/final as .csv files.

5. **Data Analysis Plan**

   Use Jupyter Notebooks to analyze the processed data. Key goals:

   - Understand distribution of lifestyle and social factors.

   - Find how these factors relate to health outcomes.

   - Explore how different groups (e.g., gender, race) compare.

   - Create simple, data-backed health insights.

6. **Handling Survey Design**

   Use NHANES-provided survey weights to make results representative of the U.S. population.

   Since full complex survey methods have limitations in Python:

   - Use Weighted Least Squares (WLS) and Generalized Linear Models (GLM) with HC3 correction to produce reliable estimates.

---

7. **Files and Scripts to Build**

| No. | File Name                       | Purpose                                |
| --- | ------------------------------- | -------------------------------------- |
| 1   | `config.py`                     | Set up paths and selected columns      |
| 2   | `utils.py`                      | Reusable helper functions              |
| 3   | `db_utils.py`                   | Functions for SQLite database          |
| 4   | `data_loading.py`               | Load and save raw NHANES data          |
| 5   | `data_cleaning.py`              | Control script to run all cleaning     |
| 6   | `clean_demo.py`                 | Clean demographics data                |
| 7   | `clean_clinical_exam.py`        | Clean clinical/lab data                |
| 8   | `clean_sleep.py`                | Clean sleep questionnaire data         |
| 9   | `clean_diet.py`                 | Clean diet intake data                 |
| 10  | `clean_fped.py`                 | Clean USDA FPED data                   |
| 11  | `calculating_usda_hei_score.py` | Calculate HEI diet quality score       |
| 12  | `clean_physical.py`             | Clean physical activity data           |
| 13  | `clean_healthcare_access.py`    | Clean insurance/healthcare access data |
| 14  | `clean_chronic_disease.py`      | Clean chronic disease files            |
| 15  | `feature_engineering.py`        | Create grouped/categorized variables   |

---

8. **Final Deliverables**

   Clean and well-structured datasets (.csv and SQLite)

   Insightful analysis notebooks

   Clear findings about how lifestyle and social factors affect health

   Practical data based health suggestions

---
## Project Timeline (10 Weeks)

| Week | What’s Happening                                                                                                     |
| ---- | -------------------------------------------------------------------------------------------------------------------- |
| 1    | Project kickoff: define key health questions, set up the project repo, folder structure, and development environment |
| 2    | Download all required NHANES and USDA FPED data; organize raw files and begin exploratory checks                     |
| 3    | Write and run scripts to clean and standardize individual datasets (e.g., demographics, diet, sleep, exercise)       |
| 4    | Merge and clean food data; calculate Healthy Eating Index (HEI); save outputs to structured folders                  |
| 5    | Create new features (e.g., grouped income, activity levels); finalize cleaned and processed datasets                 |
| 6    | Load processed data into SQLite; build final combined datasets for analysis (lifestyle-only and full health)         |
| 7    | Perform statistical analysis: run WLS and GLM regressions with HC3 correction; examine lifestyle-health links        |
| 8    | Continue analysis: assess interaction effects, compare gender/race groups, and develop simplified health insights    |
| 9    | Build an interactive dashboard and visualizations; finalize all Jupyter notebooks and summary materials (Optional)             |
| 10   | Share results, gather feedback, polish final outputs (report, code, data), and wrap up the project                   |

---

## Risks and Mitigation Strategies

1. **Data Quality and Completeness**

   Risk: The health and food data from NHANES and USDA FPED could have missing or inconsistent entries, which might affect the accuracy of the analysis.
   Mitigation: I carefully cleaned the data using custom Python scripts to fix missing values, correct errors, and standardize the format. This helped make the data more reliable and easier to work with.

2. **Complex Survey Design Limitations**

   Risk: NHANES uses a complex survey design with weights and strata to represent the U.S. population, but the analysis tools in Python don’t fully support this complexity, which could lead to biased or incorrect results.
   Mitigation: I applied the survey weights to adjust for population representation and used Weighted Least Squares (WLS) and Generalized Linear Models (GLM) with robust correction methods. This is a widely accepted approach when full complex design modeling isn’t possible, ensuring the results remain trustworthy.

3. **Data Integration Challenges**

   Risk: Combining multiple datasets from different sources and formats can cause mismatches or loss of information.
   Mitigation: I organized the data step-by-step, saving intermediate cleaned and processed versions in clearly labeled folders. This made it easier to track changes and ensured smooth merging of datasets into a final, unified format.

4. **Script Errors or Workflow Breakdowns**

   Risk: Running multiple scripts and notebooks increases the chance of errors or disruptions in the workflow.
   Mitigation: I designed the data processing to be modular, with each script doing one specific job. I also used a master Jupyter Notebook to run scripts in the right order, helping catch issues early and keeping the process organized.

5. **Overfitting or Misinterpretation in Analysis**

   Risk: Drawing incorrect conclusions from the data because of overlapping variables or statistical challenges.
   Mitigation: I carefully checked for multicollinearity and used robust statistical methods to avoid confusing overlapping effects. I also focused on interpreting results within the context of the data and methods used, highlighting limitations openly.

6. **Data Security and Privacy**

   Risk: Handling sensitive health data could raise privacy concerns.
   Mitigation: I only used publicly available, anonymized government datasets and kept all data securely stored locally. No personal identifiers were used or shared at any point.

---

## Test and Evaluation Plan

1. **Check the Data**

   Make sure the data doesn’t have missing or weird values. I’ll look for blanks, errors, or strange numbers to be sure the data is good to use.

2. **Test the Scripts**

   Run each cleaning and processing script one by one to see if they do what they’re supposed to do. I’ll check the results to make sure everything is working right.

3. **Check Data Merging**

   After combining different data files, I’ll double-check that nothing got lost or mixed up. I’ll compare before and after merging to be sure all info is still correct.

4. **Validate the Analysis**

   I’ll look at the statistical models and results carefully, making sure they make sense and follow the right methods. If something looks off, I’ll review and fix it.

5. **Review Final Results**
   Look over the final cleaned data and scores to confirm they are clear, accurate, and useful.

6. **Repeat the Process**

   Run the whole process again from start to finish to make sure it works smoothly every time, so others can do it too.

---
## Contact 

- **Main Contact:** Sahiladevi Deenadayalu — [sahiladevi2003@gmail.com](mailto:sahiladevi2003@gmail.com) 

- **Repository:** [https://github.com/Sahiladevi/health_track](https://github.com/Sahiladevi/health_track)

---

*End of Project Plan*
