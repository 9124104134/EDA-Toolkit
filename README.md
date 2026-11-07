# 📊 Automated EDA Toolkit

An interactive and reusable **Exploratory Data Analysis (EDA) Toolkit** built using Python. This project helps users understand datasets, identify missing values, analyze distributions, visualize relationships, and perform feature engineering through reusable functions.

The project demonstrates practical data analysis using real-world datasets and automated visualization techniques.

## 🚀 Project Overview

Exploratory Data Analysis is an important step in every Data Science and Machine Learning project.

This toolkit simplifies the EDA process by providing reusable Python functions that can be applied to different datasets without repeatedly writing the same analysis code.

## ✨ Key Features

### 1. Dataset Exploration
- Dataset dimensions and structure
- Column names and data types
- Statistical summaries
- Unique value analysis

### 2. Data Cleaning and Preprocessing
- Missing value identification and handling
- Duplicate record detection
- Numerical and categorical data handling
- Outlier identification using the IQR method

### 3. Data Visualization
- Histograms for numerical distributions
- Count plots for categorical distributions
- Univariate, bivariate, and multivariate analysis
- Correlation matrices and heatmaps

### 4. Feature Engineering
- Passenger title extraction
- Family size calculation
- Identification of passengers travelling alone
- Age grouping
- Fare categorization

### 5. Reusable EDA Functions
The toolkit includes six reusable functions:

| Function | Description |
|---|---|
| `dataset_overview()` | Displays dataset structure and information |
| `missing_value_report()` | Generates a missing value report |
| `column_summary()` | Summarizes numerical and categorical columns |
| `plot_numerical_distributions()` | Generates numerical distribution plots |
| `plot_categorical_distributions()` | Generates categorical count plots |
| `correlation_analysis()` | Generates correlation matrices and heatmaps |

### 6. Multiple Dataset Support
The toolkit is demonstrated using:
- Titanic Dataset
- Wine Quality Dataset

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook / Google Colab

## 📁 Project Structure

```text
EDA-Toolkit/
│
├── notebooks/
│   └── 01_Dataset_Exploration.ipynb
│
├── Automated_EDA_Toolkit/
│   ├── analysis.py
│   └── __init__.py
│
├── datasets/
│
├── outputs/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/9124104134/EDA-Toolkit.git
```

Navigate to the project directory:

```bash
cd EDA-Toolkit
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## 💻 Usage

Import the reusable functions from the toolkit:

```python
import sys
sys.path.append(".")

from Automated_EDA_Toolkit import (
    dataset_overview,
    missing_value_report,
    column_summary,
    plot_numerical_distributions,
    plot_categorical_distributions,
    correlation_analysis
)
```

Load a dataset:

```python
import pandas as pd

df = pd.read_csv("your_dataset.csv")
```

Run the analysis:

```python
dataset_overview(df)

missing_value_report(df)

column_summary(df)

plot_numerical_distributions(df)

plot_categorical_distributions(df)

correlation_analysis(df)
```

## 📈 Project Learning Outcomes

Through this project, I gained practical experience in:

- Data exploration and preprocessing
- Handling missing values and duplicates
- Statistical analysis and visualization
- Feature engineering
- Writing reusable Python functions
- Handling edge cases in data analysis
- Applying EDA techniques to multiple datasets
- Organizing and maintaining a GitHub project

## 🔮 Future Enhancements

- Automated EDA report generation
- Interactive dashboards
- Advanced outlier detection
- Feature selection techniques
- Automated data quality assessment
- Support for additional datasets and file formats

## 👩‍💻 Author

**Sai Shruthi**

Computer Science and Engineering Student

---

⭐ If you find this project useful, consider giving the repository a star!

**GitHub Repository:**  
https://github.com/9124104134/EDA-Toolkit
