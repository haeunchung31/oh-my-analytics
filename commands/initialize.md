# /initialize - Project Setup

**Usage**: `/initialize [project_name]`
**Description**: Create the standard directory structure for a new analytics project.

## Purpose
Establishes the standard folder layout to ensure consistency across all projects. This must be run **once** before any other commands for a new project.

## Workflow Steps

### 1. **Validate Name**
- Ensure `[project_name]` is valid (snake_case recommended, no spaces).

### 2. **Create Directories**
- Generate the following structure under `src/[project_name]/`:
  ```
  src/[project_name]/
  ├── input/          # Read-only data files
  ├── output/         # Analysis results and artifacts
  │   └── figures/    # Plots and charts
  ├── intermediate/   # Brainstorm and Design documents
  ├── report/         # Final Korean reports
  └── sql/            # SQL query files
  ```

### 3. **Validation**
- Verify confirm directories were created successfully.

## Output
- **Console**: "Project `[project_name]` initialized at `src/[project_name]/`."

## References
- **Next Step**: `/brainstorm [project_name]`
- **Structure Rule**: `rules/structure.md`
