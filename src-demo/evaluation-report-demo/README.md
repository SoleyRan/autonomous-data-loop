# Evaluation Report Demo

[简体中文](README.zh-CN.md)

This demo compares a simplified canonical label file with perception outputs and generates an evaluation report.

It demonstrates the Phase 5 idea: automated evaluation should compare immutable predictions with frozen labels and produce metrics plus failed cases.

## Run

```powershell
python build_evaluation_report.py `
  ..\..\examples\label-format\canonical-label.example.json `
  ..\..\examples\evaluation\perception-output.example.json
```

