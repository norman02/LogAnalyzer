import logging
from typing import Any, Dict, Optional


class LogCategorizer:
    """Handles categorization of log entries based on severity levels."""

    def __init__(self, severity_map: Optional[Dict[str, str]] = None) -> None:
        """
        Dependency injection for severity mappings.

        :param severity_map: Optional custom mapping for log levels.
        """
        self.severity_map: Dict[str, str] = severity_map or {
            "ERROR": "Critical Issue",
            "WARNING": "Potential Problem",
            "INFO": "General Info",
        }

    def categorize(self, log_entry: Dict[str, Any]) -> str:
        """
        Categorizes a log entry based on severity.

        :param log_entry: Dictionary containing log details.
        :return: Categorized severity description.
        """
        # Ensure log_entry is a Dictionary
        if not isinstance(log_entry, dict):
            logging.warning(f"Invalid log entry type: {type(log_entry)} - {log_entry}")
            return "Unknown Category"
        # Attempt to get the "level" value, defaulting to an empty string.
        level: Any = log_entry.get("level", "")

        # Ensure level is a string before calling string methods.
        if not isinstance(level, str):
            logging.warning(f"Unexpected log level type: {type(level)} - {level}")
            return "Unknown Category"

        # Standardize the level by stripping whitespace and converting to uppercase.
        level = level.strip().upper()

        if level not in self.severity_map:
            logging.warning(f"Unexpected log level value: {level}")

        return self.severity_map.get(level, "Unknown Category")
