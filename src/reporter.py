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
