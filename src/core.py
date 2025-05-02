from src.parser import parse_log_entry
from src.analyzer import LogCategorizer
from src.reporter import generate_structured_report, export_report
from src.exporters import CSVExporter, JSONExporter


class LogAnalyzerCore:
    """Central controller for parsing, analyzing, and reporting logs."""

    def __init__(self, raw_log_lines):
        self.raw_logs = raw_log_lines
        self.parsed_logs = [
            parse_log_entry(line) for line in self.raw_logs if parse_log_entry(line)
        ]
        self.analyzer = LogCategorizer()
        self.structured_report = generate_structured_report(self.parsed_logs)

    def analyze_logs(self):
        """Categorize parsed logs based on severity."""
        return [
            {**log, "category": self.analyzer.categorize(log)}
            for log in self.parsed_logs
        ]

    def export_report(self, format_type="csv"):
        """Export structured report in CSV or JSON format."""
        exporter = CSVExporter() if format_type == "csv" else JSONExporter()
        return export_report(self.structured_report, exporter)
