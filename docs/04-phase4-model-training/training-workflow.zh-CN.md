# 训练流程

[English](training-workflow.md)

## 主流程

```mermaid
sequenceDiagram
  participant U as 用户
  participant P as 平台
  participant D as 数据集存储
  participant S as 调度器
  participant R as 训练运行环境
  participant M as 模型注册

  U->>P: 选择冻结数据集版本
  U->>P: 选择训练配置
  P->>D: 加载数据集 manifest
  P->>S: 提交训练任务
  S->>R: 启动训练运行环境
  R->>D: 读取数据集 manifest 和样本
  R->>P: 回传日志和指标
  R->>M: 上传模型产物
  P->>M: 注册模型版本和血缘关系
  U->>P: 查看指标并对比版本
```

## 训练任务状态

```mermaid
stateDiagram-v2
  [*] --> Created
  Created --> Queued
  Queued --> Running
  Running --> Succeeded
  Running --> Failed
  Running --> Cancelled
  Succeeded --> Registered
  Registered --> ReadyForEvaluation
```

## 必要输入

| 输入 | 说明 |
|---|---|
| 数据集 manifest | 阶段三冻结后的数据集版本 |
| 训练配置 | 模型结构、超参、运行环境和输出规则 |
| 运行镜像 | 容器或环境版本 |
| 代码版本 | Git commit、包版本或 release ID |

## 必要输出

| 输出 | 说明 |
|---|---|
| 模型产物 | checkpoint、导出模型或运行包 |
| 指标 | 训练、验证和场景级指标 |
| 日志 | 运行日志和失败原因 |
| 模型卡片 | 面向人工评审的血缘、指标和就绪状态摘要 |

