import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


def stable_ratio(value: str) -> float:
    digest = hashlib.sha256(value.encode("utf-8")).hexdigest()
    return int(digest[:8], 16) / 0xFFFFFFFF


def assign_split(sample: dict[str, Any], config: dict[str, Any]) -> str:
    key_parts = [str(sample[field]) for field in config["hash_key"]]
    key = "|".join(key_parts) + "|" + config.get("seed", "")
    ratio = stable_ratio(key)
    train = config["ratios"]["train"]
    val = config["ratios"]["val"]
    if ratio < train:
        return "train"
    if ratio < train + val:
        return "val"
    return "test"


def build_manifest(sample_index: dict[str, Any], split_config: dict[str, Any]) -> dict[str, Any]:
    samples = sample_index["samples"]
    split_counts: Counter[str] = Counter()
    class_counts: Counter[str] = Counter()
    scene_counts: Counter[str] = Counter()

    output_samples = []
    for sample in samples:
        assigned = assign_split(sample, split_config)
        split_counts[assigned] += 1
        class_counts.update(sample.get("object_classes", []))
        scene_counts.update(sample.get("scene_tags", []))
        output = dict(sample)
        output["split"] = assigned
        output_samples.append(output)

    return {
        "manifest_version": "demo",
        "dataset_version_id": sample_index["dataset_version_id"],
        "sample_count": len(output_samples),
        "splits": dict(split_counts),
        "object_count_by_class": dict(class_counts),
        "scene_tag_count": dict(scene_counts),
        "samples": output_samples,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("sample_index", type=Path)
    parser.add_argument("split_config", type=Path)
    args = parser.parse_args()

    sample_index = json.loads(args.sample_index.read_text(encoding="utf-8"))
    split_config = json.loads(args.split_config.read_text(encoding="utf-8"))
    manifest = build_manifest(sample_index, split_config)
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

