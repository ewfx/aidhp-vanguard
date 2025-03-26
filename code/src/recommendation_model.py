def recommend_product(user_data):
    total_income = user_data.get("TotalIncome", 0)
    total_spending = user_data.get("TotalSpending", 0)
    investment = user_data.get("Investment", 0)
    savings = user_data.get("Savings", 0)
    age = user_data.get("Age", 0)
    job_type = user_data.get("JobType", 0)
    risk_tolerance = user_data.get("RiskTolerance", 0)

    # 🟢 Improved Credit Card Logic
    if total_income > 100000:
        credit_card = "Premium Credit Card"
    elif total_income > 50000:
        credit_card = "Cashback Credit Card"  # Changed from Basic to Cashback
    elif job_type == 3:  # Freelancer
        credit_card = "Freelancer Cashback Credit Card"
    else:
        credit_card = "Basic Credit Card"

    # 🟢 Improved Investment Logic
    if risk_tolerance == 2:  # High Risk
        investment_option = "Stock Portfolio & Mutual Funds"
    elif risk_tolerance == 1:  # Medium Risk
        investment_option = "Mutual Funds & ETFs"
    else:  # Low Risk
        investment_option = "Fixed Deposits & Bonds"

    # Loan Recommendation
    loan_offer = "No Loan Needed"
    if total_spending > total_income * 0.6:
        loan_offer = "Personal Loan"
    elif job_type == 4:  # Business Owner
        loan_offer = "Business Loan"

    return {
        "credit_card": credit_card,
        "loan": loan_offer,
        "investment": investment_option
    }
