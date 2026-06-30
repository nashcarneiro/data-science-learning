# Laptop Price Exploratory Data Analysis

This project explores a laptop pricing dataset using Python to better understand which hardware specifications influence laptop prices. The analysis focuses on exploring the data, identifying relationships between features, and applying statistical techniques before moving on to predictive machine learning.

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

## Project Overview

The analysis includes:
Exploring the dataset and generating descriptive statistics
Creating regression plots for numerical features
Performing Pearson correlation analysis and hypothesis testing
Comparing categorical features using boxplots
Grouping and summarizing data with `groupby()`
Creating pivot tables
Visualizing grouped data with a heatmap
Interpreting statistical results to identify the strongest predictors of laptop price

## Key Findings
RAM capacity showed the strongest positive relationship with laptop price.
CPU core count and CPU frequency were also important predictors.
SSD storage had a weaker but statistically significant positive relationship with price.
Screen size and laptop weight showed little evidence of a meaningful linear relationship with price.
Several categorical features displayed distinct price distributions, suggesting they may be useful predictors in future machine learning models.

## Visualizations

Regression Plots

- CPU Frequency vs Price
- Screen Size vs Price
- Weight vs Price

Boxplots

- Category
- GPU
- Operating System
- CPU Core
- RAM
- SSD Storage

Heatmap

- Average laptop price by GPU and CPU Core
