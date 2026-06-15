import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Customer Churn Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Analytics Dashboard")

st.write("""
This dashboard analyzes customer churn behavior in a retail banking dataset.
""")

df = pd.read_csv("data/Churn_Modelling.csv")

total_customers = len(df)

churn_rate = round(df["Exited"].mean() * 100, 2)

avg_age = round(df["Age"].mean(), 1)

avg_balance = round(df["Balance"].mean(), 2)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Customers", total_customers)

with col2:
    st.metric("Churn Rate", f"{churn_rate}%")

with col3:
    st.metric("Average Age", avg_age)

with col4:
    st.metric("Average Balance", f"{avg_balance:,.0f}")

st.markdown("---")

st.subheader("Dataset Preview")

with st.expander("View Dataset Sample"):
    st.dataframe(df.head())

st.markdown("---")

st.subheader("📍 Churn Rate by Geography")

geo_churn = (
    df.groupby("Geography")["Exited"]
      .mean()
      .sort_values(ascending=False)
      * 100
)

st.bar_chart(geo_churn)

st.info(
    "Germany shows the highest churn rate among the three regions, suggesting that retention efforts could be prioritized there."
)