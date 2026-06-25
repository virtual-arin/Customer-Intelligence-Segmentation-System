import joblib
import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Customer Intelligence Segmentation System",
    page_icon="📊"
)

# Load model
kmeans = joblib.load("model/kmeans_model.pkl")
scaler = joblib.load("model/scaler.pkl")

st.title("📊 Customer Intelligence Segmentation System")
st.write("Enter customer details to identify the customer segment.")

# Inputs
age = st.number_input("Age", 18, 100, 30)
income = st.number_input("Annual Income", 0, 1000000, 50000)
spending = st.number_input("Total Spending", 0, 1000000, 10000)
web_purchase = st.number_input("Web Purchases", 0, 100, 10)
store_purchase = st.number_input("Store Purchases", 0, 100, 5)
web_visit = st.number_input("Web Visits per Month", 0, 100, 20)
recency = st.number_input("Recency", 0, 1000, 50)

# Cluster names and recommendations
segment_names = {
    0: "💎 High-Value Customers",
    1: "🤝 Loyal Customers",
    2: "🛒 Moderate Spenders",
    3: "📉 Low-Engagement Customers"
}

recommendations = {
    "💎 High-Value Customers": "Offer premium memberships and exclusive rewards.",
    "🤝 Loyal Customers": "Provide personalized discounts and cross-selling offers.",
    "🛒 Moderate Spenders": "Run targeted marketing campaigns to increase spending.",
    "📉 Low-Engagement Customers": "Launch re-engagement campaigns and special coupons."
}

if st.button("Predict Segment"):

    input_data = pd.DataFrame({
        "Age": [age],
        "Income": [income],
        "Total_Spending": [spending],
        "NumWebPurchases": [web_purchase],
        "NumStorePurchases": [store_purchase],
        "NumWebVisitsMonth": [web_visit],
        "Recency": [recency]
    })

    scaled_data = scaler.transform(input_data)
    cluster = kmeans.predict(scaled_data)[0]

    segment = segment_names.get(cluster, f"Cluster {cluster}")

    st.success(f"Customer Segment: {segment}")
    st.info(f"Recommendation: {recommendations.get(segment)}")

    result = pd.DataFrame({
        "Customer Segment": [segment],
        "Income": [income],
        "Total Spending": [spending]
    })