# 评测报告 Demo

[English](README.md)

这个 demo 对比简化的统一标签文件和感知输出，并生成评测报告。

它展示阶段五的核心思想：自动化评测应当用固定预测结果和冻结标签进行对比，产出指标和失败 case。

## 运行

```powershell
python build_evaluation_report.py `
  ..\..\examples\label-format\canonical-label.example.json `
  ..\..\examples\evaluation\perception-output.example.json
```

