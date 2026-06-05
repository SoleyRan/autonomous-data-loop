# 公开与脱敏清单

[English](publication-sanitization.md)

在把阶段一的截图、日志、视频或文档放到公开仓库之前，需要先完成脱敏。

## 不要公开

- 内网 IP、域名、端口或服务 URL。
- 账号、token、密码、session ID 或 cookie。
- 真实车辆 ID、设备 ID、IMEI、客户名称或具体项目地点名称。
- 完整原始日志。
- 公司内部原始设计文档。
- 生产源码。
- 未打码的平台截图。

## 脱敏后可以公开

- 只展示通用功能的平台截图。
- 去掉服务地址和设备 ID 的上传日志摘要。
- 聚合后的任务统计结果。
- 打码后的压缩前后截图。
- 打码后的平台回放截图。
- 为公开说明重新绘制的简化架构图。

## 推荐素材命名

```text
phase1-platform-resource-list.png
phase1-playback-sanitized.png
phase1-compression-before.png
phase1-compression-after.png
phase1-upload-log-summary.txt
```

## 审查原则

如果一个文件能回答“内部系统在哪里”“是哪台真实设备产生的”“别人如何访问它”，就不应该公开。

