# 📊 Telco Customer Churn Analysis

## Project Overview

This project focuses on analyzing customer churn patterns in a telecommunications company using **Python, Machine Learning, and Power BI**. The primary goal is to identify the factors that contribute to customer churn and provide actionable business insights to improve customer retention.

---

## Dataset Information

* **Dataset:** Telco Customer Churn Dataset
* **Total Records:** 7,043 customers
* **Features:** 21 variables
* **Target Variable:** Churn

---

## Data Preprocessing

The dataset was cleaned and prepared for analysis using the following steps:

* Removed the `customerID` column as it does not contribute to prediction.
* Converted the `TotalCharges` column to a numeric data type.
* Handled missing values and data inconsistencies.
* Encoded categorical variables for machine learning models.
* Prepared the dataset for training and evaluation.

---

## Exploratory Data Analysis (EDA)

Key insights obtained from the analysis include:

* The overall customer churn rate is **26.54%**.
* Customers with **month-to-month contracts** show the highest churn rates.
* **Fiber optic internet users** are more likely to churn compared to other internet service users.
* Customers using **electronic check** as a payment method have a higher tendency to leave.
* Higher **monthly charges** are associated with increased churn.
* Customers with **shorter tenure** are more likely to discontinue services.

---

## Machine Learning Model

### Model Used

* Logistic Regression

### Model Performance

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 78.75% |
| Precision | 62%    |
| Recall    | 52%    |
| F1 Score  | 56%    |

The Logistic Regression model was used to predict customer churn and evaluate the impact of various customer attributes on retention.

---

## Power BI Dashboard

### Page 1: Executive Overview

The executive dashboard provides a high-level summary of business performance, including:

* Total Customers
* Churned Customers
* Churn Rate
* Average Monthly Charges
* Average Customer Tenure
* Contract Type vs Churn Analysis
* Internet Service vs Churn Analysis
* Payment Method vs Churn Analysis

### Page 2: Customer Behavior Analysis

This page focuses on customer demographics and behavioral patterns:

* Gender vs Churn
* Senior Citizen vs Churn
* Partner Status vs Churn
* Monthly Charges vs Churn
* Tenure vs Churn

---

## Business Recommendations

Based on the analysis, the following recommendations are proposed:

* Encourage customers to switch to long-term contracts through targeted incentives.
* Implement retention programs focused on newly acquired customers.
* Investigate potential service quality issues among Fiber Optic customers.
* Promote automatic payment methods to reduce churn risk.
* Develop loyalty and engagement programs for high-risk customer segments.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Power BI
* GitHub

---

## Project Outcome

This project demonstrates the use of **data analytics, machine learning, and business intelligence tools** to understand customer behavior, predict churn, and generate data-driven recommendations that support customer retention strategies.
