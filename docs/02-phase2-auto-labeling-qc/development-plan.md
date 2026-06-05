# Development Plan

[简体中文](development-plan.zh-CN.md)

## Suggested Workstreams

| Workstream | Main owner | Output |
|---|---|---|
| MCAP asset management | Backend | Metadata table, filtering API, playback entry |
| Platform UI | Frontend | MCAP list, annotation task page, QC task page, export page |
| Annotation engineering | Algorithm / engineering | Preprocessing scripts, annotation worker, output adapter |
| Xtreme1 integration | Backend / engineering | Task adapter, import/export mapping, result retrieval |
| Label and export | Backend / algorithm | Canonical label store, KITTI export, nuScenes export |

## Recommended Milestones

| Milestone | Target |
|---|---|
| M1 | MCAP assets can be filtered and replayed |
| M2 | Automated annotation can generate draft labels |
| M3 | Xtreme1 can receive QC tasks with preloaded draft labels |
| M4 | Corrected labels can return to the platform as final versions |
| M5 | Final labels can be exported to KITTI and nuScenes |

## AI-Assisted Development Opportunity

This phase is well suited for AI-agent-assisted engineering:

- Generate database schemas and API drafts.
- Build worker scripts and deployment templates.
- Implement format conversion examples.
- Generate frontend page skeletons.
- Analyze logs during integration.
- Produce release notes and validation checklists.

The expected value is not only faster coding, but also more consistent documentation and review artifacts.

