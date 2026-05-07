from dataclasses import dataclass, field
from typing import List
import uuid


@dataclass
class StepResult:
    step_id: str
    thought: str
    action: str
    observation: str
    status: str


@dataclass
class RunState:
    run_id: str
    task: str
    steps: List[StepResult] = field(default_factory=list)
    parent_run_id: str | None = None

    @staticmethod
    def create(task: str, parent_run_id: str | None = None):
        return RunState(
            run_id=str(uuid.uuid4())[:8],
            task=task,
            parent_run_id=parent_run_id,
        )
