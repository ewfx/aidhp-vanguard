import pandas as pd

# Load datasets
users_df = pd.read_csv("users.csv")
transactions_df = pd.read_csv("transactions.csv")

# Convert date column to datetime
transactions_df["Date"] = pd.to_datetime(transactions_df["Date"])

# Merge user data with transactions
data = transactions_df.merge(users_df, on="UserID", how="left")

# Extract year-month for aggregation
data["YearMonth"] = data["Date"].dt.to_period("M")

# Group transactions to calculate financial features
agg_data = data.groupby(["UserID", "YearMonth"]).agg(
    TotalIncome=("Amount", lambda x: x[data["TransactionType"] == "Salary"].sum()),
    TotalSpending=("Amount", lambda x: x[data["TransactionType"] != "Salary"].sum()),
    Investment=("Amount", lambda x: x[data["TransactionType"] == "Investment"].sum())
).reset_index()

# Calculate savings
agg_data["Savings"] = agg_data["TotalIncome"] - agg_data["TotalSpending"]

# Merge with user profile
final_data = agg_data.merge(users_df, on="UserID", how="left")

# Save feature set
final_data.to_csv("features.csv", index=False)

print("✅ Feature extraction complete: features.csv")
