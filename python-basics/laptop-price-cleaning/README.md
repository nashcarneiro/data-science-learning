Laptop Data Cleaning & Feature Engineering

A complete data preprocessing project built with Python and Pandas. This project demonstrates how raw laptop data can be cleaned, transformed, and prepared for machine learning and data analysis.

Project Overview

The objective of this project is to perform essential data preprocessing techniques commonly used in data analytics and machine learning workflows. The dataset is cleaned, transformed, and enriched with new features while preserving data quality and improving usability.

Technologies Used
Python
Pandas
NumPy
Matplotlib

Project Tasks

-Data Inspection

-Loaded the dataset into a Pandas DataFrame

-Examined data types, missing values, and summary statistics

-Handling Missing Values
Replaced missing values in Weight_kg using the column mean
Replaced missing values in Screen_Size_cm using the most frequent value (mode)

-Data Type Validation
-Verified numerical columns contained the correct data types

-Feature Engineering
Created new features while preserving the original data:
Converted Weight_kg to Weight_lb
Converted Screen_Size_cm to Screen_Size_inch

-Data Normalization
Normalized CPU frequency values using Min-Max normalization

-Data Binning

Grouped laptop prices into three categories:
Low
Medium
High

-Categorical Encoding
Converted the Screen column into numerical indicator variables by creating separate binary columns for:
IPS Panel
Full HD
The original Screen column was then removed, making the dataset more suitable for machine learning models.

-Data Visualization
Created a bar chart to visualize the distribution of laptops across the three price categories.

Export
Saved the cleaned dataset as an Excel workbook for further analysis.
