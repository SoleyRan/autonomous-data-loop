# Development Plan

[简体中文](development-plan.zh-CN.md)

## Suggested Workstreams

| Workstream | Output |
|---|---|
| Evaluation entity model | Job, runtime config, prediction, metric, report, failed-case tables |
| Dataset and model binding | Resolve dataset versions and model versions from previous phases |
| Replay worker | Run replay from MCAP or derived samples |
| Runtime adapter | Start and monitor target perception runtime |
| Metric service | Compare predictions with canonical labels |
| Report service | Generate reports and feedback candidates |

## Recommended Milestones

| Milestone | Target |
|---|---|
| M1 | Evaluation job can be created from dataset and model versions |
| M2 | Replay and runtime adapter can produce prediction records |
| M3 | Metric service can generate summary and failed cases |
| M4 | Evaluation report can be exported as JSON/Markdown |
| M5 | Failed cases can be passed to Phase 6 feedback workflow |

## AI-Assisted Development Opportunities

- Generate evaluation job state machines.
- Generate metric comparator scripts.
- Generate report templates.
- Analyze failed cases and logs.
- Produce regression summaries and release review notes.

