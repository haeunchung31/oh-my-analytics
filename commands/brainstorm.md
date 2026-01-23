# /brainstorm - Problem Definition & Hypothesis Formation

**Usage**: `/brainstorm [project_name]`
**Description**: Define the business question and hypotheses for an existing project.

## Purpose
Focuses purely on **problem definition**—clarifying "what are we trying to answer?". 
**Pre-requisite**: Project must be initialized via `/initialize [project_name]`.

## Workflow Steps

### 1. **Gather Context**
- Collect all snippets, notes, stakeholder comments, and background information.
- Identify the business function or domain.

### 2. **Iterative Question Refinement**
- Ask clarifying questions to sharpen the business question:
  - "What decision will this analysis inform?"
  - "What would a successful answer look like?"
- Continue until the question is **specific, measurable, and actionable**.

### 3. **Hypothesis Formation**
- Generate initial hypotheses based on domain knowledge.
- Each hypothesis must be falsifiable and tied to a metric.

### 4. **Output Generation**
- Create structured markdown file: `src/[project_name]/intermediate/brainstorm.md`
- Use `write_to_file` to save.

## Output Format

```markdown
---
type: brainstorm
status: draft
created: YYYY-MM-DD
project: [project_name]
---

# [Descriptive Title]

## Key Question(s)
... 
```

## References
- **Input**: User context / conversation
- **Output**: `src/[project_name]/intermediate/brainstorm.md`
- **Next Step**: `/design src/[project_name]/intermediate/brainstorm.md`
- **Agents**: Invokes `agents/strategist.md` and `agents/orchestrator.md`
