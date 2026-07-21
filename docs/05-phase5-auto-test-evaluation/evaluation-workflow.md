# Evaluation Workflow

[简体中文](evaluation-workflow.zh-CN.md)

## Main Workflow

```mermaid
sequenceDiagram
  participant U as User
  participant P as Platform
  participant D as Dataset Store
  participant R as Runtime
  participant M as Metric Service
  participant O as Report Store

  U->>P: Select dataset and model version
  U->>P: Create evaluation job
  P->>D: Resolve manifest and frozen labels
  P->>R: Start replay and perception runtime
  R->>P: Upload prediction records and logs
  P->>M: Compare predictions with labels
  M->>O: Save metrics, failed cases, and report
  U->>P: Review report and regression cases
```

## Evaluation Job States

```mermaid
stateDiagram-v2
  [*] --> Created
  Created --> Preparing
  Preparing --> Running
  Running --> CollectingOutputs
  CollectingOutputs --> ComputingMetrics
  ComputingMetrics --> ReportReady
  Running --> Failed
  Preparing --> Failed
  ComputingMetrics --> Failed
```

## Required Inputs

- Dataset version.
- Frozen label version.
- Model or perception software version.
- Runtime configuration.
- Metric configuration.

## Required Outputs

- Prediction records.
- Runtime logs.
- Metric summary.
- Failed cases.
- Evaluation report.
- Feedback candidates.

