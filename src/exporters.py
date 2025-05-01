from abc import ABC, abstractmethod
import csv
import json
from io import StringIO


class ReportExporter(ABC):
    """Abstract base class for exporting reports."""

    @abstractmethod
    def export(self, report):
        """Export report in a specific format."""
        pass


class CSVExporter(ReportExporter):
    """Exports report in CSV format."""

    def export(self, report):
        output = StringIO()
        writer = csv.writer(output, lineterminator="\n")
        writer.writerow(["timestamp", "level", "message"])
        for log in report["logs"]:
            writer.writerow([log["timestamp"], log["level"], log["message"]])
        return output.getvalue()


class JSONExporter(ReportExporter):
    """Exports report in JSON format."""

    def export(self, report):
        return json.dumps(report, indent=4)
