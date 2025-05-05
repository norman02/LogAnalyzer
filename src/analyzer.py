import logging
from typing import Any, Dict, Optional

UNKNOWN_CATEGORY = "Unknown Category"


class LogCategorizer:
    """Handles categorization of log entries based on severity levels."""

    def __init__(
        self,
        severity_map: Optional[Dict[str, str]] = None,
        logger: Optional[logging.Logger] = None,
    ) -> None:
        """
        Dependency injection for severity mappings and logger.

        :param severity_map: Optional custom mapping for log levels.
        :param logger: Optional logger. If not provided, a default logger is used.
        """
        self.severity_map: Dict[str, str] = severity_map or {
            "ERROR": "Critical Issue",
            "WARNING": "Potential Problem",
            "INFO": "General Info",
        }

        # Use dependency injection for the logger; if none provided, obtain one by name.
        self.logger: logging.Logger = logger or logging.getLogger("log_categorizer")

        # Explicitly attach a StreamHandler to ensure messages are processed.
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            handler.setLevel(logging.WARNING)
            formatter = logging.Formatter("%(levelname)s: %(message)s")
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

        self.logger.setLevel(logging.WARNING)

    def log_warning(self, message: str) -> None:
        """Helper function for logging warnings."""
        self.logger.warning(message)

    def categorize(self, log_entry: Dict[str, Any]) -> str:
        """
        Categorizes a log entry based on severity.

        :param log_entry: Dictionary containing log details.
        :return: Categorized severity description.
        """
        if not isinstance(log_entry, dict):
            self.log_warning(f"Invalid log entry type: {type(log_entry)} - {log_entry}")
            return UNKNOWN_CATEGORY

        level: Any = log_entry.get("level", "")
        if not isinstance(level, str):
            self.log_warning(f"Unexpected log level type: {type(level)} - {level}")
            return UNKNOWN_CATEGORY

        level = level.strip().upper()
        category = self.severity_map.get(level, UNKNOWN_CATEGORY)
        if category == UNKNOWN_CATEGORY:
            self.log_warning(f"Unexpected log level value: {level}")
        return category
