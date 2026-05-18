import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="Urban Company Churn Analysis",
    layout="wide"
)

# ------------------------------------------------
# LOAD DATA
# ------------------------------------------------

df = pd.read_csv("customer_churn_analysis.csv")

# ------------------------------------------------
# TITLE
# ------------------------------------------------

st.title("Urban Company Service Intelligence & Churn Risk Analysis")

st.markdown("""
This application analyzes customer behavior,
churn risk, and retention intelligence
for Urban Company customers.
""")

# ------------------------------------------------
# KPI SECTION
# ------------------------------------------------

st.subheader("Executive Overview")

col1, col2, col3, col4 = st.columns(4)

total_customers = df['customer_id'].nunique()

churn_rate = round(
    (df['churn'].mean()) * 100,
    2
)

high_risk_customers = df[
    df['churn_probability'] > 0.75
].shape[0]

avg_spend = round(
    df['total_spend'].mean(),
    2
)

col1.metric(
    "Total Customers",
    total_customers
)

col2.metric(
    "Churn Rate",
    f"{churn_rate}%"
)

col3.metric(
    "High Risk Customers",
    high_risk_customers
)

col4.metric(
    "Average Customer Spend",
    f"₹{avg_spend}"
)

# ------------------------------------------------
# RISK SEGMENTATION
# ------------------------------------------------

st.subheader("Customer Risk Distribution")

fig, ax = plt.subplots()

df['churn'].value_counts().plot(
    kind='bar',
    ax=ax
)

plt.title("Churn Distribution")

st.pyplot(fig)

# ------------------------------------------------
# CHURN PROBABILITY DISTRIBUTION
# ------------------------------------------------

st.subheader("Churn Probability Distribution")

fig, ax = plt.subplots()

sns.histplot(
    df['churn_probability'],
    bins=20,
    ax=ax
)

plt.title("Customer Churn Probability")

st.pyplot(fig)

# ------------------------------------------------
# HIGH RISK CUSTOMERS
# ------------------------------------------------

st.subheader("High Risk Customers")

high_risk_df = df[
    df['churn_probability'] > 0.75
]

st.dataframe(high_risk_df.head(20))

# ------------------------------------------------
# CUSTOMER SEARCH
# ------------------------------------------------

st.subheader("Search Customer")

customer_input = st.number_input(
    "Enter Customer ID",
    min_value=int(df['customer_id'].min()),
    max_value=int(df['customer_id'].max()),
    step=1
)

customer_data = df[
    df['customer_id'] == customer_input
]

st.dataframe(customer_data)

# ------------------------------------------------
# BUSINESS INSIGHTS
# ------------------------------------------------

st.subheader("Business Insights")

st.markdown("""
### Key Findings

- Customers inactive for long periods are highly likely to churn.
- Frequent bookings reduce churn risk.
- High-spending customers tend to stay loyal.
- Customer inactivity is the strongest churn indicator.
- Customers with repeated cancellations show higher churn behavior.

### Business Recommendations

- Target inactive customers with retention campaigns.
- Create loyalty programs for repeat users.
- Offer premium benefits to high-value customers.
- Improve customer engagement through personalized offers.
""")

# ------------------------------------------------
# FULL DATASET
# ------------------------------------------------

st.subheader("Customer Intelligence Dataset")

st.dataframe(df)

# cd "C:\Users\Priya\OneDrive\Desktop\SHUBHAM\Data Science Projects\URBAN  COMPANY SERVICE INTELLIGENCE & CHURN RISK ANALYSIS"
# streamlit run app/app.py