# Training Workflow

[简体中文](training-workflow.zh-CN.md)

## Main Workflow

```mermaid
sequenceDiagram
  participant U as User
  participant P as Platform
  participant D as Dataset Store
  participant S as Scheduler
  participant R as Runtime
  participant M as Model Registry

  U->>P: Select frozen dataset version
  U->>P: Select training configuration
  P->>D: Load dataset manifest
  P->>S: Submit training job
  S->>R: Start training runtime
  R->>D: Read dataset manifest and samples
  R->>P: Stream logs and metrics
  R->>M: Upload model artifact
  P->>M: Register model version and lineage
  U->>P: Review metrics and compare versions
```

## Training Job States

```mermaid
stateDiagram-v2
  [*] --> Created
  Created --> Queued
  Queued --> Running
  Running --> Succeeded
  Running --> Failed
  Running --> Cancelled
  Succeeded --> Registered
  Registered --> ReadyForEvaluation
```

## Required Inputs

| Input | Description |
|---|---|
| Dataset manifest | Frozen dataset version from Phase 3 |
| Training config | Model architecture, hyperparameters, runtime, and output rules |
| Runtime image | Container or environment version |
| Code version | Git commit, package version, or release ID |

## Required Outputs

| Output | Description |
|---|---|
| Model artifact | Checkpoint, exported model, or runtime package |
| Metrics | Training, validation, and scenario-level metrics |
| Logs | Runtime logs and failure reason |
| Model card | Human-readable summary of lineage, metrics, and readiness |

