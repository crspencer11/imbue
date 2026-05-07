from agent.models import RunState
from agent.planner import generate_plan
from agent.executor import execute_step
from agent.storage import save_run


class AgentRuntime:
    def run(self, task: str) -> RunState:
        state = RunState.create(task)

        plan = generate_plan(task)

        for step in plan:
            result = execute_step(step)
            state.steps.append(result)

            save_run(state)

            if result.status == "failed":
                print(f"[!] Failed at: {step}")
                break

        return state
