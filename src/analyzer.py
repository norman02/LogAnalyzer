import logging

logging.basicConfig(level=logging.DEBUG)


def categorize_log(log_entry):
    """
    Categorizes a log entry based on severity.
    """
    level = log_entry.get("level", "")
    # Ensure level is a string before calling string methods

    if not isinstance(level, str):
        logging.warning(f"Unexpected log level type: {type(level)} - {level}")
        return "Unknown Category"

    level = level.strip().upper()

    categories = {
        "ERROR": "Critical Issue",
        "WARNING": "Potential Problem",
        "INFO": "General Info",
    }

    if level not in categories:
        logging.warning(f"Unexpected log level value: {level}")

    return categories.get(level, "Unknown Category")  # Simplified lookup
