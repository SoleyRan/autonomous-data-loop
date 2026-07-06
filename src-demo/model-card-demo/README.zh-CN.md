# 模型卡片生成 Demo

[English](README.md)

这个 demo 基于训练配置、训练任务和指标报告生成一个简化模型卡片。

它展示阶段四的核心思想：训练完成的模型应该带着数据集血缘、训练配置、指标和就绪状态进入模型注册。

## 运行

```powershell
python build_model_card.py `
  ..\..\examples\training\training-config.example.json `
  ..\..\examples\training\training-job.example.json `
  ..\..\examples\training\model-metrics.example.json
```

