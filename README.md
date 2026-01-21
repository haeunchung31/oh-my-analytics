# Agentic Analytics

A repository for data analysis and modeling workflows, designed to facilitate hypothesis generation, testing, and reporting.

## Overview
This project provides a structured, agentic approach to business analytics:
- **Agents**: Specialized personas:
    - `orchestrator`: Oversees the workflow, delegates tasks, and synthesizes final outputs.
    - `strategist`: Frames business questions and generates hypotheses.
    - `ds` (Data Scientist): Performs statistical analysis and modeling.
    - `de` (Data Engineer): Fetches data via SQL.
- **Skills**: Executable workflows and methodologies (`workflow.md`, `methodology.md`, `reporting.md`).
- **Knowledge Base**: Business glossary and schema context.

## Setup
1. Install dependencies: `uv sync`
2. Configure credentials in `.env`
3. Run the main orchestrator: `uv run python main.py`

## Structure
- `agents/`: Definitions of AI agents (`orchestrator.md`, `strategist.md`, `ds.md`, `de.md`).
- `skills/`: Reusable analysis capabilities (`workflow.md`, `methodology.md`, `reporting.md`).
- `rules/`: Global mandates (Security, Privacy).
- `knowledge_base/`: Business and data context.
