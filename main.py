import argparse

from agent.runtime import AgentRuntime
from agent.replay import replay_from
from agent.history import get_history


parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(dest="command")

run_parser = subparsers.add_parser("run")
run_parser.add_argument("task")

replay_parser = subparsers.add_parser("replay")
replay_parser.add_argument("run_id")
replay_parser.add_argument("step", type=int)

history_parser = subparsers.add_parser("history")
history_parser.add_argument("run_id")
history_parser.add_argument("step", type=int)

args = parser.parse_args()

if args.command == "run":
    runtime = AgentRuntime()
    state = runtime.run(args.task)

    print(f"Run ID: {state.run_id}")

elif args.command == "replay":
    state = replay_from(args.run_id, args.step)

    print(f"Branched replay run: {state.run_id}")

elif args.command == "history":
    # default is 0 or beginning of agent history
    history = get_history(args.run_id, args.step)

    print(history)
