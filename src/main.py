import os
import sys
from src.core import LogAnalyzerCore


def main():
    try:
        # Ensure the current working directory is set relative to this file;
        # this helps resolve any relative paths (like config or logs) consistently.
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        # Define a fixed set of raw log entries for demonstration.
        raw_logs = [
            "2025-05-01 10:00:00 ERROR Crash detected",
            "2025-05-01 10:05:00 INFO Startup complete",
            "2025-05-01 10:10:00 WARNING High memory usage",
        ]

        # Initialize the core analyzer.
        analyzer = LogAnalyzerCore(raw_logs)

        # Run analysis to enrich logs with categories.
        categorized_logs = analyzer.analyze_logs()
        print("Categorized Logs:")
        print(categorized_logs)

        # Export the report in CSV format.
        csv_report = analyzer.export_report("csv")
        print("\nCSV Report:")
        print(csv_report)

    except Exception as e:
        # On exception, print the error to stderr and return a non-zero exit code.
        print("An error occurred in main:", e, file=sys.stderr)
        return 1

    # If everything runs smoothly, return 0.
    return 0


if __name__ == "__main__":
    sys.exit(main())
