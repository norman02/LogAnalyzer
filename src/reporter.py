import csv
from io import StringIO


def generate_summary_report(log_entries):
    """Generates a summary report grouping log entries by severity.

    :param log_entries: List of log entry dictionaries.
    :return: Dictionary containing log count per severity level.
    """
    summary = {}

    for entry in log_entries:
        level = entry.get("level", "UNKNOWN")
        summary[level] = summary.get(level, 0) + 1

    return summary


def generate_structured_report(log_entries):
    """
    Generates a structured summary of log entries in JSON-like format.

    :param log_entries: List of parsed log entry dictionaries.
    :return: Dictionary containing a structured log summary.
    """
    summary = {}

    for entry in log_entries:
        level = entry.get("level", "UNKNOWN")
        summary[level] = summary.get(level, 0) + 1

    return {"summary": summary, "logs": log_entries}


def export_report_csv(report):
    """
    Exports a log report to CSV format.

    :param retport: Dictionary containg a structured log summary
    :return: CSV string representation of the logs.
    """
    output = StringIO()
    writer = csv.writer(
        output, lineterminator="\n"
    )  # Enusre Unix-style line terminator

    # Write CSV header

    writer.writerow(["timestamp", "level", "message"])

    # Write log entries

    for log in report["logs"]:
        writer.writerow([log["timestamp"], log["level"], log["message"]])
    return output.getvalue()
