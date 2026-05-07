from agent.models import StepResult


def execute_step(step: str) -> StepResult:
    if "Patch" in step:
        status = "failed"
        observation = "Patch introduced regression"
    else:
        status = "success"
        observation = f"Executed: {step}"

    return StepResult(
        step_id=step.lower().replace(" ", "_"),
        thought=f"Need to perform: {step}",
        action=step,
        observation=observation,
        status=status,
    )
