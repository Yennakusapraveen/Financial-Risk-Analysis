import pandas as pd
import sqlite3

# Load cleaned dataset
df = pd.read_csv("data/cleaned_loan.csv")

# Create database
conn = sqlite3.connect("loan_analysis.db")

# Store dataset as SQL table
df.to_sql("loan_data", conn, if_exists="replace", index=False)

print("Database created successfully!")

conn.close()