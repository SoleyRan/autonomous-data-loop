# Workflow

[简体中文](workflow.zh-CN.md)

## Main Flow

```mermaid
sequenceDiagram
  participant U as User
  participant P as Platform
  participant S as Storage
  participant A as Auto Annotation Worker
  participant X as Xtreme1
  participant E as Export Worker

  U->>P: Filter and replay MCAP assets
  U->>P: Select assets for annotation
  P->>S: Create annotation input cache
  P->>A: Start automated annotation
  A->>S: Read MCAP-derived inputs
  A->>P: Save draft canonical labels
  P->>X: Create 3D QC task
  X->>U: Provide 3D correction workspace
  U->>X: Correct boxes, classes, and attributes
  X->>P: Return inspected labels
  P->>P: Validate and freeze final labels
  U->>P: Request KITTI / nuScenes export
  P->>E: Start export job
  E->>S: Generate export package
```

## Step 1: MCAP Selection

Users review uploaded MCAP assets on the platform. The first implementation uses whole MCAP packages as the selection unit.

Recommended filters:

- Upload time.
- Vehicle or device alias.
- Event or probe type.
- Duration.
- Package status.
- Playback availability.

## Step 2: Automated Annotation

The platform creates an annotation job and prepares the input required by the annotation worker. The worker runs inference and returns draft labels in the canonical label format.

Draft labels are not final labels. They are traceable intermediate versions.

## Step 3: Xtreme1 Quality Inspection

The platform creates a corresponding Xtreme1 task and imports the required 3D annotation inputs. Human reviewers inspect and correct the automated labels in Xtreme1.

Typical corrections:

- Move or resize 3D boxes.
- Fix classes.
- Add missed objects.
- Remove false positives.
- Update attributes.

## Step 4: Label Finalization

After Xtreme1 results return to the platform, the platform validates the labels, stores a final version, and optionally freezes it for export.

Validation examples:

- Required fields exist.
- Frame timestamps can be mapped back to MCAP data.
- Classes belong to the supported taxonomy.
- Box dimensions are within expected ranges.

## Step 5: Export

The export service reads final canonical labels and generates external packages.

The first public formats are:

- KITTI.
- nuScenes.

Future formats should be implemented as additional adapters.

