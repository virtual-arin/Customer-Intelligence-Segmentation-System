# Customer Intelligence Segmentation System 📊

## 🛍️ Business Domain

Marketing

----

## 🤔 Problem Statement

* Businesses often struggle to understand their diverse customer base and deliver personalized marketing strategies. Treating all customers the same leads to ineffective campaigns, reduced customer engagement, and lower revenue generation.
* Accurately segmenting customers based on their demographic and purchasing behavior helps organizations identify high-value customers, improve targeting strategies, and optimize business decisions.

----

## 🎯 Project Objective

The objective of the project is to build a unsupervised machine learning system that automatically segments customers into premium and risky based on their demographic information, purchasing patterns, and engagement metrics.

## 📊 Dataset Overview
[Customer Personality Analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)

The dataset contains customer information such as age, annual income, spending behavior, purchase frequency, website interactions, and recency of purchases.


## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-Learn
* Joblib
* Streamlit

## 📈 Data Visualization



## 🔄 Workflow

### 1. Data Analysis

* Performed Exploratory Data Analysis (EDA) to understand customer behavior.
* Analyzed customer demographics and purchasing patterns.
* Identified missing values and outliers.
* Studied feature distributions and correlations.

### 2. Feature Engineering

* Selected business-relevant customer attributes.
* Created aggregated spending metrics.
* Scaled numerical features using StandardScaler and Encoded categorical features using Onehotencoder.
* Prepared data for clustering algorithms.

### 3. Model Training

Implemented and evaluated clustering techniques:

* K-Means Clustering
* Elbow Method for optimal cluster selection
* Cluster Profiling and Interpretation

### 4. Model Optimization

* Determined the optimal number of customer segments.
* Fine-tuned feature selection and preprocessing steps.

### 5. Deployment

* Saved the trained clustering model using Joblib.
* Built a Streamlit application for real-time customer segmentation and cluster prediction.

## 📈 Results Summary

| Model              | Status                  |
| ------------------ | ----------------------- |
| K-Means Clustering | 🏆 Champion Model       |
| Optimal Clusters   | Successfully Identified |
| Customer Profiling | Completed               |

## 📊 Customer Segments Generated

The system automatically groups customers into segments such as:
* High-Value Customers 💎
* Loyal Customers 🤝
* Moderate Spenders 🛒
* Low-Engagement Customers 📉
* Potential High-Value Customers 🚀

## 🚀 Business Impact

* Enables personalized marketing campaigns.
* Improves customer targeting and retention strategies.
* Identifies high-value and at-risk customers.
* Supports data-driven decision-making.
* Enhances customer relationship management (CRM).
* Increases marketing ROI and customer lifetime value.