# Results and Evidence

[简体中文](results.zh-CN.md)

## Result Summary

Phase 1 proved that the first layer of the data loop is usable:

- Data packages can be generated from vehicle-side runtime data.
- Metadata and probe rules can describe why and when data is uploaded.
- MCAP-related packages can be compressed and uploaded.
- The platform can show vehicles, events, probe rules, datasets, and uploaded resources.
- Uploaded data can be reviewed through a playback entry.

## Evidence Map

| Capability | Evidence type | Public status |
|---|---|---|
| Vehicle-side module startup | Sanitized log summary | Included |
| Probe rule loading | Sanitized log summary | Included |
| Metadata generation | Sanitized metadata fields | Included |
| Compression | Sanitized before/after screenshots | To be added after masking |
| Upload result | Platform resource screenshots | To be added after masking |
| Playback | Platform playback screenshot | To be added after masking |

## Sanitized Sample Metadata

```json
{
  "package_type": "mcap_backup_archive",
  "duration_seconds": 21,
  "compressed_size_bytes": 341275952,
  "sharding_count": 33,
  "event_type": "sample_trigger_event",
  "integrity_check": "checksum_recorded"
}
```

## What This Enabled

Phase 1 made later phases feasible because it created:

- A stable path for MCAP assets to enter the platform.
- A metadata baseline for search and traceability.
- A probe-rule mechanism that can later support targeted collection.
- A playback verification path for human review.
- A resource model that Phase 2 can reuse for automated annotation.

## Follow-Up Work

The next phase builds on these results by adding automated annotation, 3D quality inspection, label versioning, and dataset export.

