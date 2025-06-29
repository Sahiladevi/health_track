# 🧪 Analyzing the Impact of Lifestyle, Socioeconomic Status, and Healthcare Access on Chronic Health Conditions Among U.S. Adults

## 📊 NHANES 2021–2023 Data Analysis Project - health_track

---

## 🎯 Project Objective

This project investigates how **lifestyle behaviors**, **socioeconomic factors**, and **healthcare access** influence chronic health conditions among U.S. adults using the **NHANES 2021–2023 dataset**. We focus on chronic conditions such as:

- Obesity (BMI)
- Hypertension
- Diabetes
- High cholesterol

The key goals are to:

- Understand the role of **diet, physical activity, and sleep** in chronic disease
- Examine how **income, education, and insurance status** affect health
- Identify **gender- and race-based disparities**
- Support **data-driven public health policies**

---

## 📋 Project Overview

Using nationally representative NHANES data, this analysis merges demographic, dietary, physical activity, laboratory, and questionnaire data. By applying both traditional statistical and exploratory visualization techniques, we aim to uncover key relationships between risk factors and health outcomes in U.S. adults.

---

## ⚙️ Features

- ✅ Data ingestion from local NHANES `.XPT` files and conversion to `.CSV`
- ✅ Full data cleaning and merging using **Pandas**
- ✅ Survey-weighted analysis using **statsmodels**
- ✅ Visualizations via **Seaborn**, **Matplotlib**, and **Plotly**
- ✅ SQLite database creation for querying cleaned dataset
- ✅ (Optional) Machine learning clustering and regression
- ✅ (Optional) Streamlit app for interactive visualization

---

## 🛠 Technology Stack

| Component          | Tool / Library                          |
|-------------------|------------------------------------------|
| Programming       | Python (3.9+)                            |
| Data Handling     | Pandas, NumPy                            |
| Visualization     | Seaborn, Matplotlib, Plotly              |
| Statistical Models| Statsmodels (with survey weights)        |
| Database          | SQLite                                   |
| Notebooks         | Jupyter                                  |
| Optional ML       | scikit-learn                             |
| Environment       | Virtualenv or Conda                      |
| Deployment        | (Optional) Streamlit                     |

---

## 📚 Data Source

Data from the **National Health and Nutrition Examination Survey (NHANES)**, a program of studies designed to assess the health and nutritional status of adults and children in the United States.

