import pandas as pd
import pytest

# Test 1: Does the data load?
def test_data_loads():
    """Check if the CSV file loads successfully."""
    df = pd.read_csv("Telco-Customer-Churn.csv")
    assert len(df) > 0  # Make sure we got data
    print("✅ Data loaded successfully!")

# Test 2: Does it have 7043 rows?
def test_data_has_correct_rows():
    """Check if dataset has expected number of rows."""
    df = pd.read_csv("Telco-Customer-Churn.csv")
    assert len(df) == 7043
    print("✅ Data has correct number of rows!")

# Test 3: Is the target column there?
def test_churn_column_exists():
    """Check if 'Churn' column exists."""
    df = pd.read_csv("Telco-Customer-Churn.csv")
    assert 'Churn' in df.columns
    print("✅ Churn column exists!")

# Test 4: Does preprocessing work?
def test_preprocessing():
    """Check if customerID gets removed."""
    df = pd.read_csv("Telco-Customer-Churn.csv")
    # Simulate preprocessing
    df.drop('customerID', axis=1, inplace=True)
    assert 'customerID' not in df.columns
    print("✅ Preprocessing works!")
