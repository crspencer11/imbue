from tools.log_analysis_tool import LogAnalysisTool
from tools.repo_search_tool import RepoSearchTool

LOGS = """
ERROR: Error in thread 'write_certified_data' with target 'write_file'
ERROR: Unhandled exception in thread
"""

ISSUE = "mngr create crashes immediately after install"

def main():
    log_tool = LogAnalysisTool()
    repo_tool = RepoSearchTool("./mngr")  # IMPORTANT: scoped correctly

    print("\n=== Extracted Error Keywords ===")
    keywords = log_tool.extract_error_keywords(LOGS)
    print(keywords)

    print("\n=== Repository Search Results ===")

    for kw in keywords:
        results = repo_tool.search(kw)

        for r in results:
            print(f"\nFile: {r['file']}")

    print("\n=== Investigation Summary ===")
    print("""
Likely issue:
- write_certified_data thread failing during file write phase

Possible causes:
- missing file write permissions
- runtime environment mismatch after install
- incorrect CLI execution context (global vs repo venv)

Suggested next steps:
1. run CLI from repo virtual environment
2. inspect write_certified_data initialization
3. verify filesystem access during install flow
""")

if __name__ == "__main__":
    main()