# Analyzing the Impact of Lifestyle, Socioeconomic Status, and Healthcare Access on Chronic Health Conditions Among U.S. Adults

## NHANES 2021–2023 Data Analysis Project - health_track

---

## Project Objective

This project looks at how daily habits, income, and access to healthcare affect common health problems in U.S. adults. It uses national data from the 2021–2023 NHANES survey, which includes health interviews, physical exams, and lab results. To better understand what people eat, I also used data from the USDA ARS FPED (Food Patterns Equivalents Database), this helps break down complex food intake into clear diet components, like how many fruits, veggies, or added sugars someone eats. The project focuses on key health issues like obesity, high blood pressure, diabetes, and high cholesterol. The goal is to see how lifestyle factors like diet, physical activity, and sleep are linked to these conditions. It also looks at how income, education, and health insurance shape health outcomes, and how these patterns differ between men and women, and across racial and ethnic groups. In the end, the hope is to turn these insights into useful ideas for improving public health policies.

---

## Data Selection

For this project, I used a smaller, more focused selection of variables from the NHANES 2021–2023 datasets. I only kept the columns that were actually needed to explore things like BMI, lifestyle habits, and chronic disease risk and FPED datas from USDA ARS.

- From DEMO_L.XPT, I pulled just the basics—demographics, education level, income (poverty to income ratio), and weight.
- From BMX_L.XPT, I only used the BMI (BMXBMI) column since that’s all I needed from there.
- From FPED_1720.xls, I pulled the required nutrient food columns required to calculate HEI score (Healthy Eating Index score.)

All the datasets were then joined together using the SEQN ID, which links each participant across files.  

You can check the Data Dictionary section below for a full list of the variables I used and what each one means.

---

## NHANES 2021–2023 Data Dictionary with Definitions

### Lifestyle behaviors (physical activity, sleep duration, diet quality) and socioeconomic indicators (income, education, health insurance coverage)

| Dataset  | Variable  | Description                                | Definition                               |
|----------|-----------|--------------------------------------------|----------------------------------------|
| DEMO_L   | SEQN      | Unique respondent ID                       | Participant’s unique survey identifier |
|          | RIAGENDR  | Gender (1 = Male, 2 = Female)              | Biological sex reported by participant |
|          | RIDAGEYR  | Age in years                               | Participant’s age at time of exam      |
|          | RIDRETH3  | Race/ethnicity                             | Race/ethnic group categories defined by NHANES |
|          | DMDEDUC2  | Education level                            | Highest education completed (categories) |
|          | INDFMPIR  | Income-to-poverty ratio                    | Ratio of family income to poverty threshold |
| PAQ_L    | PAD680    | Moderate-intensity work activity (min/week) | Weekly minutes of moderate activity    |
|          | PAD790Q   | Frequency of vigorous activity            | How often participant does vigorous activities |
|          | PAD790U   | Unit of PAD790Q                           | Time unit for frequency (e.g., times/week) |
|          | PAD800    | Duration of vigorous activity             | Average time per session (minutes)     |
| SLQ_L    | SLD012    | Weekday sleep duration                     | Average weekday/workday sleep in hours |
|          | SLD013    | Weekend sleep duration                     | Average weekend sleep in hours         |
| DR1TOT_L | DR1TKCAL  | Total energy intake (kcal)                 | Total kilocalories consumed on recall day 1 |
|          | DR1TSFAT  | Saturated fat intake (g)                   | Grams of saturated fat consumed        |
|          | DR1TSODI  | Sodium intake (mg)                         | Milligrams of sodium consumed           |
|          | WTDRD1    | Dietary sample weight                      | Weight for Day 1 dietary recall data    |
| DR1IFF_L | DR1IGRMS  | Food gram weight                           | Grams of individual food item consumed |
|          | DR1IKCAL  | Energy from individual food (kcal)        | Calories from each food item            |
|          | DR1IFDCD  | USDA food code                             | Food description code                   |
| HIQ_L    | HIQ011    | Health insurance status                    | Covered by any health insurance (Yes/No) |

