import os
import sys
from src.core import LogAnalyzerCore
from src.parser import parse_log_entry  # ✅ Import parser
import logging

logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def get_logs_from_file(file_path="logs.txt"):
    """Retrieve log entries from a file or or return an empty list

    :param file_path: Path to log file.
    :return: List of log lines
    """
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.readlines()

    return []


def main(log_file="logs.txt", export_format="csv"):
    """Main execution function for log analysis and reporting."""
    try:
        raw_logs = get_logs_from_file(log_file)

        if not raw_logs:  # ✅ Handle case where logs are missing
            raise FileNotFoundError(f"Log file '{log_file}' not found or empty.")

        analyzer = LogAnalyzerCore(raw_logs, parser=parse_log_entry)
        categorized_logs = analyzer.analyze_logs()
        report = analyzer.export_report(export_format)
        print(f"\n{export_format.upper()} Report:\n", report)

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        print("An error occurred. Check 'error.log' for details.", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
