from pathlib import Path

IGNORED_DIRS = {
    ".venv", "venv", "__pycache__", ".git",
    "site-packages", ".idea"
}

class RepoSearchTool:
    def __init__(self, root):
        self.root = Path(root)

    def should_skip(self, path: Path):
        return any(part in IGNORED_DIRS for part in path.parts)

    def search(self, query: str, extensions=None):
        extensions = extensions or [".py", ".ts", ".go"]

        matches = []

        for path in self.root.rglob("*"):
            if self.should_skip(path):
                continue

            if not path.is_file():
                continue

            if path.suffix not in extensions:
                continue

            try:
                content = path.read_text(errors="ignore")

                if query.lower() in content.lower():
                    matches.append({
                        "file": str(path)
                    })

            except Exception:
                continue

        return matches[:5]