---

### Health outcomes (BMI, BP, cholesterol, glucose, chronic disease)

| Dataset  | Variable     | Description                                   | Definition |
|----------|--------------|-----------------------------------------------|------------|
| BMX_L    | BMXBMI       | Body Mass Index (kg/m²)                       | Indicator of body fat |
| BPXO_L   | BPXOSY1-3    | Systolic BP readings 1–3                      | Three systolic blood pressure measurements |
|          | BPXODI1-3    | Diastolic BP readings 1–3                     | Three diastolic blood pressure measurements |
| TCHOL_L  | LBXTC        | Total cholesterol                             | Total blood cholesterol concentration |
| GLU_L    | LBXGLU       | Fasting glucose                              | Blood glucose concentration after fasting |
|          | LBDGLUSI     | Glucose (SI units)                            | Glucose in SI units |
|          | WTSAF2YR     | Fasting sample weight                         | Weight for fasting blood sample data |
| DIQ_L    | DIQ010       | Ever been told you have diabetes?             | Self-reported doctor diagnosis of diabetes (Yes/No) |
| MCQ_L    | MCQ160B      | Ever told had congestive heart failure        | Self-reported CHF diagnosis (Yes/No) |
|          | MCQ160C      | Coronary heart disease                        | Self-reported CHD diagnosis (Yes/No) |
|          | MCQ160D      | Angina/angina pectoris                        | Self-reported angina diagnosis (Yes/No) |
|          | MCQ160E      | Heart attack                                  | Self-reported heart attack diagnosis (Yes/No) |

---

### Modeling & Survey Design

| Dataset  | Variable   | Description                               | Definition                               |
|----------|------------|-------------------------------------------|----------------------------------------|
| DEMO_L   | WTINT2YR   | Interview weight (used for questionnaire data) | Weight to produce nationally representative estimates for interview data |
|          | WTMEC2YR   | MEC exam weight (used for physical/lab data) | Weight to produce nationally representative estimates for exam data |
|          | SDMVSTRA   | Stratification variable                  | Used to account for survey design strata in analysis |
|          | SDMVPSU    | PSU variable                            | Primary sampling units to account for clustering in survey design |
| DR1TOT_L | WTDRD1     | Dietary recall Day 1 weight              | Weight for Day 1 dietary recall data   |
| DR1IFF_L | WTDRD1     | Dietary sample weight                    | Weight for Day 1 dietary recall data    |
| GLU_L    | WTSAF2YR   | Fasting subsample weight                 | Weight for fasting subsample lab data  |
| TCHOL_L  | WTPH2YR    | Phlebotomy 2 Year Weight                 | weight for blood drawn sample data |

---

### FPED Food Patterns Data

