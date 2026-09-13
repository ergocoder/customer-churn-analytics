# Customer Churn Analytics

Project link: https://customer-churn-analytics-dash.streamlit.app/

## Overview

Customer churn is a critical challenge in the banking industry, as retaining existing customers is often more cost-effective than acquiring new ones.

This project analyzes customer churn using a retail banking dataset to identify key churn drivers, build a predictive model, and generate business recommendations that can support customer retention strategies.

## Objectives

- Analyze customer churn patterns through Exploratory Data Analysis (EDA)
- Identify factors associated with customer attrition
- Build a machine learning model to predict churn
- Translate findings into actionable business insights
- Present results through an interactive Streamlit dashboard

## Dataset

The dataset contains customer demographic, account, and engagement information, including:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Credit Card Ownership
- Active Membership Status
- Estimated Salary
- Churn Status (Exited)

## Project Workflow

1. Data Cleaning & Preparation
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Logistic Regression Modeling
5. Model Evaluation
6. Business Recommendations
7. Streamlit Dashboard Development

## Key Findings

- Germany exhibited the highest customer churn rate.
- Inactive customers were significantly more likely to churn.
- Customers aged 51–60 showed elevated churn risk.
- Product usage patterns were strongly associated with churn behavior.
- Higher-balance customers demonstrated greater churn risk.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Jupyter Notebook

## Dashboard Features

- KPI Overview
- Dataset Preview
- Churn Rate by Geography Visualization
- Business Insight Highlights

## Business Recommendations

1. Prioritize retention efforts for German customers.
2. Improve engagement strategies for inactive customers.
3. Monitor older customer segments more closely.
4. Focus retention campaigns on high-balance customers.
5. Use predictive analytics to identify at-risk customers early.

## Project Structure

<pre>
  Customer_Churn_Analytics
  │
  ├── app/
  │   └── app.py
  │
  ├── data/
  │   └── Churn_Modelling.csv
  │
  ├── images/
  │   └── dashboard_home.jpeg
  │   └── notebook_overview.jpeg
  │
  ├── notebooks/
  │   └── churn_analysis.ipynb
  │
  └── README.md
</pre>

## Future Improvements

- Deploy Streamlit dashboard online
- Add additional business visualizations
- Compare multiple machine learning models
- Enable interactive customer churn prediction

## Author

Bhargavi Shinde  
B.E. Artificial Intelligence & Data Science
