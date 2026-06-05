# Publication and Sanitization Checklist

[简体中文](publication-sanitization.zh-CN.md)

Before adding screenshots, logs, videos, or documents from Phase 1 to this public repository, sanitize them carefully.

## Do Not Publish

- Internal IP addresses, domains, ports, or service URLs.
- Account names, tokens, passwords, session IDs, or cookies.
- Real vehicle IDs, device IDs, IMEI values, customer names, or project-specific location names.
- Full raw logs.
- Original internal design documents.
- Production source code.
- Unmasked platform screenshots.

## Safe to Publish After Sanitization

- Cropped platform screenshots that show generic functions only.
- Sanitized upload logs with service addresses and device IDs removed.
- Aggregated task statistics.
- Before/after compression screenshots with paths and IDs masked.
- Playback screenshots with project names, domains, and identifiers masked.
- Simplified diagrams rebuilt for public explanation.

## Recommended Asset Naming

```text
phase1-platform-resource-list.png
phase1-playback-sanitized.png
phase1-compression-before.png
phase1-compression-after.png
phase1-upload-log-summary.txt
```

## Review Rule

If a file answers "where is the internal system", "which real device produced this", or "how can someone access it", it should not be published.

