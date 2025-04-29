def categorize_log(log_entry):
    """
    Categorizes a log entry based on severity.

    ERROR    → "Critical Issue"
    WARNING  → "Potential Problem"
    INFO     → "General Info"
    """
    level = log_entry.get("level", "").upper()

    if level == "ERROR":
        return "Critical Issue"
    elif level == "WARNING":
        return "Potential Problem"
    elif level == "INFO":
        return "General Info"
    else:
        return "Unknown Category"
