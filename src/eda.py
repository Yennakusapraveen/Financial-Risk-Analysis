import pandas as pd
import matplotlib.pyplot as plt

# ======================================
# LOAD CLEAN DATASET
# ======================================
df = pd.read_csv("data/cleaned_loan.csv")

print("="*60)
print("FINANCIAL RISK ANALYSIS - EDA")
print("="*60)

# ======================================
# DATASET OVERVIEW
# ======================================

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# ======================================
# LOAN STATUS ANALYSIS
# ======================================

print("\nLoan Status Count")
print(df["Loan_Status"].value_counts())

loan_status = df["Loan_Status"].value_counts()

loan_status.plot(kind="bar")
plt.title("Loan Approval Status")
plt.xlabel("Loan Status")
plt.ylabel("Number of Applicants")
plt.show()

# ======================================
# GENDER ANALYSIS
# ======================================

print("\nGender Count")
print(df["Gender"].value_counts())

gender = df["Gender"].value_counts()

gender.plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# ======================================
# EDUCATION ANALYSIS
# ======================================

print("\nEducation Count")
print(df["Education"].value_counts())

education = df["Education"].value_counts()

education.plot(kind="bar")
plt.title("Education Distribution")
plt.xlabel("Education")
plt.ylabel("Count")
plt.show()

# ======================================
# PROPERTY AREA ANALYSIS
# ======================================

print("\nProperty Area Count")
print(df["Property_Area"].value_counts())

property_area = df["Property_Area"].value_counts()

property_area.plot(kind="bar")
plt.title("Property Area Distribution")
plt.xlabel("Property Area")
plt.ylabel("Count")
plt.show()

# ======================================
# CREDIT HISTORY ANALYSIS
# ======================================

print("\nCredit History Count")
print(df["Credit_History"].value_counts())

credit = df["Credit_History"].value_counts()

credit.plot(kind="bar")
plt.title("Credit History")
plt.xlabel("Credit History")
plt.ylabel("Count")
plt.show()

# ======================================
# APPLICANT INCOME
# ======================================

print("\nApplicant Income Statistics")
print(df["ApplicantIncome"].describe())

plt.hist(df["ApplicantIncome"], bins=20)
plt.title("Applicant Income Distribution")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()

# ======================================
# LOAN AMOUNT
# ======================================

print("\nLoan Amount Statistics")
print(df["LoanAmount"].describe())

plt.hist(df["LoanAmount"], bins=20)
plt.title("Loan Amount Distribution")
plt.xlabel("Loan Amount")
plt.ylabel("Frequency")
plt.show()

print("\nEDA COMPLETED SUCCESSFULLY")