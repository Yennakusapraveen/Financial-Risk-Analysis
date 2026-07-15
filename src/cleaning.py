import pandas as pd

# ======================================
# STEP 1 : Load Dataset
# ======================================
df = pd.read_csv("data/loan.csv")

# ======================================
# STEP 2 : Check Missing Values
# ======================================
print("Missing Values Before Cleaning")
print(df.isnull().sum())

# ======================================
# STEP 3 : Clean Categorical Columns
# ======================================

df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])

df["Married"] = df["Married"].fillna(df["Married"].mode()[0])

df["Dependents"] = df["Dependents"].fillna(df["Dependents"].mode()[0])

df["Self_Employed"] = df["Self_Employed"].fillna(df["Self_Employed"].mode()[0])

df["Credit_History"] = df["Credit_History"].fillna(df["Credit_History"].mode()[0])

# ======================================
# STEP 4 : Clean Numerical Columns
# ======================================

df["LoanAmount"] = df["LoanAmount"].fillna(df["LoanAmount"].median())

df["Loan_Amount_Term"] = df["Loan_Amount_Term"].fillna(df["Loan_Amount_Term"].median())

# ======================================
# STEP 5 : Verify Missing Values
# ======================================

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

# ======================================
# STEP 6 : Save Clean Dataset
# ======================================

df.to_csv("data/cleaned_loan.csv", index=False)

print("\nDataset cleaned successfully.")
print("Saved as: data/cleaned_loan.csv")