| Dataset     | Variable           | Description                                   | Definition |
|-------------|--------------------|-----------------------------------------------|------------|
| FPED_1720   | FOODCODE           | USDA Food Code                                | Unique food item identifier |
|             | DESCRIPTION        | Food name                                     | Text description of the food |
|             | F_TOTAL            | Total fruits (cup eq)                         | All fruit servings including juice |
|             | F_JUICE            | Fruit juice (cup eq)                          | 100% fruit juice servings |
|             | F_CITMLB           | Citrus, melon, berries (cup eq)               | Citrus fruits, melons, and berries only |
|             | F_OTHER            | Other fruits (cup eq)                         | Fruits not in citrus/melon/berry group |
|             | V_TOTAL            | Total vegetables (cup eq)                     | All vegetable servings |
|             | V_DRKGR            | Dark green vegetables (cup eq)                | Spinach, kale, broccoli, etc. |
|             | V_LEGUMES          | Legumes (cup eq)                              | Beans and peas counted as vegetables |
|             | G_WHOLE            | Whole grains (oz eq)                          | Ounces of whole grain intake |
|             | G_REFINED          | Refined grains (oz eq)                        | Ounces of refined grain intake |
|             | D_TOTAL            | Total dairy (cup eq)                          | Milk, cheese, yogurt, etc. |
|             | D_MILK             | Milk (cup eq)                                 | Fluid milk and milk-based drinks |
|             | D_YOGURT           | Yogurt (cup eq)                               | Yogurt servings |
|             | D_CHEESE           | Cheese (cup eq)                               | Cheese and cheese-containing foods |
|             | PF_TOTAL           | Total protein foods (oz eq)                   | Meat, poultry, seafood, nuts, seeds, soy |
|             | PF_MPS_TOTAL       | Meat, poultry, seafood total (oz eq)          | All animal-based protein foods |
|             | PF_SEAFD_HI        | High omega-3 seafood (oz eq)                  | Salmon, mackerel, trout, etc. |
|             | PF_SEAFD_LOW       | Low omega-3 seafood (oz eq)                   | Shrimp, tilapia, cod, etc. |
|             | SOLID_FATS         | Solid fats (g)                                | Butter, lard, beef fat, etc. |
|             | ADD_SUGARS         | Added sugars (tsp eq)                         | Table sugar, syrups, sweeteners |
|             | OILS               | Oils (g)                                      | Plant oils, fish oils, and soft fats |

---

## Data Summary

### What is this data about?

It looks at how people live and their health. It includes:

- **Lifestyle habits:** How much they exercise, sleep, and what they eat.
- **Background:** Their age, gender, race, education, income, and if they have health insurance.
- **Health:** Their weight, blood pressure, cholesterol, blood sugar, and if they have diseases like diabetes or heart problems.

### Why is this important?

To see how lifestyle and money affect health.

To understand who might be at risk for health problems.

To help make better health policies for everyone.

### How was the data collected?

People answered questions about their habits and health.

Their food intake and body measurements were recorded.

The survey is designed to fairly represent all people in the U.S.

---

## Data Source

### 1. [NHANES (2021–2023)](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?Cycle=2021-2023)

