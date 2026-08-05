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

----

## 📊 Dataset Overview
[Customer Personality Analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)

The dataset contains customer information such as age, annual income, spending behavior, purchase frequency, website interactions, and recency of purchases.

----

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-Learn
* Joblib
* Streamlit

----

## 📈 Data Visualization

1. **What is the overall distribution of customer income, and are there extreme outliers that could distort clustering?**
- **Income is mostly clustered around 50,000, but a massive outlier above 600,000 could heavily misinterpret clustering results.**
<img src="https://github.com/virtual-arin/Customer-Intelligence-Segmentation-System/blob/main/images/income_distribution_and_outlier.png" width="100%">

2. **How does spending behavior vary across product categories?**
- **Customers spend the most on wines and meats, while spending very little on fruits and sweet products.**
<img src="https://github.com/virtual-arin/Customer-Intelligence-Segmentation-System/blob/main/images/average_spending_by_product_category.png" width="100%">

3. **Are customers with higher income actually spending more?**
- **Total spending strongly increases as income grows, while a few extreme high-income outliers spend very little.**
<img src="https://github.com/virtual-arin/Customer-Intelligence-Segmentation-System/blob/main/images/income_vs_total_spending.png" width="100%">

4. **Which purchase channel is most associated with total spending?**
- **In-store purchases are the most frequent channel, then web purchases, and catalog purchases being the lowest that is contributing to purchase.**
<img src="https://github.com/virtual-arin/Customer-Intelligence-Segmentation-System/blob/main/images/average_purchase_by_channel.png" width="100%">

5. **Does recency relate to customer value and engagement?**
- **Recency shows almost no clear relationship with total spending, because recent buyers do not certainly spend more money.**
<img src="https://github.com/virtual-arin/Customer-Intelligence-Segmentation-System/blob/main/images/recency_vs_total_spending.png" width="100%">

6. **What is the distribution of marital status with respect to spending?**
- **Widows show slightly higher spending, while single and married customers have heavily lower total spending. The marital status column has some invalid data also.**
<img src="https://github.com/virtual-arin/Customer-Intelligence-Segmentation-System/blob/main/images/total_spending_by_marital_status_eda.png" width="100%">

7. **Are there distinct age groups with different purchasing patterns?**
- **Among all age group 70+ are spending the highest on average, then 60-69 and then 30-39.**
<img src="https://github.com/virtual-arin/Customer-Intelligence-Segmentation-System/blob/main/images/average_total_spending_by_age_group.png" width="100%">

8. **Do customers who accepted previous campaigns spend more or buy differently?**
- **Customers who accepted more campaigns consistently show much higher total spending than those who accept none.**
<img src="https://github.com/virtual-arin/Customer-Intelligence-Segmentation-System/blob/main/images/spending_vs_campaign_acceptance.png" width="100%">

9. **What features are highly correlated, and which may be redundant for clustering?**
- **People with higher incomes spend more money overall and buy more from catalogs and as customers tend to buy similar amounts across all product types, tracking every single category will be like repeating the same information.**
<img src="https://github.com/virtual-arin/Customer-Intelligence-Segmentation-System/blob/main/images/correalation_heatmap(EDA).png" width="100%">

10. **How do marital groups affect spending?**
- **Everyone mostly spends small amounts. widow spend the most on average. but, a few single and partnered people spend the highest amounts overall.**
<img src="https://github.com/virtual-arin/Customer-Intelligence-Segmentation-System/blob/main/images/total_spending_by_marital_status.png" width="100%">

11. **Checking distribution of some important columns to check skewness before log transformation**
- **Important columns like Income, MntWines, MntMeatProducts, MntGoldProds and Web_Visit_to_Purchase_Ratio have extreme outliers and data is right skewed. So, we will perform log transformation to reduce right skewness.**
<img src="https://github.com/virtual-arin/Customer-Intelligence-Segmentation-System/blob/main/images/distribution_of_important_columns_before_log_transformation.png" width="100%">

12. **Checking distribution of some important columns to check skewness after log transformation**
<img src="https://github.com/virtual-arin/Customer-Intelligence-Segmentation-System/blob/main/images/distribution_of_important_columns_after_log_transformation.png" width="100%">

13. **Feature Correlation Heatmap**
<img src="https://github.com/virtual-arin/Customer-Intelligence-Segmentation-System/blob/main/images/feature_correlation_heatmap.png" width="100%">

14. **Clustering Evaluation: Elbow Method and Silhouette Analysis**
<img src="https://github.com/virtual-arin/Customer-Intelligence-Segmentation-System/blob/main/images/elbow_and_silhouette_plots.png" width="100%">

15. **Customer Segmentation Analysis**
<img src="https://github.com/virtual-arin/Customer-Intelligence-Segmentation-System/blob/main/images/pca_customer_segments_k2.png" width="100%">

16. **Customer Segments**
<img src="https://github.com/virtual-arin/Customer-Intelligence-Segmentation-System/blob/main/images/customer_segments.png" width="100%">

----

### 🏆 Final Outcome 

- **Best-performing algorithm:** K-Means Clustering 
- **Optimal clusters selected:** **2** 
- **Customer segments successfully identified** 
- **Business-friendly customer profiles generated** 
- **Ready for marketing and retention strategies**

----

## 📊 Customer Segments Generated

| Customer Type | Suggested Action | 
|----------------|-----------------| 
| 💎 **Premium Customers** | High-value customer with strong engagement and purchasing behavior.
Ideal for loyalty rewards, premium bundles, and personalized recommendations. | 
| 🚨 **At-Risk Customers** | Low-value customer with browsing-oriented behavior and weaker conversion. 
Use discounts, re-engagement campaigns, and conversion-focused offers. |

----

## 🚀 Business Impact

* Enables personalized marketing campaigns.
* Improves customer targeting and retention strategies.
* Identifies high-value and at-risk customers.
* Supports data-driven decision-making.
* Enhances customer relationship management (CRM).
* Increases marketing ROI and customer lifetime value.