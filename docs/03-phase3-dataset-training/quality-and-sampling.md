# Quality and Sampling

[简体中文](quality-and-sampling.zh-CN.md)

## Quality Checks

Before a dataset version is frozen, the platform should run lightweight checks:

| Check | Purpose |
|---|---|
| Missing label check | Avoid samples without valid final labels |
| Timestamp mapping check | Ensure samples can map back to source MCAP data |
| Class distribution check | Detect severe class imbalance |
| Split leakage check | Avoid near-duplicate samples across train/val/test |
| Sensor availability check | Ensure required sensor streams exist |
| Label schema check | Ensure all labels use the expected canonical schema |

## Sampling Dimensions

Recommended sampling dimensions:

- Time range.
- Vehicle or device alias.
- Event or probe type.
- Object class.
- Scene tag.
- Sensor type.
- Label version.
- Annotation confidence or QC status.

## Split Strategy

The first version can use deterministic hashing:

```text
split_key = hash(source_mcap_id + frame_timestamp_ns)
```

This makes the split stable across repeated runs. Later versions can add scenario-aware splitting to reduce leakage and improve evaluation fairness.

