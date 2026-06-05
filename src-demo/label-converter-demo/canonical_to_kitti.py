import argparse
import json
from pathlib import Path
from typing import Any


def kitti_type(class_name: str) -> str:
    mapping = {
        "car": "Car",
        "truck": "Truck",
        "pedestrian": "Pedestrian",
        "cyclist": "Cyclist",
        "traffic_cone": "DontCare",
        "barrier": "DontCare",
    }
    return mapping.get(class_name, "DontCare")


def object_to_kitti_line(obj: dict[str, Any]) -> str:
    box = obj["box_3d"]
    center = box["center"]
    size = box["size"]
    yaw = box.get("rotation", {}).get("yaw", 0.0)
    score = obj.get("confidence", 1.0)

    fields = [
        kitti_type(obj["class_name"]),
        "0.00",  # truncated
        "0",  # occluded
        "0.00",  # alpha
        "0.00",
        "0.00",
        "0.00",
        "0.00",  # 2D box placeholder
        f"{size['height']:.3f}",
        f"{size['width']:.3f}",
        f"{size['length']:.3f}",
        f"{center['x']:.3f}",
        f"{center['y']:.3f}",
        f"{center['z']:.3f}",
        f"{yaw:.3f}",
        f"{score:.3f}",
    ]
    return " ".join(fields)


def convert(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    lines: list[str] = []
    for frame in data.get("frames", []):
        for obj in frame.get("objects", []):
            lines.append(object_to_kitti_line(obj))
    return lines


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("canonical_label_json", type=Path)
    args = parser.parse_args()

    for line in convert(args.canonical_label_json):
        print(line)


if __name__ == "__main__":
    main()

