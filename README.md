# Financial Risk Analysis & Loan Approval Prediction

## Project Overview

This project analyzes loan application data and predicts whether a loan application will be approved or rejected using Machine Learning.

## Tech Stack

- Python
- Pandas
- NumPy
- SQLite
- Scikit-learn
- Matplotlib
- GitHub

## Dataset

- Total Records: 614
- Features: 13
- Target Variable: Loan_Status

## Data Cleaning

- Handled missing values using Mode and Median.
- Converted categorical variables into numerical values.
- Removed unnecessary columns.

## Exploratory Data Analysis

Key Insights:

- 422 loans approved
- 192 loans rejected
- Graduates had higher approval rates
- Semiurban applicants had highest approval rates
- Credit History was the strongest predictor

## SQL Analysis

Performed:

- COUNT()
- AVG()
- MAX()
- MIN()
- GROUP BY

Business analyses:

- Loan Approval Analysis
- Gender Analysis
- Education Analysis
- Property Area Analysis
- Credit History Analysis

## Machine Learning

Model Used:

- Logistic Regression

Results:

- Accuracy: 78.86%

Confusion Matrix:

18 True Negatives
25 False Positives
1 False Negative
79 True Positives

## How to Run

```bash
pip install pandas numpy matplotlib scikit-learn

python src/cleaning.py
python src/eda.py
python src/model.py
```
