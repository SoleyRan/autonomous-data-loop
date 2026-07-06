# Development Plan

[简体中文](development-plan.zh-CN.md)

## Suggested Workstreams

| Workstream | Output |
|---|---|
| Training job model | Training job, config, status, log, artifact, and metric tables |
| Dataset consumption | Read frozen dataset manifests from Phase 3 |
| Scheduler integration | Submit training jobs to a local, container, or cluster runtime |
| Metric collection | Store overall, class, scenario, and split metrics |
| Model registry | Register model versions and artifacts |
| Model comparison | Compare baseline and candidate model metrics |

## Recommended Milestones

| Milestone | Target |
|---|---|
| M1 | Training config and training job can be created |
| M2 | Job can consume a dataset manifest and produce a mock artifact |
| M3 | Metrics can be stored and compared |
| M4 | Model card can be generated from config, dataset, and metrics |
| M5 | Registered model can be passed to Phase 5 evaluation |

## AI-Assisted Development Opportunities

- Generate training config schemas.
- Generate job state machines and mock schedulers.
- Build metric collectors and comparators.
- Generate model cards.
- Produce documentation and review checklists.

