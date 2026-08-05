import joblib
import streamlit as st
import pandas as pd
import numpy as np

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Customer Intelligence Segmentation System",
    page_icon="📊",
    layout="centered"
)

# -----------------------------
# Load saved objects
# -----------------------------
preprocessor = joblib.load("model/preprocessor.pkl")
kmeans = joblib.load("model/customer_segmentation_model.pkl")

# -----------------------------
# Title
# -----------------------------
st.title("📊 Customer Intelligence Segmentation System")
st.markdown("Predict whether a customer belongs to the **Premium Engaged** or **Browsing Low-Value** segment.")

# -----------------------------
# Input form
# -----------------------------
with st.form("customer_form"):

    age = st.number_input("Age", 18, 100, 35)
    income = st.number_input("Annual Income", 0.0, 1000000.0, 60000.0)

    col1, col2, col3 = st.columns(3)

    with col1:
        mnt_wines = st.number_input("Wine Spending", 0.0, 100000.0, 500.0)

    with col2:
        mnt_meat = st.number_input("Meat Spending", 0.0, 100000.0, 300.0)

    with col3:
        mnt_gold = st.number_input("Gold Spending", 0.0, 100000.0, 100.0)

    col4, col5, col6 = st.columns(3)

    with col4:
        num_web = st.number_input("Web Purchases", 0, 100, 5)

    with col5:
        num_catalog = st.number_input("Catalog Purchases", 0, 100, 2)

    with col6:
        num_store = st.number_input("Store Purchases", 0, 100, 7)

    web_visits = st.number_input("Web Visits per Month", 0, 100, 5)
    recency = st.number_input("Recency (days since last purchase)", 0, 365, 30)
    tenure = st.number_input("Customer Tenure (days)", 0, 5000, 365)
    children = st.number_input("Total Children", 0, 10, 1)

    education = st.selectbox(
        "Education",
        ["Basic", "2n Cycle", "Graduation", "Master", "PhD"]
    )

    marital_status = st.selectbox(
        "Marital Status",
        ["Single", "Married", "Together", "Divorced", "Widow"]
    )

    submitted = st.form_submit_button("Predict Segment")

# -----------------------------
# Prediction
# -----------------------------
if submitted:

    total_purchases = num_web + num_catalog + num_store
    total_spending = mnt_wines + mnt_meat + mnt_gold

    ratio = web_visits / total_purchases if total_purchases > 0 else 0

    # Apply SAME transformations used during training
    input_df = pd.DataFrame({
        "Education": [education],
        "Marital_Status": [marital_status],
        "Income": [np.log1p(income)],
        "Recency": [recency],
        "MntWines": [np.log1p(mnt_wines)],
        "MntMeatProducts": [np.log1p(mnt_meat)],
        "MntGoldProds": [np.log1p(mnt_gold)],
        "NumDealsPurchases": [0],
        "NumWebPurchases": [num_web],
        "NumCatalogPurchases": [num_catalog],
        "NumStorePurchases": [num_store],
        "NumWebVisitsMonth": [web_visits],
        "Age": [age],
        "Customer_Tenure_Days": [tenure],
        "Total_Children": [children],
        "Web_Visit_to_Purchase_Ratio": [np.log1p(ratio)]
    })

    # Transform and predict
    X_processed = preprocessor.transform(input_df)
    cluster = kmeans.predict(X_processed)[0]

    # Segment names
    segment_names = {
        0: "💎 Premium Customer",
        1: "🚨 Risky Customer"
    }

    segment = segment_names[cluster]

    # -----------------------------
    # Result display
    # -----------------------------
    if cluster == 0:

        st.success(f"Customer Type: **{segment}**")

        st.info(
            "High-value customer with strong engagement and purchasing behavior. "
            "Ideal for loyalty rewards, premium bundles, and personalized recommendations."
        )

    else:

        st.error(f"Customer Type: **{segment}**")

        st.warning(
            "Low-value customer with browsing-oriented behavior and weaker conversion. "
            "Use discounts, re-engagement campaigns, and conversion-focused offers."
        )
