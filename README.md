# Analyzing the Impact of Lifestyle, Socioeconomic Status, and Healthcare Access on Chronic Health Conditions Among U.S. Adults

##  NHANES 2021–2023 Data Analysis Project - health_track
---
##  Project Objective

This project looks at how lifestyle habits, socioeconomic status, and access to healthcare affect chronic health conditions in U.S. adults, using data from the 2021–2023 NHANES survey. It focuses on conditions like obesity, high blood pressure, diabetes, and high cholesterol. The main goals are to understand how behaviors like diet, exercise, and sleep relate to these diseases; to see how factors like income, education, and health insurance influence overall health; to explore health differences across gender and racial/ethnic groups; and to help inform smarter, evidence-based public health policies.

---
##  Project Overview

This analysis uses nationally representative NHANES data, combining information from demographics, diet, physical activity, lab results, and questionnaires. I used a mix of traditional statistical methods and exploratory visualizations to explore how different lifestyle and socioeconomic factors relate to health outcomes among U.S. adults.
---
## Features

- I started by importing NHANES data from local .XPT files and converted them to .CSV for easier handling.
- Then, I cleaned and merged all the datasets using Pandas to prepare them for analysis.
- To make sure the findings represent the U.S. population accurately, I used survey-weighted regression models with NHANES sample weights. I ran these models using Python’s statsmodels library—mostly WLS (Weighted Least Squares) and GLM—because they’re more appropriate for survey data than tools like scikit-learn or numpy, which don’t directly handle sample weights.
- For visualizations, I used Seaborn, Matplotlib, and Plotly to bring out key patterns in the data.
- I also created an SQLite database so I could query the cleaned dataset efficiently.
- (Optional) I experimented with machine learning techniques like clustering and regression to explore deeper patterns.
- (Optional) I built a basic Streamlit app to make the visualizations interactive and easier to explore.

---

## Technology Stack
| Component          | Tool / Library                          |
|-------------------|------------------------------------------|
| Programming       | Python (3.13.1)                            |
| Data Handling     | Pandas, NumPy                            |
| Visualization     | Seaborn, Matplotlib, Plotly              |
| Statistical Models| Statsmodels (Model based)                |
| Database          | SQLite                                   |
| Notebooks         | Jupyter                                  |
| Optional ML       | scikit-learn                             |
| Environment       | Virtualenv                               |
| Deployment        | (Optional) Streamlit                     |

---
## Data Source

Data from the **National Health and Nutrition Examination Survey (NHANES)**, a program of studies designed to assess the health and nutritional status of adults and children in the United States.

