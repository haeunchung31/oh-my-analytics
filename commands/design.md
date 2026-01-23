# /design - Technical Approach & Methodology

**Usage**: `/design src/[project_name]/intermediate/brainstorm.md`
**Description**: Design the technical approach to test hypotheses.

## Purpose
Determines "how do we answer this?" based on the specific project context.

## Workflow Steps

### 1. **Load Brainstorm Context**
- Parse the input file at `src/[project_name]/intermediate/brainstorm.md`.
- Identify the project root `src/[project_name]/`.

### 2. **Review & Validate Hypotheses**
- Confirm testability with available data.

### 3. **Methodology Selection**
- Select appropriate methods (`skills/methodology.md`).

### 4. **Data Requirements & Validation**
- **Validation**: Use `duckdb` (or SQL) to verify data availability.
- **Reference**: Check `input/` or `sql/` within the project (or shared raw data if applicable).
- Define the "Ideal Dataset" structure.

### 5. **Output Generation**
- Create structured markdown file: `src/[project_name]/intermediate/design.md`.

## Output Format

```markdown
---
type: design
status: draft
project: [project_name]
brainstorm_ref: src/[project_name]/intermediate/brainstorm.md
---

# Technical Design: [Title]

## Hypotheses Review
...

## Data Requirements
- **Input Source**: `src/[project_name]/input/` or SQL query.

...
```

## References
- **Input**: `src/[project_name]/intermediate/brainstorm.md`
- **Output**: `src/[project_name]/intermediate/design.md`
- **Next Step**: `/analyze src/[project_name]/intermediate/design.md`
