import re

class LogAnalysisTool:
    def extract_error_keywords(self, logs: str):
        patterns = [
            r"ModuleNotFoundError: ([^\n]+)",
            r"ImportError: ([^\n]+)",
            r"AttributeError: ([^\n]+)",
            r"TypeError: ([^\n]+)",
            r"ERROR: ([^\n]+)",
        ]

        findings = []

        for pattern in patterns:
            matches = re.findall(pattern, logs)

            findings.extend(matches)

        return findings