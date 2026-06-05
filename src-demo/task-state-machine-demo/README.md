# Phase 2 Task State Machine Demo

[简体中文](README.zh-CN.md)

This demo shows a simplified state machine for Phase 2 annotation, quality inspection, and export tasks.

It is intentionally small and public-safe. It is not production code.

## Run

```powershell
python phase2_state_machine.py
```

## Covered Flow

```text
created -> preprocessing -> annotating -> draft_ready -> qc_in_progress -> final_ready -> frozen -> exported
```

