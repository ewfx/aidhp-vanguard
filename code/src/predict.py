import pandas as pd
import joblib
import numpy as np

# Load the trained model
model = joblib.load("recommendation_model.pkl")

# Load data for reference
df = pd.read_csv("features.csv")

# Drop non-numeric columns
df = df.drop(columns=["YearMonth"])

# Define a sample user (You can replace values with real data)
sample_user = {
    "TotalIncome": 80000,
    "TotalSpending": 30000,
    "Investment": 5000,
    "Savings": 50000,
    "Age": 35,
    "Income": 80000,
    "JobType": 1,  # (0 = Salaried, 1 = Self-Employed, etc.)
    "RiskTolerance": 2,  # (0 = Low, 1 = Medium, 2 = High)
}

# Convert sample user to DataFrame
input_df = pd.DataFrame([sample_user])

# Make prediction
predicted_product = model.predict(input_df)[0]

# Decode product recommendation
product_mapping = {0: "Fixed Deposit", 1: "Mutual Fund", 2: "Stock Portfolio", 3: "Stocks", 4: "Hedge Fund"}
recommended_product = product_mapping[predicted_product]

print(f"✅ Recommended Product: {recommended_product}")
