import json
import unittest
from src.reporter import generate_structured_report, export_report
from src.exporters import CSVExporter, JSONExporter


class TestReporter(unittest.TestCase):
    """Tests for exporting log reports dynamically."""

    def test_export_csv(self):
        report = {
            "summary": {"ERROR": 2, "INFO": 1},
            "logs": [
                {
                    "timestamp": "2025-05-01 10:00:00",
                    "level": "ERROR",
                    "message": "Crash detected",
                },
                {
                    "timestamp": "2025-05-01 10:05:00",
                    "level": "INFO",
                    "message": "Startup complete",
                },
            ],
        }
        expected_csv = "timestamp,level,message\n2025-05-01 10:00:00,ERROR,Crash detected\n2025-05-01 10:05:00,INFO,Startup complete\n"
        self.assertEqual(export_report(report, CSVExporter()), expected_csv)

    def test_export_json(self):
        report = {
            "summary": {"ERROR": 2, "INFO": 1},
            "logs": [
                {
                    "timestamp": "2025-05-01 10:00:00",
                    "level": "ERROR",
                    "message": "Crash detected",
                },
                {
                    "timestamp": "2025-05-01 10:05:00",
                    "level": "INFO",
                    "message": "Startup complete",
                },
            ],
        }
        expected_json = json.dumps(report, indent=4)
        self.assertEqual(export_report(report, JSONExporter()), expected_json)
