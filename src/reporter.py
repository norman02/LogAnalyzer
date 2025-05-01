from src.exporters import CSVExporter, JSONExporter, ReportExporter


def generate_summary_report(log_entries):
    """Generates a summary report grouping log entries by severity."""
    summary = {}
    for entry in log_entries:
        level = entry.get("level", "UNKNOWN")
        summary[level] = summary.get(level, 0) + 1
    return summary


def generate_structured_report(log_entries):
    """Generates a structured summary of log entries in JSON-like format."""
    summary = generate_summary_report(log_entries)
    return {"summary": summary, "logs": log_entries}


def export_report(report, exporter: ReportExporter):
    """Exports report using the given exporter instance."""
    return exporter.export(report)
