import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_model_card(
    training_config: dict[str, Any],
    training_job: dict[str, Any],
    metrics: dict[str, Any],
) -> dict[str, Any]:
    overall = metrics["metrics"]["overall"]
    readiness = metrics.get("readiness", {})
    artifact_uri = training_job["outputs"]["model_artifact_uri"]

    limitations: list[str] = []
    by_scenario = metrics["metrics"].get("by_scenario", {})
    if by_scenario:
        weakest = min(by_scenario.items(), key=lambda item: item[1].get("map", 0.0))
        limitations.append(f"Lowest scenario mAP: {weakest[0]}={weakest[1].get('map', 0.0):.3f}")

    by_class = metrics["metrics"].get("by_class", {})
    if by_class:
        weakest_class = min(by_class.items(), key=lambda item: item[1].get("recall", 0.0))
        limitations.append(
            f"Lowest class recall: {weakest_class[0]}={weakest_class[1].get('recall', 0.0):.3f}"
        )

    return {
        "model_version_id": metrics["model_version_id"],
        "model_family": training_config["model_family"],
        "status": "ready_for_evaluation" if readiness.get("ready_for_evaluation") else "needs_review",
        "artifact": {
            "uri": artifact_uri,
            "format": artifact_uri.rsplit(".", 1)[-1],
        },
        "lineage": {
            "training_job_id": training_job["training_job_id"],
            "training_config_id": training_config["training_config_id"],
            "dataset_version_id": training_job["dataset_version_id"],
            "code_version": training_job["code_version"],
        },
        "metric_summary": {
            "map": overall["map"],
            "precision": overall["precision"],
            "recall": overall["recall"],
            "f1": overall["f1"],
        },
        "known_limitations": limitations,
        "blocking_issues": readiness.get("blocking_issues", []),
        "next_step": "submit_to_phase5_automated_evaluation"
        if readiness.get("ready_for_evaluation")
        else "review_training_result",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("training_config", type=Path)
    parser.add_argument("training_job", type=Path)
    parser.add_argument("model_metrics", type=Path)
    args = parser.parse_args()

    card = build_model_card(
        load_json(args.training_config),
        load_json(args.training_job),
        load_json(args.model_metrics),
    )
    print(json.dumps(card, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

