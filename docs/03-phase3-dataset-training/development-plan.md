# Development Plan

[简体中文](development-plan.zh-CN.md)

## Suggested Workstreams

| Workstream | Output |
|---|---|
| Dataset entity model | Dataset, dataset version, sample, split, manifest, lineage tables |
| Sample index builder | Build reusable sample indexes from frozen labels and MCAP metadata |
| Dataset creation API | Create draft datasets, add filters, generate versions |
| Split service | Generate deterministic train/validation/test splits |
| Statistics service | Produce class, frame, split, and scenario statistics |
| Manifest service | Generate dataset manifests for downstream jobs |

## Recommended Milestones

| Milestone | Target |
|---|---|
| M1 | Dataset version entity and sample index can be created |
| M2 | Dataset split and statistics can be generated |
| M3 | Dataset manifest can be exported and consumed by demo tools |
| M4 | Dataset lineage can link back to MCAP and label versions |

## AI-Assisted Development Opportunities

- Generate database schemas and migration drafts.
- Generate manifest builders and validators.
- Create deterministic split scripts.
- Produce quality-statistics scripts.
- Generate API examples and documentation.

