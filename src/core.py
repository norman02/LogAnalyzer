from src.parser import parse_log_entry
from src.analyzer import LogCategorizer
from src.reporter import generate_structured_report, export_report
from src.exporters import CSVExporter, JSONExporter


class LogAnalyzerCore:
    """Central controller for parsing, analyzing, and reporting logs.

    This class follows SOLID principles, ensuring separation of concerns
    and easy dependency injection.
    """

    def __init__(self, raw_log_lines, parser, analyzer=None):
        """Initialize LogAnalyzerCore with dependency injection.

        :param raw_log_lines: List of raw log entries (string format).
        :param parser: Function to parse individual log lines into structured data.
        :param analyzer: Custom log categorizer (defaults to LogCategorizer).
        """
        # Parse logs using the provided parser function
        self.raw_logs = self.parse_logs(raw_log_lines, parser)

        # Use the provided analyzer or default to LogCategorizer
        self.analyzer = analyzer or LogCategorizer()

    def parse_logs(self, raw_log_lines, parser):
        """Parse log entries using the provided parser function.

        :param raw_log_lines: List of raw log entries (string format).
        :param parser: Function to parse individual log lines into structured data.
        :return: List of parsed log dictionaries.
        """
        # Filter out None values to ensure only valid logs are processed
        return [parser(line) for line in raw_log_lines if parser(line)]

    def analyze_logs(self):
        """Categorize parsed logs based on severity.

        :return: List of log entries with an added 'category' field.
        """
        return [
            {**log, "category": self.analyzer.categorize(log)} for log in self.raw_logs
        ]

    def export_report(self, format_type="csv"):
        """Export structured report in CSV or JSON format.

        :param format_type: Export format ('csv' or 'json').
        :return: Formatted report as a string.
        """
        structured_report = generate_structured_report(self.raw_logs)

        # Select the appropriate exporter based on format type
        exporters = {"csv": CSVExporter, "json": JSONExporter}
        exporter_class = exporters.get(format_type, CSVExporter)  # Default to CSV
        exporter = exporter_class()

        return export_report(structured_report, exporter)
