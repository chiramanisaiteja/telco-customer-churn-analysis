# 📊 Telco Customer Churn Analysis

## Project Overview

This project focuses on analyzing customer churn patterns in a telecommunications company using **Python, Machine Learning, and Power BI**. The primary goal is to identify factors driving customer churn and provide actionable retention strategies.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Jupyter Notebook
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/chiramanisaiteja/telco-customer-churn-analysis.git
   cd telco-customer-churn-analysis
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the analysis:**
   ```bash
   jupyter notebook Telco_Customer_Churn_Analysis.ipynb
   ```

5. **Execute all cells:**
   - In Jupyter: `Kernel → Restart & Run All`

---

## Dataset Information

* **Dataset:** Telco Customer Churn Dataset
* **Total Records:** 7,043 customers
* **Features:** 20 variables (after preprocessing)
* **Target Variable:** Churn (binary: Yes/No)
* **Churn Rate:** 26.54%

---

## Data Preprocessing

The dataset was cleaned and prepared for analysis:

* Removed the `customerID` column (no predictive value)
* Converted `TotalCharges` to numeric data type
* Handled missing values (dropped 11 rows with NaN)
* Encoded categorical variables using one-hot encoding
* Removed 22 duplicate rows

**See [`DECISIONS.md`](DECISIONS.md) for detailed rationale on preprocessing steps.**

---

## Exploratory Data Analysis (EDA)

Key insights from the analysis:

* **Overall churn rate:** 26.54%
* **Month-to-month contracts** show highest churn rates (42%)
* **Fiber optic internet users** have 41.8% churn vs. 20.5% for Cable
* **Electronic check** payment method shows 45% churn
* **Higher monthly charges** correlate with increased churn
* **Shorter tenure** (<6 months) = 5x higher churn risk

---

## Machine Learning Model

### Model Used: Logistic Regression

**Why Logistic Regression?**
- Interpretable coefficients for business stakeholders
- Established baseline for binary classification
- Fast training and inference
- Good balance of performance vs. complexity

### Model Performance

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 78.75% |
| Precision | 62%    |
| Recall    | 52%    |
| F1 Score  | 56%    |

**Interpretation:**
- 78.75% of predictions are correct
- 62% of predicted churners actually churn (low false positive rate)
- Catches 52% of actual churners (can improve with SMOTE)

---

## Power BI Dashboard

### Page 1: Executive Overview
High-level business performance metrics:
- Total Customers & Churned Customers
- Churn Rate & Average Monthly Charges
- Contract Type vs Churn Analysis
- Internet Service vs Churn Analysis
- Payment Method vs Churn Analysis

### Page 2: Customer Behavior Analysis
Customer demographic patterns:
- Gender vs Churn
- Senior Citizen Status vs Churn
- Partner Status vs Churn
- Monthly Charges vs Churn
- Tenure vs Churn

*Dashboard visualizations included: See `dashboard_page1.png` and `dashboard_page2.png`*

---

## Business Recommendations

Based on the analysis:

1. **Encourage long-term contracts** through targeted incentives (reduces churn from 42% to 3%)
2. **Implement early onboarding programs** (first 6 months critical for retention)
3. **Investigate Fiber Optic service quality** (41.8% churn rate suggests issues)
4. **Promote automatic payments** (reduces churn from 45% to 20%)
5. **Develop loyalty programs** for high-risk segments (high charges, short tenure)

---

## Technologies Used

* **Python** — Data analysis & modeling
* **Pandas** — Data manipulation
* **NumPy** — Numerical computations
* **Matplotlib & Seaborn** — Visualizations
* **Scikit-Learn** — Machine learning
* **Jupyter** — Interactive notebooks
* **Power BI** — Business dashboards
* **GitHub** — Version control

---

## Project Structure

```
telco-customer-churn-analysis/
├── README.md                           # This file
├── DECISIONS.md                        # Model & design decisions
├── CONTRIBUTING.md                     # Development guidelines
├── requirements.txt                    # Dependencies
├── .gitignore                          # Git ignore rules
├── Telco-Customer-Churn.csv           # Dataset
├── Telco_Customer_Churn_Analysis.ipynb # Main analysis notebook
├── Telco_Churn_Dashboard.pbix         # Power BI dashboard
├── dashboard_page1.png                # Dashboard screenshot 1
└── dashboard_page2.png                # Dashboard screenshot 2
```

---

## Reproducibility

### How to Reproduce Results
```bash
pip install -r requirements.txt
jupyter notebook Telco_Customer_Churn_Analysis.ipynb
# Run: Kernel → Restart & Run All
```

### Random Seed
- `random_state=42` used throughout for reproducibility
- Slight variations (±1%) normal when changing seeds

---

## Future Improvements

**High Priority:**
- [ ] Implement k-fold cross-validation
- [ ] Apply SMOTE for class imbalance handling
- [ ] Refactor notebook into reusable modules (`src/` directory)
- [ ] Add unit tests for preprocessing & model validation

**Medium Priority:**
- [ ] Try Random Forest & XGBoost for comparison
- [ ] Hyperparameter tuning with GridSearchCV
- [ ] Feature engineering (interaction terms, polynomial features)

**Nice-to-have:**
- [ ] Model versioning & experiment tracking
- [ ] Automated data pipeline & retraining schedule
- [ ] REST API for model predictions
- [ ] Docker containerization

**See [`DECISIONS.md`](DECISIONS.md) for detailed technical backlog.**

---

## Contributing

We welcome contributions! Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines on:
- Development workflow
- Code style standards
- Testing requirements
- Commit message conventions

---

## License

This project is open source and available for portfolio and educational purposes.

---

## Project Outcome

This project demonstrates the use of **data analytics, machine learning, and business intelligence tools** to understand customer behavior, predict churn, and generate data-driven recommendations. It showcases a complete end-to-end ML workflow from data preprocessing through model evaluation and business insights.

---

**Last updated:** July 13, 2026

For questions or issues, please open a GitHub Issue or Discussion.
