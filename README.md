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

## 📁 Data Dictionary
### 1. Demographics & Socioeconomic Variables

| Variable      | Description                            | Dataset  | Notes                         |
|---------------|----------------------------------------|----------|-------------------------------|
| SEQN          | Participant ID (key)                   | DEMO_L   | Key for merging datasets      |
| RIAGENDR      | Gender (1=Male, 2=Female)              | DEMO_L   | Used for subgroup analysis    |
| RIDRETH3      | Race/Ethnicity                         | DEMO_L   | e.g., NH White, NH Black      |
| DMDEDUC2      | Education Level (20+ yrs)              | DEMO_L   | Categorical                   |
| INDFMPIR      | Poverty Income Ratio                   | DEMO_L   | Proxy for socioeconomic status|

### 2. Lifestyle Factors

| Variable     | Description                                  | Dataset  | Notes                      |
|--------------|----------------------------------------------|----------|----------------------------|
| PAD680       | Sedentary minutes/day                        | PAQ_L    | Screen/sitting time        |
| PAD790Q/U    | Physical activity frequency + unit           | PAQ_L    | Unit: day/week/month/year  |
| PAD800       | Duration per activity session                | PAQ_L    | In minutes                 |
| SLD012/13    | Sleep duration (weekday/weekend)             | SLQ_L    | Self-reported              |
| DR1TKCAL     | Daily caloric intake                         | DR1TOT_L | 24-hr recall               |
| DR1TSFAT     | Saturated fat intake (g)                     | DR1TOT_L | Optional dietary metric    |

### 3. Healthcare Access

| Variable    | Description                                      | Dataset   | Notes                        |
|-------------|--------------------------------------------------|-----------|------------------------------|
| HIQ011      | Insurance status (Yes/No)                        | HIQ_L     | Yes/No indicator             |
| RXQ033      | Prescription medicine (past 30 days)             | RXQ_RX_L  | Medication usage             |
| BPQ101D     | Taking meds to lower blood cholesterol           | BPQ_L     | Medication usage             |

### 4. Health Outcomes

| Variable        | Description                         | Dataset       | Notes                      |
|-----------------|-------------------------------------|---------------|----------------------------|
| BMXBMI          | Body Mass Index                     | BMX_L         | Measured                   |
| BPXOSY          | Blood pressure (systolic)           | BPXO_L        | 3 readings per participant |
| BPXODI          | Blood pressure (diastolic)          | BPXO_L        | 3 readings per participant |
| LBXTC           | Total cholesterol                   | TCHOL_L       | Lab results                |
| LBXHDL          | HDL cholesterol                     | HDL_L         | Lab results                |
| LBXGLU          | Glucose                             | GLU_L         | Metabolic indicators       |
| LBXIN           | Insulin                             | INS_L         | Metabolic indicators       |
| LBDGLUSI        | HOMA-IR (SI units)                  | GLU_L         | Metabolic indicators       |
| DIQ010          | Diagnosed Diabetes (Yes/No)         | DIQ _L        | Chronic condition          |
| BPQ020          | Diagnosed Hypertension              | BPQ_L         | Chronic condition          |
| BPQ080          | Diagnosed high cholesterol          | BPQ_L         | Chronic condition          |
| MCQ160B-E       | Cardiovascular conditions           | MCQ_L         | Heart disease types        |


### 5. Survey Design Variables

| Variable     | Description                         | Dataset  | Notes                    |
|--------------|-------------------------------------|----------|--------------------------|
| WTMEC2YR     | MEC sample weight                   | DEMO_L   | Lab and physical data    |
| WTDR2D       | 2-day dietary recall weight         | DR1TOT_L | Use for dietary analyses |
| SDMVSTRA     | Stratification variable             | DEMO_L   | Required for variance    |
| SDMVPSU      | Primary Sampling Unit               | DEMO_L   | Cluster identifier       |

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