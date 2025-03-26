import streamlit as st
import requests

# Streamlit UI layout
st.title("💰 Hyper-Personalized Financial Recommendations")

# User Input Fields
age = st.number_input("Enter Your Age", min_value=18, max_value=100, value=30)
total_income = st.number_input("Enter Your Annual Income ($)", min_value=0, value=50000)
total_spending = st.number_input("Enter Your Annual Spending ($)", min_value=0, value=20000)
investment = st.number_input("Current Investment Amount ($)", min_value=0, value=5000)
job_type = st.selectbox("Select Job Type", ["Salaried", "Self-Employed", "Freelancer", "Investor", "Business Owner", "Student", "Retired"])
risk_tolerance = st.radio("Select Risk Tolerance", ["Low", "Medium", "High"])

# Convert job type to a number for API
job_type_mapping = {
    "Salaried": 0,
    "Self-Employed": 1,
    "Freelancer": 2,
    "Investor": 3,
    "Business Owner": 4,
    "Student": 5,
    "Retired": 6
}
job_type_value = job_type_mapping[job_type]

# Convert risk tolerance to a number for API
risk_tolerance_mapping = {"Low": 0, "Medium": 1, "High": 2}
risk_tolerance_value = risk_tolerance_mapping[risk_tolerance]

# Calculate Savings
savings = total_income - total_spending

# Submit Button
if st.button("Get Recommendations"):
    # API Request Data
    user_data = {
        "TotalIncome": total_income,
        "TotalSpending": total_spending,
        "Investment": investment,
        "Savings": savings,
        "Age": age,
        "JobType": job_type_value,
        "RiskTolerance": risk_tolerance_value
    }

    # Call API
    try:
        response = requests.post("http://127.0.0.1:5000/recommend", json=user_data)
        if response.status_code == 200:
            recommendations = response.json()
            st.success(f"✅ **Credit Card:** {recommendations['credit_card']}")
            st.info(f"🏦 **Loan Offer:** {recommendations['loan']}")
            st.warning(f"📈 **Investment Option:** {recommendations['investment']}")
        else:
            st.error("⚠️ API Error: " + response.text)
    except Exception as e:
        st.error(f"⚠️ Connection Error: {e}")
