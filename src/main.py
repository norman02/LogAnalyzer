import os
import sys
from src.core import LogAnalyzerCore
from src.parser import parse_log_entry  # ✅ Import parser


def get_logs_from_file(file_path="logs.txt"):
    """Retrieve log entries from a file or fallback to default logs.

    :param file_path: Path to log file.
    :return: List of log lines
    """
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.readlines()

        # Default logs for testing/demo purposes

    return [
        "2025-05-01 10:00:00 ERROR Crash detected",
        "2025-05-01 10:05:00 INFO Startup complete",
        "2025-05-01 10:10:00 WARNING High memory usage",
    ]


def main():
    try:
        # ✅ Ensure consistent working directory resolution
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        # ✅ Sample log entries for demonstration
        raw_logs = [
            "2025-05-01 10:00:00 ERROR Crash detected",
            "2025-05-01 10:05:00 INFO Startup complete",
            "2025-05-01 10:10:00 WARNING High memory usage",
        ]

        # 🔥 FIX: Pass the parser function to LogAnalyzerCore
        analyzer = LogAnalyzerCore(raw_logs, parser=parse_log_entry)

        # ✅ Run analysis to enrich logs with categories
        categorized_logs = analyzer.analyze_logs()
        print("Categorized Logs:", categorized_logs)

        # ✅ Export the report in CSV format
        csv_report = analyzer.export_report("csv")
        print("\nCSV Report:\n", csv_report)

    except Exception as e:
        # ✅ Handle errors gracefully
        print("An error occurred in main:", e, file=sys.stderr)
        return 1

    return 0  # ✅ Indicate successful execution


if __name__ == "__main__":
    sys.exit(main())
