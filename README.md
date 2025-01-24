# E-Commerce Data Cleaning and Analysis exercise

This project provides a Python-based solution for cleaning, transforming, and analyzing e-commerce sales data stored in a CSV file. It uses **Pandas** to preprocess the data and generate summaries for insights.

## Features

- **Data Loading**: Load data from a CSV file into a Pandas DataFrame.
- **Cleaning and Validation**:
  - Remove duplicates and whitespace from column names.
  - Ensure proper data types for numeric columns.
  - Handle missing values and invalid dates.
  - Convert float columns to integers when necessary.
- **Feature Engineering**:
  - Create new columns, such as `total_price`.
  - Extract day, month, and year from the `order_date` column.
- **Analysis and Summarization**:
  - Group data by product category to calculate total sales and average quantity.
  - Generate a pivot table summarizing total sales by product category and month.
  - Show unit prices as percentages relative to the average price.

## Prerequisites

- Python
- Pandas library

Install Pandas if not already installed:
```bash
pip install pandas
