import re
from typing import Optional, Dict


def parse_log_entry(
    log_entry: Optional[str], allowed_levels: Optional[set] = None
) -> Optional[Dict[str, str]]:
    """Parses a log entry string into its components: timestamp, level, message.

    :param log_entry: Log entry string.
    :param allowed_levels: Set of allowed log levels (defaults to ERROR, WARNING, INFO).
    :return: Dictionary with parsed log fields, or None if the format is invalid or level is not allowed.
    """
    if not isinstance(log_entry, str) or not log_entry.strip():
        return None  # ✅ Handle None and empty strings gracefully

    if allowed_levels is None:
        allowed_levels = {"ERROR", "WARNING", "INFO"}  # ✅ Default log levels

    log_entry = log_entry.strip()  # ✅ Normalize input

    match = re.fullmatch(
        r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)$", log_entry
    )
    if not match:
        return None

    timestamp, level, message = match.groups()

    if level not in allowed_levels:
        return None

    return {"timestamp": timestamp, "level": level, "message": message}
