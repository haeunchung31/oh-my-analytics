# %% Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_context("talk")

# %% Load data
data_path = Path('input/credit_risk_dataset.csv')
df = pd.read_csv(data_path)

# %% Basic profiling
print("Dataset shape:", df.shape)
print("\nData types:")
print(df.dtypes)
print("\nNull counts:")
print(df.isnull().sum())
print("\nUnique values in categorical columns:")
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"{col}: {df[col].nunique()} unique values")

# %% Summary statistics
print("\nSummary statistics for numerical columns:")
numerical_cols = df.select_dtypes(include=[np.number]).columns
print(df[numerical_cols].describe())

# %% Visualizations
output_dir = Path('output')
output_dir.mkdir(exist_ok=True)

# Histograms for numerical columns
fig, axes = plt.subplots(3, 3, figsize=(15, 12))
numerical_cols = ['person_age', 'person_income', 'person_emp_length', 'loan_amnt', 'loan_int_rate', 'loan_percent_income', 'cb_person_cred_hist_length']
for i, col in enumerate(numerical_cols):
    ax = axes.flat[i]
    df[col].hist(bins=30, ax=ax)
    ax.set_title(f'Histogram of {col}')
    ax.set_xlabel(col)
    ax.set_ylabel('Frequency')
plt.tight_layout()
plt.savefig(output_dir / 'histograms.png', dpi=150, bbox_inches='tight')
plt.show()

# Count plots for categorical columns
categorical_cols = ['person_home_ownership', 'loan_intent', 'loan_grade', 'loan_status', 'cb_person_default_on_file']
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
for i, col in enumerate(categorical_cols):
    ax = axes.flat[i]
    sns.countplot(data=df, x=col, ax=ax)
    ax.set_title(f'Count of {col}')
    ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.savefig(output_dir / 'countplots.png', dpi=150, bbox_inches='tight')
plt.show()

# Correlation heatmap
corr = df.select_dtypes(include=[np.number]).corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.savefig(output_dir / 'correlation_heatmap.png', dpi=150, bbox_inches='tight')
plt.show()

# Scatter plot for loan_status vs some key variables
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
key_vars = ['person_age', 'person_income', 'loan_amnt', 'loan_int_rate']
for i, var in enumerate(key_vars):
    ax = axes.flat[i]
    sns.scatterplot(data=df, x=var, y='loan_status', ax=ax, alpha=0.6)
    ax.set_title(f'Loan Status vs {var}')
plt.tight_layout()
plt.savefig(output_dir / 'scatter_plots.png', dpi=150, bbox_inches='tight')
plt.show()

# %% Output summary
print("\nEDA Summary:")
print("- Dataset has", df.shape[0], "rows and", df.shape[1], "columns.")
print("- Numerical columns:", list(numerical_cols))
print("- Categorical columns:", list(categorical_cols))
print("- Null values present in:", df.columns[df.isnull().any()].tolist())
print("- Plots saved to output/ directory.")
