from dataclasses import dataclass
from enum import Enum


class Phase2State(str, Enum):
    CREATED = "created"
    PREPROCESSING = "preprocessing"
    ANNOTATING = "annotating"
    DRAFT_READY = "draft_ready"
    QC_IN_PROGRESS = "qc_in_progress"
    FINAL_READY = "final_ready"
    FROZEN = "frozen"
    EXPORTING = "exporting"
    EXPORTED = "exported"
    FAILED = "failed"


ALLOWED_TRANSITIONS = {
    Phase2State.CREATED: {Phase2State.PREPROCESSING, Phase2State.FAILED},
    Phase2State.PREPROCESSING: {Phase2State.ANNOTATING, Phase2State.FAILED},
    Phase2State.ANNOTATING: {Phase2State.DRAFT_READY, Phase2State.FAILED},
    Phase2State.DRAFT_READY: {Phase2State.QC_IN_PROGRESS, Phase2State.FAILED},
    Phase2State.QC_IN_PROGRESS: {Phase2State.FINAL_READY, Phase2State.FAILED},
    Phase2State.FINAL_READY: {Phase2State.FROZEN, Phase2State.QC_IN_PROGRESS},
    Phase2State.FROZEN: {Phase2State.EXPORTING},
    Phase2State.EXPORTING: {Phase2State.EXPORTED, Phase2State.FAILED},
    Phase2State.EXPORTED: set(),
    Phase2State.FAILED: {Phase2State.CREATED},
}


@dataclass
class Phase2Task:
    task_id: str
    state: Phase2State = Phase2State.CREATED

    def transit(self, next_state: Phase2State) -> None:
        allowed = ALLOWED_TRANSITIONS[self.state]
        if next_state not in allowed:
            raise ValueError(f"Invalid transition: {self.state} -> {next_state}")
        self.state = next_state


def demo() -> None:
    task = Phase2Task(task_id="phase2_demo_task_001")
    flow = [
        Phase2State.PREPROCESSING,
        Phase2State.ANNOTATING,
        Phase2State.DRAFT_READY,
        Phase2State.QC_IN_PROGRESS,
        Phase2State.FINAL_READY,
        Phase2State.FROZEN,
        Phase2State.EXPORTING,
        Phase2State.EXPORTED,
    ]

    print(f"{task.task_id}: {task.state.value}")
    for state in flow:
        task.transit(state)
        print(f"{task.task_id}: {task.state.value}")


if __name__ == "__main__":
    demo()