- [NHANES 2021–2023](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?Cycle=2021-2023)
- Documentation: [NHANES Data Documentation](https://wwwn.cdc.gov/nchs/nhanes/default.aspx)

---
## Data Selection

For this project, I used a smaller, more focused selection of variables from the NHANES 2021–2023 datasets. I only kept the columns that were actually needed to explore things like BMI, lifestyle habits, and chronic disease risk.

From DEMO_L.XPT, I pulled just the basics—demographics, education level, income, and weight.
From BMX_L.XPT, I only used the BMI (BMXBMI) column since that’s all I needed from there.
All the datasets were then joined together using the SEQN ID, which links each participant across files.
You can check the Data Dictionary section below for a full list of the variables I used and what each one means.

---
## NHANES 2021–2023 Data Dictionary with Definitions

### Step 1: lifestyle behaviors (physical activity, sleep duration, diet quality) and socioeconomic indicators (income, education, health insurance coverage)

| Dataset | Variable     | Description                                   | Definition |
|---------|--------------|-----------------------------------------------|------------|
| DEMO_L  | SEQN         | Unique respondent ID                          | Participant’s unique survey identifier |
|         | RIAGENDR     | Gender (1 = Male, 2 = Female)                 | Biological sex reported by participant |
|         | RIDAGEYR     | Age in years                                  | Participant’s age at time of exam |
|         | RIDRETH3     | Race/ethnicity                                | Race/ethnic group categories defined by NHANES |
|         | DMDEDUC2     | Education level                               | Highest education completed (categories) |
|         | INDFMPIR     | Income-to-poverty ratio                       | Ratio of family income to poverty threshold |
|         | WTINT2YR     | Interview sample weight                       | Weight for interview data to represent US population |
|         | WTMEC2YR     | MEC exam sample weight                        | Weight for physical exam and lab data |
|         | SDMVSTRA     | Stratification variable for survey design     | Variable to account for survey design strata |
|         | SDMVPSU      | PSU variable for survey design                | Variable to account for primary sampling units |
| PAQ_L    | PAD680       | Minutes of moderate-intensity work activity/week| Self-reported weekly minutes of moderate physical activity |
|          | PAD790Q      | Frequency of vigorous recreational activity     | How often participant engages in vigorous activities |
|          | PAD790U      | Time unit for PAD790Q                           | Units for PAD790Q (e.g., times per week) |
|          | PAD800       | Duration of vigorous activity                   | Average length of vigorous activity sessions |
| SLQ_L    | SLD012       | Sleep hours on weekdays/workdays               | Self-reported average hours of sleep on workdays |
|          | SLD013       | Sleep hours on weekends                        | Self-reported average hours of sleep on weekends |
| DR1TOT_L | DR1TKCAL     | Total daily energy intake (kcal)               | Calories consumed on dietary recall day 1 |
|          | DR1TSFAT     | Saturated fat intake (g)                       | Grams of saturated fat consumed day 1 |
|          | DR1TSUGR     | Total sugars intake (g)                        | Grams of sugars consumed day 1 |
|          | DR1TFIBE     | Total dietary fiber intake (g)                 | Grams of fiber consumed day 1 |
|          | WTDR2D       | Dietary Day 1 sample weight                    | Weight for dietary recall day 1 data |
| HIQ_L    | HIQ011       | Covered by health insurance                    | Has any health insurance coverage (Yes/No) |
---
### Step 2: Health outcomes (BMI, BP, cholesterol, glucose, chronic disease)

| Dataset  | Variable     | Description                                   | Definition |
|----------|--------------|-----------------------------------------------|------------|
| BMX_L   | BMXBMI       | Body Mass Index (kg/m²)                        |  indicator of body fat |
| BPXO_L   | BPXOSY1-3    | Systolic BP readings 1–3                      | Three systolic blood pressure measurements (mm Hg) |
|          | BPXODI1-3    | Diastolic BP readings 1–3                     | Three diastolic blood pressure measurements (mm Hg) |
| TCHOL_L  | LBXTC        | Total cholesterol (mg/dL)                     | Total blood cholesterol concentration |
| GLU_L    | LBXGLU       | Fasting glucose (mg/dL)                       | Blood glucose concentration after fasting |
|          | LBDGLUSI     | Glucose (SI units)                            | Glucose in SI units (mmol/L) |
|          | WTSAF2YR     | Fasting sample weight                         | Weight for fasting blood sample data |
| DIQ_L    | DIQ010       | Ever been told you have diabetes?             | Self-reported doctor diagnosis of diabetes (Yes/No) |
| MCQ_L    | MCQ160B      | Ever told had congestive heart failure        | Self-reported CHF diagnosis (Yes/No) |
|          | MCQ160C      | Coronary heart disease                        | Self-reported CHD diagnosis (Yes/No) |
|          | MCQ160D      | Angina/angina pectoris                        | Self-reported angina diagnosis (Yes/No) |
|          | MCQ160E      | Heart attack                                  | Self-reported heart attack diagnosis (Yes/No) |

---
###  Step 3: Modeling & Survey Design

| Dataset    | Variable      | Description                                           | Definition |
|------------|---------------|-------------------------------------------------------|------------|
| DEMO_L     | WTINT2YR      | Interview weight (used for questionnaire data)        | Weight to produce nationally representative estimates for interview data |
|            | WTMEC2YR      | MEC exam weight (used for physical/lab data)          | Weight to produce nationally representative estimates for exam data |
|            | SDMVSTRA      | Stratification variable                               | Used to account for survey design strata in analysis |
|            | SDMVPSU       | PSU variable                                          | Primary sampling units to account for clustering in survey design |
| DR1TOT_L   | WTDR2D        | Dietary recall Day 1 weight                           | Weight for Day 1 dietary recall data |
| GLU_L | WTSAF2YR    | Fasting subsample weight                              | Weight for fasting subsample lab data |
---
## Visualizations

- Boxplots and histograms of BMI, glucose, cholesterol
- Grouped bar plots by gender, income, or race
---
##  Example Research Questions

1. How do everyday habits like exercise, what people eat, and how much they sleep affect things like BMI, blood pressure, and blood sugar in adults across the U.S.?
2. Does a person’s income, education, or whether they have health insurance change their chances of having conditions like obesity or diabetes or high blood pressure?
3. Are there differences between men and women when it comes to how lifestyle and money affect their health?
4. How do race and ethnicity influence the connection between lifestyle, access to healthcare, and chronic health problems?
5. Do unhealthy habits together—like not exercising and eating poorly—make health problems worse than just one of those habits alone?
6. Which groups seem to be at the highest risk for chronic diseases, and how can this info help create better health programs?
---
## Why Use Survey Weights?

Since NHANES uses a complex, multistage sampling design, we can’t just analyze the raw numbers like in a simple random sample because that would lead to biased or misleading results. To deal with this, NHANES provides survey weights that we have to use in our analysis. These weights help adjust for a few important things:

- Not everyone has the same chance of being picked

- Some groups, like minorities, are intentionally oversampled

- Some people don’t respond, which could mess with the data

By using these weights properly, our results better represent the whole U.S. population, not just the people who actually took part in the survey.

---
## Project Folder Structure

```
project-root/
│
├── data/
      ├── raw      # Raw NHANES dataset in XPT format (downloaded)
      ├── interim  # NHANES dataset with selected columns in csv format
      ├── clean    # cleaned datas
      ├── processed  # merged and processed data             
├── notebooks/             # Jupyter Notebooks
├── outputs/               # Visualizations and tables
├── requirements.txt       # Python dependencies
├── README.md
├── .env              # Project readme 
├── scripts/          # Data loading and cleaning and analysis scripts
      ├──config.py
      ├──utils.py 
      ├──data_loading.py
      ├──data_cleaning.py
      ├── all individual data cleaning script           
└── docs /                 # related to project documents
```

---
## Setup Instructions

### 1. Clone This Repository

```bash
git clone https://github.com/yourusername/project.git
cd project
```

### 2. Create & Activate Virtual Environment

```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run Jupyter Notebook

```bash
jupyter notebook
```

---

## Requirements

Contents of `requirements.txt`:

```
pandas
numpy
matplotlib
seaborn
plotly
statsmodels
scikit-learn
jupyter
```

> Only the necessary libraries are included to keep things clean and lightweight. A virtual environment was used to avoid any conflicts and keep the setup isolated from the rest of the system.

---
##  Testing & Validation

- All the code runs smoothly in a clean environment without any errors. 
- The notebooks are well-organized, with clear comments explaining each step. 
- Model based weights were applied correctly during analysis to make sure results are nationally representative. 
- I also tested the SQLite database with a few sample SQL queries to make sure everything was working as expected.
---
##  Version Control

- Tracked using the Git command line interface.
- Minimum 10 commits
- No files were uploaded through the GitHub web interface
- The .gitignore file includes the venv folder.

---
## Risk Mitigation

| **Potential Risk**              | **How I Plan to Handle It**      |
|------------------------------------------------------------------------------------------------------------------|
| **Large file sizes**            | If the files are too big to work with easily, I’ll either use a smaller subset of the data or convert them to a lighter format like SQLite. |
| **Missing values**              | I’ll either fill in the missing data (impute) or remove the affected rows, depending on the situation. Whatever I do, I’ll make sure to clearly document the steps in my notebook. |
| **Using weights incorrectly**   | I’ll carefully follow the official NHANES documentation to make sure I’m applying the sample weights properly. |
| **Reproducibility issues**      | I’ll use a virtual environment and include a `requirements.txt` file so that everything can be re-run on another machine without issues. 

---
## Contact

**Sahiladevi Deenadayalu**  
[sahiladevi2003@gmail.com](mailto:sahiladevi2003@gmail.com)