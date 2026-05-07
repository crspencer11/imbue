import json
from pathlib import Path
from dataclasses import asdict

from agent.models import RunState


RUN_DIR = Path("runs")
RUN_DIR.mkdir(exist_ok=True)


def save_run(state: RunState):
    path = RUN_DIR / f"{state.run_id}.json"

    with open(path, "w") as f:
        json.dump(asdict(state), f, indent=2)


def load_run(run_id: str) -> dict:
    path = RUN_DIR / f"{run_id}.json"

    with open(path) as f:
        return json.load(f)


def list_runs() -> list[dict]:
    runs = []

    for path in RUN_DIR.glob("*.json"):
        with open(path) as f:
            runs.append(json.load(f))

    return runs
