# Project Structure & Naming

## Directory Layout
Standard structure for all analytics projects:

```
src/[project-id]/
├── sql/                # SQL query files
├── input/              # CSV or Parquet data files (Read-Only)
├── output/             # Result files (PNG, CSV, HTML)
├── report/             # Task reports
├── intermediate/       # Brainstorm and Design docs
└── *.py                # Reproducible Python scripts at root
```

## File Naming
- **Scripts**: `snake_case.py` (e.g., `churn_analysis.py`).
- **Parallel Tasks**: `XX_description.py` (e.g., `01_distribution.py`).
- **Data**: `snake_case.csv`.
- **Images**: `snake_case.png` (include variable name if possible).

## Script Standards
- **Interactive**: Always use `# %%` for cells.
- **Output**: Save artifacts to `output/`.
