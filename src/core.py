from src.parser import parse_log_entry
from src.analyzer import LogCategorizer
from src.reporter import generate_structured_report, export_report
from src.exporters import CSVExporter, JSONExporter


class LogAnalyzerCore:
    """Central controller for parsing, analyzing, and reporting logs."""

    def __init__(self, raw_log_lines, parser):
        """
        Initialize the LogAnalyzerCore.

        :param raw_log_lines: List of raw log entries as strings
        :param parser: Function to parse individual log lines into structured data.
        """
        # Parse each log line using the injected parser function

        # Ignore lines that return None (invalid or empty entries)

        self.raw_logs = [parser(line) for line in raw_log_lines if parser(line)]

        # Initialize the log categorizer (handles severity classification)
        self.analyzer = LogCategorizer()

    def analyze_logs(self):
        """Categorize parsed logs based on severity.

        :return: List of log entries with an added 'category' field.
        """
        return [
            {**log, "category": self.analyzer.categorize(log)} for log in self.raw_logs
        ]

    def export_report(self, format_type="csv"):
        """Export structured report in CSV or JSON format."""
        structured_report = generate_structured_report(self.raw_logs)
        exporter = CSVExporter() if format_type == "csv" else JSONExporter()
        return export_report(structured_report, exporter)
