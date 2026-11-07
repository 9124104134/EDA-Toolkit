
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Dataset Overview
def dataset_overview(data):

    print("=" * 50)
    print("DATASET OVERVIEW")
    print("=" * 50)

    print("\nNumber of Rows:", data.shape[0])
    print("Number of Columns:", data.shape[1])

    print("\nColumn Names:")
    print(data.columns.tolist())

    print("\nData Types:")
    print(data.dtypes)

    print("\nDataset Information:")
    data.info()


# 2. Missing Value Analysis
def missing_value_report(data):

    report = pd.DataFrame({
        "Missing Count": data.isnull().sum(),
        "Missing Percentage": (data.isnull().sum() / len(data)) * 100
    })

    report = report[report["Missing Count"] > 0]

    if report.empty:
        print("No missing values found!")
    else:
        display(report.sort_values(
            by="Missing Percentage",
            ascending=False
        ))


# 3. Numerical and Categorical Summary
def column_summary(data):

    numerical_columns = data.select_dtypes(
        include=["number"]
    ).columns.tolist()

    categorical_columns = data.select_dtypes(
        include=["object", "category", "bool"]
    ).columns.tolist()

    print("Numerical Columns:")
    print(numerical_columns)

    print("\nCategorical Columns:")
    print(categorical_columns)

    if numerical_columns:
        print("\nNumerical Summary:")
        display(data[numerical_columns].describe())
    else:
        print("\nNo numerical columns found.")

    if categorical_columns:
        print("\nCategorical Summary:")
        display(data[categorical_columns].describe())
    else:
        print("\nNo categorical columns found.")


# 4. Numerical Distribution
def plot_numerical_distributions(data):

    numerical_columns = data.select_dtypes(
        include=["number"]
    ).columns.tolist()

    if not numerical_columns:
        print("No numerical columns found!")
        return

    for column in numerical_columns:

        plt.figure(figsize=(7, 4))
        sns.histplot(data=data, x=column, kde=True)

        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()


# 5. Categorical Distribution
def plot_categorical_distributions(data):

    categorical_columns = data.select_dtypes(
        include=["object", "category", "bool"]
    ).columns.tolist()

    if not categorical_columns:
        print("No categorical columns found!")
        return

    for column in categorical_columns:

        plt.figure(figsize=(8, 4))

        order = data[column].value_counts().index

        sns.countplot(
            data=data,
            x=column,
            order=order
        )

        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


# 6. Correlation Analysis
def correlation_analysis(data, exclude_columns=None):

    if exclude_columns is None:
        exclude_columns = []

    numerical_data = data.select_dtypes(
        include=["number"]
    ).drop(columns=exclude_columns, errors="ignore")

    if numerical_data.shape[1] < 2:
        print("At least two numerical columns are required.")
        return

    correlation_matrix = numerical_data.corr()

    print("Correlation Matrix:")
    display(correlation_matrix)

    plt.figure(figsize=(10, 7))

    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5
    )

    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()
