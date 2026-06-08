# 数据集 Manifest 生成 Demo

[English](README.md)

这个 demo 基于样本索引和确定性划分配置，生成一个小型数据集 manifest。

它展示阶段三的核心思想：数据集版本应该是可复现的工程产物，明确记录样本、划分和统计信息。

## 运行

```powershell
python build_dataset_manifest.py `
  ..\..\examples\metadata\dataset-sample-index.example.json `
  ..\..\examples\manifest\phase3-split-config.example.json
```

