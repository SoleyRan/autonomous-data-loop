# Dataset Manifest Builder Demo

[简体中文](README.zh-CN.md)

This demo builds a small dataset manifest from a sample index and deterministic split configuration.

It demonstrates the Phase 3 idea: dataset versions should be reproducible artifacts with explicit samples, splits, and statistics.

## Run

```powershell
python build_dataset_manifest.py `
  ..\..\examples\metadata\dataset-sample-index.example.json `
  ..\..\examples\manifest\phase3-split-config.example.json
```

