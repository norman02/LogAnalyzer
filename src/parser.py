import re


def parse_log_entry(log_entry):
    """
    Parses a log entry string into its components:
    - timestamp (YYYY-MM-DD HH:MM:SS)
    - log level (e.g., ERROR, INFO)
    - message
    """
    match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)", log_entry)
    if match:
        return {
            "timestamp": match.group(1),
            "level": match.group(2),
            "message": match.group(3),
        }
    return None
