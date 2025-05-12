import os
import sys
import logging
from src.core import LogAnalyzerCore
from src.parser import parse_log_entry

# Set up an explicit logger for this module.
logger = logging.getLogger("main")
logger.setLevel(logging.ERROR)

# Clear any preexisting handlers.
logger.handlers.clear()

# Create and add a FileHandler to write logs to error.log.
file_handler = logging.FileHandler("error.log", mode="w")
file_handler.setLevel(logging.ERROR)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_logs_from_file(file_path="logs.txt"):
    """Retrieve log entries from a file or return an empty list.

    :param file_path: Path to log file.
    :return: List of log lines.
    """
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.readlines()
    return []


def main(log_file="logs.txt", export_format="csv"):
    """Main execution function for log analysis and reporting."""
    try:
        raw_logs = get_logs_from_file(log_file)

        if not raw_logs:  # Handle case where logs are missing.
            raise FileNotFoundError(f"Log file '{log_file}' not found or empty.")

        analyzer = LogAnalyzerCore(raw_logs, parser=parse_log_entry)
        categorized_logs = analyzer.analyze_logs()
        report = analyzer.export_report(export_format)
        print(f"\n{export_format.upper()} Report:\n", report)

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        # Flush and close all logger handlers to force file creation.
        for handler in logger.handlers:
            handler.flush()
            handler.close()
        logging.shutdown()
        print("An error occurred. Check 'error.log' for details.", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
