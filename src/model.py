import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ======================================
# Load Dataset
# ======================================

df = pd.read_csv("data/cleaned_loan.csv")

# ======================================
# Encoding
# ======================================

df["Loan_Status"] = df["Loan_Status"].map({"Y":1, "N":0})

df["Gender"] = df["Gender"].map({"Male":1, "Female":0})
df["Married"] = df["Married"].map({"Yes":1, "No":0})
df["Education"] = df["Education"].map({"Graduate":1, "Not Graduate":0})
df["Self_Employed"] = df["Self_Employed"].map({"Yes":1, "No":0})

df["Property_Area"] = df["Property_Area"].map({
    "Rural":0,
    "Semiurban":1,
    "Urban":2
})

df["Dependents"] = df["Dependents"].replace("3+", 3)
df["Dependents"] = df["Dependents"].astype(int)

df = df.drop("Loan_ID", axis=1)

# ======================================
# Features and Target
# ======================================

X = df.drop("Loan_Status", axis=1)

y = df["Loan_Status"]

# ======================================
# Train Test Split
# ======================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ======================================
# Model Training
# ======================================

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# ======================================
# Prediction
# ======================================

y_pred = model.predict(X_test)

# ======================================
# Accuracy
# ======================================

accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", round(accuracy * 100, 2), "%")
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

sns.heatmap(cm,
            annot=True,
            fmt="d")

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()