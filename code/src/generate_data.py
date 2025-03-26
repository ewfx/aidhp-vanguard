import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
np.random.seed(42)

# Generate user profiles
num_users = 1000

users = []
for user_id in range(1, num_users + 1):
    age = np.random.randint(20, 65)
    income = np.random.randint(30000, 200000)
    job_type = np.random.choice(["Salaried", "Self-Employed", "Freelancer", "Investor"])
    risk_tolerance = np.random.choice(["Low", "Medium", "High"])

    users.append([user_id, age, income, job_type, risk_tolerance])

users_df = pd.DataFrame(users, columns=["UserID", "Age", "Income", "JobType", "RiskTolerance"])

# Generate transactions
num_transactions = 5000

transactions = []
for _ in range(num_transactions):
    user_id = np.random.randint(1, num_users + 1)
    transaction_type = np.random.choice(["Salary", "Groceries", "Shopping", "Investment", "Loan Payment"])
    amount = abs(np.random.normal(500, 300))  # Random amounts
    date = fake.date_between(start_date="-2y", end_date="today")

    transactions.append([user_id, date, transaction_type, round(amount, 2)])

transactions_df = pd.DataFrame(transactions, columns=["UserID", "Date", "TransactionType", "Amount"])

# Save to CSV
users_df.to_csv("users.csv", index=False)
transactions_df.to_csv("transactions.csv", index=False)

print("✅ Data generated: users.csv & transactions.csv")
