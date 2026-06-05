# 阶段二任务状态机 Demo

[English](README.md)

这个 demo 展示阶段二标注、质检和导出任务的简化状态机。

它是一个公开安全的小示例，不是生产代码。

## 运行

```powershell
python phase2_state_machine.py
```

## 覆盖流程

```text
created -> preprocessing -> annotating -> draft_ready -> qc_in_progress -> final_ready -> frozen -> exported
```

