import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

# Load data
df = pd.read_csv("features.csv")

# Drop non-numeric columns
df = df.drop(columns=["YearMonth"])

# Encode categorical variables
label_encoders = {}
for col in ["JobType", "RiskTolerance"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Define financial products based on user risk profile
def assign_product(risk_tolerance, investment):
    if risk_tolerance == 0:  # Low risk
        return "Fixed Deposit" if investment < 1000 else "Mutual Fund"
    elif risk_tolerance == 1:  # Medium risk
        return "Mutual Fund" if investment < 5000 else "Stock Portfolio"
    else:  # High risk
        return "Stocks" if investment < 10000 else "Hedge Fund"

df["ProductRecommendation"] = df.apply(lambda row: assign_product(row["RiskTolerance"], row["Investment"]), axis=1)

# Encode target variable
df["ProductRecommendation"] = LabelEncoder().fit_transform(df["ProductRecommendation"])

# Define features & target
X = df.drop(columns=["UserID", "ProductRecommendation"])
y = df["ProductRecommendation"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Trained. Accuracy: {accuracy:.2f}")

# Save model
joblib.dump(model, "recommendation_model.pkl")
print("✅ Model saved as recommendation_model.pkl")
