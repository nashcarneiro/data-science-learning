# Automobile Data Preprocessing & Exploratory Data Analysis

A Python data analysis project that explores automobile pricing through data preprocessing, exploratory data analysis (EDA), statistical testing, correlation analysis, and data visualization using Pandas, NumPy, Seaborn, Matplotlib, and SciPy.

---

## Project Overview

This project demonstrates a complete exploratory data analysis workflow on an automobile dataset.

The goal was to clean and preprocess the data, identify relationships between different automobile features and price, perform statistical analysis, and visualize insights that can support predictive modeling.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

---

## Project Workflow

### Data Inspection

- Loaded the dataset into a Pandas DataFrame
- Explored column names, data types, and descriptive statistics
- Identified missing values

### Data Cleaning

- Replaced missing values using the mean and mode where appropriate
- Corrected data types
- Removed invalid or incomplete records when necessary

### Exploratory Data Analysis

- Generated descriptive statistics
- Used `value_counts()` to inspect categorical variables
- Performed `groupby()` operations
- Created pivot tables to summarize relationships

### Correlation Analysis

Calculated Pearson correlation coefficients to measure the strength and direction of relationships between automobile price and numerical variables.

Variables analyzed include:

- Engine Size
- Highway MPG
- Peak RPM
- Wheel Base
- Horsepower
- Curb Weight

### Statistical Testing

Performed Pearson correlation hypothesis testing using SciPy.

For each feature, calculated:

- Pearson Correlation Coefficient
- P-value

to determine whether the observed relationship with price was statistically significant.

### Data Visualization

Created multiple visualizations, including:

- Regression plots
- Scatter plots
- Heatmaps
- Correlation analysis
- Pivot table visualizations

---

## Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Statistical Analysis
- Correlation Analysis
- Hypothesis Testing
- Feature Relationship Analysis
- GroupBy Operations
- Pivot Tables
- Data Visualization
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
