# Model Card Builder Demo

[简体中文](README.zh-CN.md)

This demo builds a simple model card from a training config, training job, and metric report.

It demonstrates the Phase 4 idea: a trained model should be registered with dataset lineage, training configuration, metrics, and readiness status.

## Run

```powershell
python build_model_card.py `
  ..\..\examples\training\training-config.example.json `
  ..\..\examples\training\training-job.example.json `
  ..\..\examples\training\model-metrics.example.json
```

