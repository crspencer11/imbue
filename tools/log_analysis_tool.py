import re

class LogAnalysisTool:
    def extract_error_keywords(self, logs: str):
        keywords = set()

        # capture high-signal tokens from logs
        patterns = [
            r"([A-Za-z_]+Error)",          # WriteError, TypeError, etc
            r"'([^']+)'",                 # quoted identifiers
            r"([a-zA-Z_]+\.py)",          # python files
            r"([a-zA-Z_]+_+[a-zA-Z_]+)",  # snake_case tokens
        ]

        for pattern in patterns:
            matches = re.findall(pattern, logs)
            for m in matches:
                if isinstance(m, tuple):
                    keywords.update(m)
                else:
                    keywords.add(m)

        # clean noise
        cleaned = [
            k for k in keywords
            if len(k) < 60 and not k.startswith("ERROR")
        ]

        return list(cleaned)