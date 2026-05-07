from agent.runtime import AgentRuntime
from agent.replay import replay_from


def test_replay_creates_branch():
    runtime = AgentRuntime()

    original = runtime.run("Fix failing tests")

    branched = replay_from(original.run_id, 2)

    assert branched.parent_run_id == original.run_id
    assert len(branched.steps) >= 2
    assert branched.run_id != original.run_id
