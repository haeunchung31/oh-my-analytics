# /analyze - Analysis Execution

**Usage**: `/analyze src/[project_name]/intermediate/design.md`
**Description**: Execute the technical plan.

## Purpose
Run the analysis using scripts within the project directory.

## Workflow Steps

### 1. **Load Design Context**
- Read `src/[project_name]/intermediate/design.md`.
- Determine paths for input (`src/[project_name]/input/`) and output (`src/[project_name]/output/`).

### 2. **Data Acquisition & Prep**
- Write `src/[project_name]/01_data_prep.py`.
- Load data from `input/` or execute SQL from `sql/`.

### 3. **Hypothesis Testing Execution**
- Write analysis scripts (e.g., `src/[project_name]/02_analysis.py`).
- Save plots to `src/[project_name]/output/figures/`.
- Save results to `src/[project_name]/output/results.json`.

### 4. **Output Results**
- Generate `src/[project_name]/intermediate/analysis_results.md`.

## Output Format

```markdown
---
type: analysis
status: complete
project: [project_name]
---

# Analysis Results

## Artifacts
- **Code**: `src/[project_name]/*.py`
- **Data**: `src/[project_name]/output/...`
...
```

## References
- **Input**: `src/[project_name]/intermediate/design.md`
- **Output**: `src/[project_name]/intermediate/analysis_results.md`
- **Next Step**: `/report src/[project_name]/intermediate/analysis_results.md`
