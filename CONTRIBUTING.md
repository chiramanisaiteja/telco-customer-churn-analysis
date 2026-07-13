# Contributing to Telco Customer Churn Analysis

## Overview
This is a portfolio data science project showcasing end-to-end ML workflow. Contributions are welcome to improve model performance, add features, or enhance documentation.

---

## Development Workflow

### 1. Fork & Clone
```bash
git clone https://github.com/chiramanisaiteja/telco-customer-churn-analysis.git
cd telco-customer-churn-analysis
```

### 2. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
git checkout -b refactor/code-section
```

### 3. Set Up Local Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Make Changes
- Edit notebook or create new modules in `src/`
- Test locally: run notebook or `pytest tests/`
- Keep commits atomic and descriptive

### 5. Commit with Conventional Messages
Follow [Conventional Commits](https://www.conventionalcommits.org/):

```bash
git commit -m "feat: add SMOTE for class imbalance handling"
git commit -m "fix: correct TotalCharges data type conversion"
git commit -m "refactor: extract preprocessing logic into module"
git commit -m "docs: update README with setup instructions"
git commit -m "test: add validation for model accuracy baseline"
```

**Commit message format:**
```
<type>(<scope>): <subject>

<body (optional)>

<footer (optional)>
```

**Valid types:**
- `feat:` new feature or capability
- `fix:` bug fix
- `refactor:` code restructuring (no behavior change)
- `docs:` documentation updates
- `test:` test additions or fixes
- `perf:` performance optimization
- `chore:` build, dependencies, tooling

**Examples:**
```bash
git commit -m "feat(model): implement XGBoost classifier"
git commit -m "fix(eda): correct chart labels in analysis"
git commit -m "docs(readme): add reproducibility section"
```

### 6. Push & Open Pull Request
```bash
git push origin feature/your-feature-name
```

Then open a PR on GitHub with:
- **Title:** Clear, concise summary
- **Description:** What problem does it solve? How was it tested?
- **Related issues:** Link to any relevant GitHub issues

**PR template:**
```markdown
## Description
Brief explanation of changes.

## Type of Change
- [ ] New feature
- [ ] Bug fix
- [ ] Refactoring
- [ ] Documentation update

## How to Test
Steps to verify the changes work correctly.

## Checklist
- [ ] Code follows style guidelines
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No new warnings generated
```

---

## Code Style & Quality

### Python Style Guide
- Follow [PEP 8](https://pep8.org/)
- Use **2-space indentation** (Jupyter default)
- Max line length: **100 characters**
- Use descriptive variable names (avoid `x`, `y`, `tmp`)

### Notebook Best Practices
- Add markdown headers to organize cells
- Use meaningful cell labels and comments
- Clear outputs before committing
- One analysis/concept per notebook section

### Example: Well-Structured Cell
```python
# Data Preprocessing
# Remove columns, handle missing values, encode categoricals

import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/Telco-Customer-Churn.csv")
df.drop('customerID', axis=1, inplace=True)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)

print(f"Processed data shape: {df.shape}")
print(f"Data types:\n{df.dtypes}")
```

---

## Testing

### Running Tests
```bash
pip install pytest
pytest tests/ -v                    # Run all tests
pytest tests/test_preprocessing.py  # Run specific test file
pytest tests/ -k "test_accuracy"    # Run tests matching pattern
```

### Writing Tests
Place test files in `tests/` directory with naming: `test_*.py`

**Example: `tests/test_model.py`**
```python
import pytest
from src.model import train_logistic_regression

def test_model_trains_successfully():
    """Model should train without errors."""
    model, metrics = train_logistic_regression()
    assert model is not None

def test_accuracy_meets_baseline():
    """Model accuracy should be >= 75%."""
    model, metrics = train_logistic_regression()
    assert metrics['accuracy'] >= 0.75

def test_metrics_contain_required_keys():
    """Metrics dict should have all required keys."""
    model, metrics = train_logistic_regression()
    required_keys = {'accuracy', 'precision', 'recall', 'f1'}
    assert required_keys.issubset(metrics.keys())
```

### Test Coverage Goal
- Aim for >70% code coverage for critical functions
- Test edge cases (empty data, missing values, extreme values)
- Use fixtures for repeated test data

---

## Documentation

### README.md
Update if you:
- Add new features or datasets
- Change setup instructions
- Improve model performance significantly
- Add new analysis sections

### DECISIONS.md
Update if you:
- Change model selection rationale
- Add new preprocessing steps
- Identify new business insights
- Update technical debt backlog

### Docstrings
All functions should have docstrings:
```python
def load_and_preprocess(filepath: str) -> pd.DataFrame:
    """
    Load Telco dataset and apply preprocessing.
    
    Args:
        filepath: Path to CSV file
        
    Returns:
        Cleaned DataFrame ready for modeling
        
    Raises:
        FileNotFoundError: If filepath doesn't exist
    """
    pass
```

---

## Common Contribution Types

### 🎯 Improving Model Performance
1. Try new algorithm (XGBoost, Random Forest, SVM)
2. Implement hyperparameter tuning
3. Apply SMOTE for class imbalance
4. Add feature engineering

**PR checklist:**
- [ ] New model accuracy is better than baseline (78.75%)
- [ ] Cross-validation scores reported
- [ ] Tests added to validate new metrics
- [ ] DECISIONS.md updated with rationale

### 📊 Enhancing Analysis
1. Add new EDA visualizations
2. Discover additional business insights
3. Analyze specific customer segments

**PR checklist:**
- [ ] Visualizations are clear and labeled
- [ ] Insights are actionable for business
- [ ] README updated with new findings

### 🔧 Refactoring Code
1. Extract functions from notebook
2. Improve code organization
3. Reduce duplication

**PR checklist:**
- [ ] Functionality unchanged (same outputs)
- [ ] Tests pass
- [ ] Code is more readable/maintainable

### 📝 Documentation
1. Improve README clarity
2. Add API documentation
3. Create tutorials or guides

**PR checklist:**
- [ ] Grammar/spelling correct
- [ ] Examples work as shown
- [ ] Links are valid

---

## Reporting Issues

Use GitHub Issues to report bugs or suggest features.

**Bug report template:**
```markdown
## Description
Clear description of the bug.

## Steps to Reproduce
1. Step one
2. Step two
3. Bug occurs

## Expected Behavior
What should happen

## Actual Behavior
What actually happened

## Environment
- Python version: 3.9
- OS: macOS / Windows / Linux
```

**Feature request template:**
```markdown
## Description
Brief description of desired feature.

## Use Case
Why is this feature needed?

## Example Implementation
Any code examples or mockups.
```

---

## Getting Help

- **Questions?** Open a GitHub Discussion
- **Stuck?** Check existing issues/PRs for similar problems
- **Review feedback?** Respond to PR comments, ask for clarification

---

## Code Review Guidelines

### For Authors
- Keep PRs focused (one feature per PR)
- Write clear commit messages
- Respond to feedback promptly
- Run tests before submitting

### For Reviewers
- Provide constructive, specific feedback
- Approve once quality criteria met
- Merge when approved and CI passes

---

## Merge Criteria

Your PR is ready to merge when:
- ✅ All tests pass (`pytest`)
- ✅ Code follows style guidelines
- ✅ At least 1 approval review
- ✅ No merge conflicts
- ✅ Documentation updated (if needed)

---

**Thank you for contributing! 🚀**
