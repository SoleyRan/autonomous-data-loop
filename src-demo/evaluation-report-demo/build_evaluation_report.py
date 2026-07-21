import argparse
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def distance_3d(a: dict[str, float], b: dict[str, float]) -> float:
    return math.sqrt((a["x"] - b["x"]) ** 2 + (a["y"] - b["y"]) ** 2 + (a["z"] - b["z"]) ** 2)


def f1(precision: float, recall: float) -> float:
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)


def metric_dict(tp: int, fp: int, fn: int) -> dict[str, float | int]:
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    return {
        "true_positive": tp,
        "false_positive": fp,
        "false_negative": fn,
        "precision": round(precision, 3),
        "recall": round(recall, 3),
        "f1": round(f1(precision, recall), 3),
    }


def index_predictions(prediction_data: dict[str, Any]) -> dict[int, list[dict[str, Any]]]:
    indexed: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for frame in prediction_data.get("predictions", []):
        indexed[frame["frame_timestamp_ns"]].extend(frame.get("objects", []))
    return indexed


def evaluate(labels: dict[str, Any], predictions: dict[str, Any], threshold_m: float = 2.0) -> dict[str, Any]:
    indexed_predictions = index_predictions(predictions)
    counts = Counter()
    class_counts: dict[str, Counter[str]] = defaultdict(Counter)
    failed_cases = []

    for frame in labels.get("frames", []):
        timestamp = frame["frame_timestamp_ns"]
        unmatched_predictions = list(indexed_predictions.get(timestamp, []))

        for expected in frame.get("objects", []):
            expected_class = expected["class_name"]
            expected_center = expected["box_3d"]["center"]
            best_index = None
            best_distance = None

            for idx, actual in enumerate(unmatched_predictions):
                if actual["class_name"] != expected_class:
                    continue
                actual_center = actual["box_3d"]["center"]
                dist = distance_3d(expected_center, actual_center)
                if dist <= threshold_m and (best_distance is None or dist < best_distance):
                    best_index = idx
                    best_distance = dist

            if best_index is None:
                counts["fn"] += 1
                class_counts[expected_class]["fn"] += 1
                failed_cases.append(
                    {
                        "error_type": "false_negative",
                        "frame_timestamp_ns": timestamp,
                        "expected_class": expected_class,
                    }
                )
            else:
                counts["tp"] += 1
                class_counts[expected_class]["tp"] += 1
                unmatched_predictions.pop(best_index)

        for actual in unmatched_predictions:
            actual_class = actual["class_name"]
            counts["fp"] += 1
            class_counts[actual_class]["fp"] += 1
            failed_cases.append(
                {
                    "error_type": "false_positive",
                    "frame_timestamp_ns": timestamp,
                    "actual_class": actual_class,
                    "confidence": actual.get("confidence"),
                }
            )

    return {
        "metric_summary": {
            "overall": metric_dict(counts["tp"], counts["fp"], counts["fn"]),
            "by_class": {
                class_name: metric_dict(values["tp"], values["fp"], values["fn"])
                for class_name, values in sorted(class_counts.items())
            },
        },
        "failed_case_count": len(failed_cases),
        "failed_cases": failed_cases,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("canonical_label_json", type=Path)
    parser.add_argument("perception_output_json", type=Path)
    parser.add_argument("--threshold-m", type=float, default=2.0)
    args = parser.parse_args()

    report = evaluate(
        load_json(args.canonical_label_json),
        load_json(args.perception_output_json),
        threshold_m=args.threshold_m,
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