The **National Health and Nutrition Examination Survey (NHANES)**, a program of studies designed to assess the health and nutritional status of adults and children in the United States.
[NHANES Documentation](https://wwwn.cdc.gov/nchs/nhanes/default.aspx)

### 2. [USDA ARS FPED](https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/food-surveys-research-group/docs/fped-databases/)

The **USDA Agricultural Research Service (ARS) - Food Patterns Equivalents Database (FPED)** converts reported food and beverage intake into 37 standardized USDA Food Pattern components.  
[FPED Documentation](https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/food-surveys-research-group/docs/fped-overview/)

---
## Setup Instructions

### 1. Clone This Repository

```bash
git clone https://github.com/Sahiladevi/health_track.git
```

### 2. Navigate to the cloned directory

Change your current directory to the cloned repository's directory (health_track)

```bash
cd health_track
```

### 3. Create Virtual Environment

On Windows:
```bash
python -m venv venv
```

On macOS and Linux:
```bash
python3 -m venv venv
```

This will create a new virtual environment named venv in your current directory

### 4. Activate Virtual Environment

On Windows:
```bash
venv\Scripts\activate
```
On macOS and Linux:
```bash
source venv/bin/activate
```
Your prompt should change to indicate that you are now operating within a Python virtual environment.

### 5. Install Requirements

Install the required packages by running the following command:

```bash
pip install -r requirements.txt
```
**Note:** Make sure ipykernel is included in the requirements.txt file. If not, install it manually:

```bash
pip install ipykernel
```
### 6. Register the Environment as a Jupyter Kernel

```bash
python -m ipykernel install --user --name=venv --display-name "Python (health_track)"
```
This step lets you select this environment inside Jupyter.

### 7. Run Jupyter Notebook

```bash
jupyter notebook
```

### 8. To deactivate the virtual environment, after running the project

```bash
deactivate
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
pyreadstat
python-dotenv
squarify
xlsxwriter
openpyxl
xlrd
pywin32==310; sys_platform == "win32"
pywinpty==2.0.15; sys_platform == "win32"

```

> Only the necessary libraries are included to keep things clean and lightweight. A virtual environment was used to avoid any conflicts and keep the setup isolated from the rest of the system. Windows-specific packages like pywin32 and pywinpty were added using platform markers (e.g., sys_platform == "win32") so they are only installed on Windows systems during local development. These are automatically skipped during deployment on Streamlit Cloud (which runs on Linux).

---
## Project Overview: What This Project Does

This project explores how different lifestyle habits like diet, sleep, exercise—and social factors—like income and education are connected to people's health across the U.S.

I used national health data collected by two government groups:

- NHANES: A big health survey that asks people across the country questions and runs lab tests.

- USDA ARS FPED: A dataset that helps explain what types of foods people ate.

The goal? To see how things like socio-economic factors and lifestyle affect health outcomes, and to turn messy, raw data into clean, meaningful insights.

### What I Did

#### 1. Getting the Data

I downloaded all the data files I needed from official websites:

- Health survey data (from 2021–2023) from [NHANES](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?Cycle=2021-2023)

- Food data from [USDA FPED](https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/food-surveys-research-group/docs/fped-databases/)

I saved everything neatly in a folder called data/raw.

#### 2. Cleaning and Organizing the Data

The data was messy and spread across many files. So, I wrote 15 small Python scripts, each doing a specific job:

- Some scripts cleaned different types of data (like diet, sleep, exercise, etc.)

- One script calculated a Healthy Eating Index (HEI) score to see how healthy someone’s diet is.

- Another script created new useful information from existing data—like turning income into categories or grouping exercise levels.

**Here’s a simple example of what these scripts did:**

- Turn messy food entries into clear diet scores.

- Fix missing or inconsistent entries.

- Organize everything so it’s easier to work with later.

#### 3. Running the Scripts for data loading, cleaning and wrangling

To bring it all together, I used a Jupyter Notebook called data_ingestion_and_cleaning.ipynb. Think of this notebook as the “master controller”, it runs all the scripts in the correct order:

- Loads all the raw datasets with the required fields and save it in a folder "data/interim".

- Cleans each dataset (e.g., diet, exercise, sleep, etc.) and save it in a folder "data/clean".

- I added new columns to these clean datasets like grouped income levels, physical activity categories, and other meaningful metrics. This gave me the processed data (to make the data more useful) and save it in a folder "data/processed".

- I also merged a few of the food and diet-related files and used them to calculate a **Healthy Eating Index (HEI)** score, which gives insight into how balanced a person’s diet is. That final score was saved too for further analysis and saved this data in a folder "data/processed".

In short, the notebook automates the full journey from messy raw data to clean, structured, and ready-to-use health information.  

At the end, I had clean, structured data that’s ready for Merging.


#### 4. Saving Processed Data in a Database - Using data_loading_database.ipynb notebook

I saved the processed data into an SQLite database, where each part (diet, exercise, health, lifestyle, etc.) is stored as its own table.

To make analysis easier, I also combined the relevant tables into two larger datasets:

- One with lifestyle and social information

- One with everything together (a full health dataset)

These final combined datasets were then saved as .csv files in the data/final folder, ready to be used for analysis and modeling.

For your reference, I am adding those python scripts detail below:
 | No. | File                             | Description                                                                                             |
|-----|----------------------------------|---------------------------------------------------------------------------------------------------------|
| 1   | `config.py`                      | Establishes file system paths for data stages (raw, interim, clean, processed); maps datasets to paths and selected columns. |
| 2   | `utils.py`                       | Common utility functions (e.g., `explore_data`, path formatting, data validation, cleaning helpers).   |
| 3   | `db_utils.py`                    | Database utility functions (e.g., creating database, running queries, creating tables, closing connections). |
| 4   | `data_loading.py`                | Loads, validates, and saves raw NHANES datasets to interim format.                                     |
| 5   | `data_cleaning.py`              | Central hub to apply cleaning functions to each dataset; imports all individual cleaning modules.      |
| 6   | `clean_demo.py`                  | Cleans `DEMO_L` dataset (Demographics file).                                                           |
| 7   | `clean_clinical_exam.py`         | Cleans `BMX_L`, `BPXO_L`, `TCHOL_L`, and `GLU_L` datasets (Clinical exam and laboratory files).         |
| 8   | `clean_sleep.py`                 | Cleans `SLQ_L` dataset (Sleep questionnaire file).                                                     |
| 9   | `clean_diet.py`                  | Cleans `DR1TOT_L` and `DR1IFF_L` datasets (Dietary questionnaire files).                               |
| 10  | `clean_fped.py`                  | Cleans `FPED_1720.xls` file (Food Patterns Equivalents file).                                          |
| 11  | `calculating_usda_hei_score.py` | Cleans and computes USDA Healthy Eating Index (HEI) score.                                             |
| 12  | `clean_physical.py`             | Cleans `PAQ_L` dataset (Physical activity questionnaire file).                                         |
| 13  | `clean_healthcare_access.py`    | Cleans `HIQ_L` dataset (Insurance and healthcare access questionnaire file).                           |
| 14  | `clean_chronic_disease.py`      | Cleans `DIQ_L` and `MCQ_L` datasets (Diabetes and medical condition files).                            |
| 15  | `feature_engineering.py`        | Creates new features or categorizes variables from NHANES health survey data.                          |

#### 5. Analyzing the Data

I used six Jupyter Notebooks for different analysis goals. Each one looked at a specific question:

| Notebook Name            | What It Did                                                          |
| ------------------------ | -------------------------------------------------------------------- |
| `obj_1.1_analysis.ipynb` | Looked at how lifestyle and social habits are spread across the data |
| `obj_1.2_analysis.ipynb` | Measured how these habits are linked to health outcomes              |
| `obj_1.3_analysis.ipynb` | Explored specific connections between lifestyle factors and health   |
| `obj_1.4_analysis.ipynb` | Studied how different factors work together to affect outcomes       |
| `obj_2.1_analysis.ipynb` | Compared things like gender and race                                 |
| `obj_2.2_analysis.ipynb` | Checked if gender/race changes how lifestyle affects health          |
| `obj_2.3_analysis.ipynb` | Created simple health advice based on the data                       |

#### 6. Survey Design Wasn’t Working—Here’s the Fix I Used

The NHANES health data is collected using something called a complex survey design. That just means the people who took the survey weren’t picked totally at random - some groups, like older adults or specific communities, were intentionally included more often. Plus, not everyone answered every question.

To make sure the results still represent the entire U.S. population, NHANES gives us special weights to apply during analysis.

Now, here’s where things got tricky.

The tools I used in Python mainly the statsmodels library don’t fully support this kind of complex design. The PSU values (which help group people by area) only had two options in the dataset, which isn’t enough to use properly. And when I tried including the strata (which split people into subgroups), the model threw multicollinearity errors basically, the variables were overlapping too much and confusing the analysis.

So I had to make a call.

I still used the survey weights to make sure my results reflect the U.S. population. But instead of using the full complex design, I used a more practical approach that’s commonly accepted when you hit these kinds of limits.

I ran my regressions using either Weighted Least Squares (WLS) with a solid correction method called HC3, or GLM (Generalized Linear Models) with HC3. This correction helps handle variance issues and keeps the estimates reliable.

It’s not a perfect substitute for full survey methods, but it’s a strong and trustworthy workaround and it allowed me to still draw meaningful insights from the data without running into errors.

---

## Technology Stack

| What I Used              | Tools / Programs             | How I Used It                                                     |
|--------------------------|------------------------------|-------------------------------------------------------------------|
| Programming              | Python (version 3.13.1)      | I wrote all the code for the project using Python.                |
| Handling Data            | Pandas, NumPy                | I used these to organize and work with the data.                  |
| Making Graphs            | Seaborn, Matplotlib, Plotly  | I created charts and graphs to help explain my results.           |
| Statistics               | Statsmodels (for regression) | I analyzed data patterns and relationships with this.             |
| Storing Data             | SQLite                       | I saved and managed the data using this database.                 |
| Writing and Sharing      | Jupyter Notebooks            | I combined my code and notes in one interactive file.             |
| Project Setup            | Virtualenv                   | I kept all the project’s tools and packages separate from others. |
| Version Control & Hosting| GitHub                       | I tracked changes, collaborated, and shared the full project online. |

---

## Project Folder Structure

```
health_track/
│
├── dashboard/             # for interactactive web app
│   ├── insights/          # Key findings summary
│   ├── health_track_app.py # Streamlit python script
|            
├── data/
│   ├── raw/               # Raw NHANES dataset in XPT format (downloaded) and Raw USDA ARS FPED dataset in xls format
│   ├── interim/           # NHANES dataset with selected columns in CSV format and FPED data in XLSX format
│   ├── clean/             # Cleaned data
│   ├── processed/         # Processed data
│   ├── final/             # Final merged data
│
├── database/
│   └── nhanes_2021_2023.db      # SQLite database
│
├── docs/                       # Project documents  
│   ├── final_report.md         # Final analysis report
│   ├── project_plan.md         # Project objective, goals, and analysis plan
|   ├── project_summary.md      # Project final summary     
│
├── notebooks/                  # Jupyter Notebooks
│   ├── data_ingestion_and_cleaning.ipynb      # Data loading, cleaning and wrangling
│   ├── data_loading_database.ipynb            # Load to SQLite & final merge
│   ├── obj_1.1_analysis.ipynb                  # Characterize distributions of lifestyle behaviors and socioeconomic indicators
│   ├── obj_1.2_analysis.ipynb                  # Quantify associations
│   ├── obj_1.3_analysis.ipynb                  # Explore specific relationships
│   ├── obj_1.4_analysis.ipynb                  # Assess combined effects
│   ├── obj_2.1_analysis.ipynb                  # Compare across gender and racial/ethnic groups
│   ├── obj_2.2_analysis.ipynb                  # Effect modification by gender/race
│   └── obj_2.3_analysis.ipynb                  # Data-driven recommendations
│
├── outputs/                    # Visualizations and Summary
│   ├── plots/                  # Output visualization plots
│   └── summary/                # Summary reports about analysis
│
├── scripts/                    # Scripts for config, cleaning, feature engineering
│   ├── config.py
│   ├── utils.py         
│   ├── db.utils.py
│   ├── data_loading.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── calculating_usda_hei_score.py
│   └── [individual cleaning scripts...]
│
├── venv/                       # Virtual environment (hidden)
├── .env                        # Environment variables
├── README.md                   # Project overview
├── requirements.txt            # Python dependencies
```

---

## Additional Information

For a detailed overview of the project's problem statement, goals, purpose, objectives, scope and analysis plan, research questions explored, features, project timeline, risks and mitigation strategies, and test and evaluation plan, please refer to the `docs/project_plan.md` file in this repository. Additionally, the final report and project summary document can be found in the `docs/final_report.md` and `docs/project_summary.md` files, respectively.

---

## Project summary - Interactive Dashboard

You can view the full dashboard including **Key Findings and Recommendations** — by clicking the link below:

[health-track-dashboard.streamlit.app](https://health-track-dashboard.streamlit.app)

---

## Contact

- **Sahiladevi Deenadayalu**  
[sahiladevi2003@gmail.com](mailto:sahiladevi2003@gmail.com)

- **Repository:** [https://github.com/Sahiladevi/health_track](https://github.com/Sahiladevi/health_track) 

---

**End of README File**