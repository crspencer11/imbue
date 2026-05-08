from pathlib import Path

class RepoSearchTool:
    def __init__(self, root="."):
        self.root = Path(root)

    def search(self, query: str, extensions=None):
        extensions = extensions or [".py", ".ts", ".tsx", ".go"]

        matches = []

        for path in self.root.rglob("*"):
            if path.suffix not in extensions:
                continue

            try:
                content = path.read_text(errors="ignore")

                if query.lower() in content.lower():
                    matches.append({
                        "file": str(path),
                        "preview": self._extract_preview(content, query)
                    })

            except Exception:
                pass

        return matches[:10]

    def _extract_preview(self, content, query):
        lines = content.splitlines()

        for i, line in enumerate(lines):
            if query.lower() in line.lower():
                start = max(0, i - 2)
                end = min(len(lines), i + 3)

                return "\n".join(lines[start:end])

        return ""