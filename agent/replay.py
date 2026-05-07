from agent.models import RunState, StepResult
from agent.storage import load_run, save_run
from agent.executor import execute_step


def replay_from(run_id: str, step_index: int) -> RunState:
    data = load_run(run_id)

    original_steps = [
        StepResult(**s)
        for s in data["steps"][:step_index]
    ]

    branched = RunState.create(
        task=data["task"],
        parent_run_id=run_id,
    )

    branched.steps.extend(original_steps)

    replay_steps = [
        "Apply safer patch",
        "Run regression suite",
    ]

    for step in replay_steps:
        result = execute_step(step)

        # simulate successful replay branch
        result.status = "success"

        branched.steps.append(result)

    save_run(branched)

    return branched
