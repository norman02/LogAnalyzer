import re
from typing import Optional, Dict


def parse_log_entry(log_entry: str) -> Optional[Dict[str, str]]:
    """
    Parses a log entry string into its components: timestamp, level, message.

    :param log_entry: Log entry string.
    :return: Dictionary with parsed log fields, or None if the format is invalid or if the level is not allowed.
    """
    # Define the allowed log levels
    allowed_levels = {"ERROR", "WARNING", "INFO"}

    # The regex expects: timestamp, level, then message—each separated by a single space.
    match = re.match(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)$", log_entry)

    if not match:
        return None  # Log format doesn't match

    timestamp, level, message = match.groups()

    # Validate that the log level is one of the allowed levels
    if level not in allowed_levels:
        return None

    return {
        "timestamp": timestamp,
        "level": level,
        "message": message,
    }
