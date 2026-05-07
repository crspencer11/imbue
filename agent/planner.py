def generate_plan(task: str) -> list[str]:
    return [
        "Inspect repository",
        "Run tests",
        "Identify failing test",
        "Patch implementation",
        "Re-run tests",
    ]
