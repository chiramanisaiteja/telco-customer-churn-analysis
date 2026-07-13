# Design & Model Decisions

## Problem Statement
Predict customer churn in a telecommunications company to identify at-risk customers and enable targeted retention strategies.

---

## Data Understanding

### Dataset
- **Source:** Telco Customer Churn Dataset (Kaggle)
- **Records:** 7,043 customers
- **Features:** 20 variables (after preprocessing)
- **Target:** Churn (binary: Yes/No)
- **Imbalance:** 26.54% churn rate

---

## Data Preprocessing Decisions

### 1. Feature Removal
- **Dropped `customerID`:** No predictive value
- **Rationale:** IDs don't generalize to new data

### 2. Handling Missing Values
- **TotalCharges:** Converted to numeric with `pd.to_numeric(..., errors='coerce')`
- **Missing rows:** Dropped 11 rows from 7,043 (minimal loss)
- **Rationale:** Cleaner than imputation for this use case

### 3. Categorical Encoding
- **Method:** One-hot encoding with `pd.get_dummies(..., drop_first=True)`
- **Why:** Prevents multicollinearity in linear models

---

## Model Selection: Logistic Regression

### Why Logistic Regression?
1. **Interpretability:** Coefficients show feature importance (key for business stakeholders)
2. **Baseline:** Established approach for binary classification
3. **Speed:** Fast training and inference
4. **Trade-off:** Lower recall (52%) vs. accuracy (78.75%) acceptable for MVP

### Performance Metrics
| Metric    | Score |
|-----------|-------|
| Accuracy  | 78.75% |
| Precision | 62%    |
| Recall    | 52%    |
| F1 Score  | 56%    |

---

## Key Business Insights (from EDA)

**Top Churn Risk Factors:**

1. **Tenure:** < 6 months = 5x higher churn
2. **Contract Type:** Month-to-month (42%) vs. 2-year (3%)
3. **Internet Service:** Fiber optic (41.8%) vs. Cable (20.5%)
4. **Payment Method:** Electronic check (45%) vs. Automatic (20%)
5. **Monthly Charges:** Higher charges → higher churn

---

## Technical Improvements (Backlog)

**P0 (Critical):**
- [ ] k-fold cross-validation
- [ ] Refactor notebook into modules
- [ ] Add unit tests

**P1 (Important):**
- [ ] SMOTE for class imbalance
- [ ] Feature engineering

**P2 (Nice-to-have):**
- [ ] Hyperparameter tuning
- [ ] Random Forest/XGBoost comparison

---

## Reproducibility

### Setup
```bash
pip install -r requirements.txt
jupyter notebook Telco_Customer_Churn_Analysis.ipynb
```

### Random Seed
- `random_state=42` for reproducibility
- ±1% variation from seed changes is normal

---

**Last updated:** 2026-07-13
**Next review:** 2026-08-13