- 🔗 [NHANES 2021–2023](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?Cycle=2021-2023)
- 📄 Documentation: [NHANES Data Documentation](https://wwwn.cdc.gov/nchs/nhanes/default.aspx)

---
## Data Selection

This project uses a curated subset of variables from the NHANES 2021–2022 datasets. Only relevant columns were selected from each dataset to support our analysis of BMI, lifestyle, and chronic disease risk factors.

For example:
- From `DEMO_L.XPT`, only demographic, education, income, and weight variables were extracted.
- From `BMX_L.XPT`, only the `BMXBMI` (Body Mass Index) column was used.
- All datasets were merged using the common participant identifier `SEQN`.

See `Data Dictionary` for full list of selected variables and their descriptions.
---
## 📘 NHANES 2021–2023 Data Dictionary with Definitions

### 🔹 Step 1: Demographics + BMI

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
| BMX_L   | BMXBMI       | Body Mass Index (kg/m²)                       | Weight (kg) / height (m)^2, indicator of body fat |

---

### 🔹 Step 2: Lifestyle Factors

| Dataset  | Variable     | Description                                     | Definition |
|----------|--------------|-------------------------------------------------|------------|
| PAQ_L    | PAD680       | Minutes of moderate-intensity work activity/week| Self-reported weekly minutes of moderate physical activity |
|          | PAD790Q      | Frequency of vigorous recreational activity     | How often participant engages in vigorous activities |
|          | PAD790U      | Time unit for PAD790Q                           | Units for PAD790Q (e.g., times per week) |
|          | PAD800       | Duration of vigorous activity                   | Average length of vigorous activity sessions |
| SLQ_L    | SLD012       | Sleep hours on weekdays/workdays               | Self-reported average hours of sleep on workdays |
|          | SLD013       | Sleep hours on weekends                        | Self-reported average hours of sleep on weekends |
| DR1TOT_L | DR1TKCAL     | Total daily energy intake (kcal)               | Calories consumed on dietary recall day 1 |
|          | DR1TSFAT     | Saturated fat intake (g)                       | Grams of saturated fat consumed day 1 |
|          | DR1TSUGR     | Total sugars intake (g)                        | Grams of sugars consumed day 1 |
|          | DR1TFIBE     | Total dietary fiber intake (g)                | Grams of fiber consumed day 1 |
|          | WTDR2D       | Dietary Day 1 sample weight                   | Weight for dietary recall day 1 data |
| SMQ_L    | SMQ020       | Smoked at least 100 cigarettes in life         | Ever smoked 100+ cigarettes (Yes/No) |
|          | SMQ040       | Current smoking status                         | Currently smoke cigarettes (Yes/No) |

---

### 🔹 Step 3: Clinical Measures

| Dataset  | Variable     | Description                                   | Definition |
|----------|--------------|-----------------------------------------------|------------|
| BPXO_L   | BPXOSY1-3    | Systolic BP readings 1–3                      | Three systolic blood pressure measurements (mm Hg) |
|          | BPXODI1-3    | Diastolic BP readings 1–3                     | Three diastolic blood pressure measurements (mm Hg) |
| TCHOL_L  | LBXTC        | Total cholesterol (mg/dL)                     | Total blood cholesterol concentration |
| HDL_L    | LBDHDD       | HDL cholesterol (mg/dL)                       | “Good” cholesterol level in blood |
|          | LBDHDDSI     | HDL cholesterol (SI units)                    | HDL cholesterol in SI units (mmol/L) |
|          | WTPH2YR      | Fasting sample weight for cholesterol         | Weight for fasting blood sample data |
| GLU_L    | LBXGLU       | Fasting glucose (mg/dL)                       | Blood glucose concentration after fasting |
|          | LBDGLUSI     | Glucose (SI units)                            | Glucose in SI units (mmol/L) |
|          | WTSAF2YR     | Fasting sample weight                         | Weight for fasting blood sample data |
| INS_L    | LBXIN        | Insulin (uU/mL)                               | Insulin concentration in blood |
|          | LBDINLC      | Insulin (SI units)                            | Insulin in SI units (pmol/L) |
|          | WTSAF2YR     | Fasting sample weight                         | Weight for fasting blood sample data |
| DIQ_L    | DIQ010       | Ever been told you have diabetes?             | Self-reported doctor diagnosis of diabetes (Yes/No) |
| MCQ_L    | MCQ160B      | Ever told had congestive heart failure        | Self-reported CHF diagnosis (Yes/No) |
|          | MCQ160C      | Coronary heart disease                        | Self-reported CHD diagnosis (Yes/No) |
|          | MCQ160D      | Angina/angina pectoris                        | Self-reported angina diagnosis (Yes/No) |
|          | MCQ160E      | Heart attack                                  | Self-reported heart attack diagnosis (Yes/No) |

---

### 🔹 Step 4: Socioeconomic & Healthcare Access

| Dataset   | Variable     | Description                                     | Definition |
|-----------|--------------|-------------------------------------------------|------------|
| DEMO_L    | DMDEDUC2     | Education level                                 | Highest education attained |
|           | INDFMPIR     | Income-to-poverty ratio                         | Family income divided by poverty level |
| HIQ_L     | HIQ011       | Covered by health insurance                     | Has any health insurance coverage (Yes/No) |
| RXQ_RX_L  | RXQ033       | Taken prescription medicine in the past month  | Used prescribed medication in last 30 days (Yes/No) |

---

### 🔹 Step 5: Modeling & Survey Design

| Dataset    | Variable      | Description                                           | Definition |
|------------|---------------|-------------------------------------------------------|------------|
| DEMO_L     | WTINT2YR      | Interview weight (used for questionnaire data)        | Weight to produce nationally representative estimates for interview data |
|            | WTMEC2YR      | MEC exam weight (used for physical/lab data)          | Weight to produce nationally representative estimates for exam data |
|            | SDMVSTRA      | Stratification variable                               | Used to account for survey design strata in analysis |
|            | SDMVPSU       | PSU variable                                          | Primary sampling units to account for clustering in survey design |
| DR1TOT_L   | WTDR2D        | Dietary recall Day 1 weight                           | Weight for Day 1 dietary recall data |
| GLU_L, INS_L | WTSAF2YR    | Fasting subsample weight                              | Weight for fasting subsample lab data |
| HDL_L      | WTPH2YR       | Fasting weight for cholesterol & HDL                  | Weight for fasting lab subsample |
---
## 🎨 Visualizations

- Boxplots and histograms of BMI, glucose, cholesterol
- Grouped bar plots by gender, income, or race
- Scatter plots of calorie intake vs BMI
- Heatmaps of correlation matrices
- Survey-weighted means with confidence intervals

---

## 🔍 Example Research Questions

1. Do low-income individuals have a higher prevalence of diabetes?
2. Does poor diet (e.g., high saturated fat) increase BMI more significantly in women than men?
3. Are physical activity and sleep protective against hypertension?
4. Is access to healthcare associated with better blood pressure control?

---

## 📈 Why Use Survey Weights?

NHANES uses **complex, multistage sampling**, so it's **not valid** to analyze it using raw frequencies. Survey weights correct for:

- Unequal probability of selection
- Oversampling of minorities
- Nonresponse bias

Using weights ensures results generalize to the **entire U.S. population**.

---

## 📂 Project Folder Structure

_📌 Fill this out based on your final organization:_

```
project-root/
│
├── data/                  # Raw and cleaned NHANES data
├── notebooks/             # Jupyter Notebooks
├── outputs/               # Visualizations and tables
├── requirements.txt       # Python dependencies
├── README.md              # Project readme (this file)
├── <your_scripts_here>/   # Data cleaning and analysis scripts
└── <others>/              # Add any other relevant folders
```

---

## 🧪 Setup Instructions

### 1. Clone This Repository

```bash
git clone https://github.com/yourusername/nhanes-chronic-health.git
cd nhanes-chronic-health
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

## 📦 Requirements

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

> Only required libraries are listed. Use a virtual environment for isolation.

---

## 🧪 Testing & Validation

- ✅ All code blocks run successfully in a clean environment
- ✅ Notebooks structured and annotated clearly
- ✅ Survey weights applied appropriately
- ✅ SQLite queries tested with sample SQL statements

---

## 🔁 Version Control

- ✅ Tracked using **Git CLI**
- ✅ Minimum 10 commits
- ✅ No files uploaded via GitHub UI
- ✅ `.gitignore` includes temporary and output files

---

## 🧠 Risk Mitigation

| Risk                                | Mitigation Strategy                             |
|-------------------------------------|-------------------------------------------------|
| Large file sizes                    | Process subset or convert to SQLite             |
| Missing values                      | Imputation or exclusion, documented in notebook |
| Incorrect weight usage              | Follow NHANES documentation strictly            |
| Reproducibility                     | Use virtualenv + requirements.txt               |

---

## 📢 Contributing

We welcome collaboration!

1. Fork the repo
2. Create a feature branch
3. Make your changes
4. Push and open a pull request

---

## 🙌 Acknowledgements

Thanks to the **CDC/NCHS** for the NHANES dataset and documentation.  
Gratitude to open-source contributors of **Pandas**, **Seaborn**, and **Plotly**.

---

## 📬 Contact

**Sahiladevi Deenadayalu**  
📧 [sahiladevi2003@gmail.com](mailto:sahiladevi2003@gmail.com)