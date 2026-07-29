# Feedback Workflow

[简体中文](feedback-workflow.zh-CN.md)

## Main Workflow

```mermaid
sequenceDiagram
  participant E as Evaluation
  participant F as Feedback Platform
  participant R as Rule Planner
  participant C as Collection Runtime
  participant D as Data Loop
  participant M as Model Iteration

  E->>F: Submit failed cases and weak metrics
  F->>F: Normalize case records
  F->>F: Group cases by scenario and error type
  F->>R: Create scenario data requirement
  R->>F: Propose probe rule update
  F->>F: Review priority and validity
  F->>C: Publish approved collection task
  C->>D: Produce new MCAP assets
  D->>M: Annotation, dataset, training, and evaluation
  M->>F: Report outcome metrics
```

## Feedback States

```mermaid
stateDiagram-v2
  [*] --> CaseCreated
  CaseCreated --> Grouped
  Grouped --> RequirementCreated
  RequirementCreated --> RuleProposed
  RuleProposed --> Approved
  RuleProposed --> Rejected
  Approved --> Collecting
  Collecting --> DataReturned
  DataReturned --> DownstreamProcessed
  DownstreamProcessed --> OutcomeMeasured
```

## Required Inputs

- Failed cases from Phase 5.
- Weak metrics from Phase 4 or Phase 5.
- Source data and label lineage.
- Scenario tags and error types.
- Collection constraints.

## Required Outputs

- Scenario data requirement.
- Probe rule update proposal.
- Targeted collection task.
- Feedback outcome report.

