import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


def load_cases(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return data
    return [data]


def normalize_name(value: str) -> str:
    return value.lower().replace(" ", "_").replace("-", "_")


def build_requirement(cases: list[dict[str, Any]]) -> dict[str, Any]:
    first = cases[0]
    scenario = first["scenario"]
    object_class = first["object_class"]
    error_type = first["error_type"]
    scene_tags = scenario.get("scene_tags", [])
    distance_range = scenario.get("distance_range", "unknown")
    requirement_name = "_".join(
        [*(normalize_name(tag) for tag in scene_tags), normalize_name(distance_range), object_class, error_type]
    )

    severity_score = {
        "low": 30,
        "medium": 60,
        "high": 85,
        "critical": 95,
    }.get(first.get("severity", "medium"), 60)

    return {
        "requirement_id": f"data_requirement_from_{first['case_id']}",
        "name": requirement_name,
        "source_case_ids": [case["case_id"] for case in cases],
        "target_scenario": {
            "scene_tags": scene_tags,
            "object_class": object_class,
            "distance_range": distance_range,
            "error_type": error_type,
        },
        "target_count": max(100, len(cases) * 50),
        "priority": min(100, severity_score + min(20, len(cases) * 5)),
        "status": "rule_proposed",
    }


def build_probe_rule(requirement: dict[str, Any]) -> dict[str, Any]:
    now = datetime.now(timezone.utc)
    expire_at = now + timedelta(days=30)
    scenario = requirement["target_scenario"]
    rule_name = f"feedback_{requirement['name']}"

    return {
        "probe_rule_update_id": f"probe_rule_update_for_{requirement['requirement_id']}",
        "requirement_id": requirement["requirement_id"],
        "proposal_type": "create",
        "probe_rule": {
            "probe_rule_id": f"probe_rule_{normalize_name(rule_name)}",
            "name": rule_name,
            "version": "1.0",
            "enabled": True,
            "priority": requirement["priority"],
            "validity": {
                "start_at": now.isoformat(timespec="seconds").replace("+00:00", "Z"),
                "expire_at": expire_at.isoformat(timespec="seconds").replace("+00:00", "Z"),
            },
            "trigger": {
                "scene_tags": scenario["scene_tags"],
                "object_class_hint": scenario["object_class"],
                "distance_range": scenario["distance_range"],
            },
            "capture": {
                "pre_seconds": 8,
                "post_seconds": 8,
                "topics": [
                    "/camera/front",
                    "/lidar/front",
                    "/vehicle/state",
                ],
            },
            "upload": {
                "strategy": "on_trigger",
                "target_count": requirement["target_count"],
                "compress": True,
            },
        },
        "review": {
            "status": "pending",
            "risk_level": "medium" if requirement["priority"] >= 60 else "low",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("feedback_case_json", type=Path)
    args = parser.parse_args()

    cases = load_cases(args.feedback_case_json)
    requirement = build_requirement(cases)
    probe_rule = build_probe_rule(requirement)
    print(json.dumps({"data_requirement": requirement, "probe_rule_update": probe_rule}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

