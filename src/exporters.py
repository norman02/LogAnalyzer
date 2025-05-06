from abc import ABC, abstractmethod
import csv
import json
from io import StringIO


class ReportExporter(ABC):
    """Abstract base class for exporting reports.

    This class defines a standard interface for exporting log reports
    in different formats (CSV, JSON, etc.).
    """

    @abstractmethod
    def export(self, report):
        """Export report in a specific format.

        :param report: A dictionary containing structured log data.
        :return: A formatted string representing the exported report.
        """
        pass


class CSVExporter(ReportExporter):
    """Exports structured log reports in CSV format.

    Generates a CSV-formatted output from a dictionary containing log entries.
    """

    def export(self, report):
        """Convert structured report data into CSV format.

        :param report: Dictionary with key 'logs', containing log entries.
        :return: CSV-formatted report as a string.
        :raises ValueError: If the report format is invalid.
        """
        if not isinstance(report, dict) or "logs" not in report:
            raise ValueError("Invalid report format for CSV export")

        output = StringIO()
        writer = csv.writer(output, lineterminator="\n")

        # Dynamically extract headers based on the first log entry
        headers = report["logs"][0].keys() if report["logs"] else []
        writer.writerow(headers)  # Ensure correct column names

        # Write each log entry as a row, handling missing fields gracefully
        for log in report["logs"]:
            writer.writerow([log.get(key, "") for key in headers])

        return output.getvalue()


class JSONExporter(ReportExporter):
    """Exports structured log reports in JSON format.

    Converts log data into a human-readable JSON string.
    """

    def export(self, report):
        """Convert structured report data into JSON format.

        :param report: Dictionary containing log entries.
        :return: JSON-formatted report as a string.
        :raises ValueError: If the report format is invalid.
        """
        if not isinstance(report, dict):
            raise ValueError("Invalid report format for JSON export")

        return json.dumps(report, indent=4)
