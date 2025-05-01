import sys
import os
import json

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

import unittest
from src.reporter import (
    generate_summary_report,
    generate_structured_report,
    export_report_csv,
    export_report_json,
)


class TestReporter(unittest.TestCase):
    """Tests for generating log summary reports."""

    def test_grouped_summary(self):
        """Test generating a grouped summary report from logs."""
        log_entries = [
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
            {
                "timestamp": "2025-05-01 10:10:00",
                "level": "WARNING",
                "message": "High memory usage",
            },
            {
                "timestamp": "2025-05-01 10:15:00",
                "level": "ERROR",
                "message": "Disk failure",
            },
            {
                "timestamp": "2025-05-01 10:20:00",
                "level": "INFO",
                "message": "User login",
            },
        ]

        expected_summary = {"ERROR": 2, "WARNING": 1, "INFO": 2}

        self.assertEqual(generate_summary_report(log_entries), expected_summary)

    def test_structured_summary_output(self):
        """Test if Reporter generates structured JSON-like output."""
        log_entries = [
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
            {
                "timestamp": "2025-05-01 10:10:00",
                "level": "WARNING",
                "message": "High memory usage",
            },
        ]

        expected_output = {
            "summary": {"ERROR": 1, "WARNING": 1, "INFO": 1},
            "logs": log_entries,
        }

        self.assertEqual(generate_structured_report(log_entries), expected_output)

    def test_export_csv(self):
        """Test exporting log reports to CSV format."""
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

        self.assertEqual(export_report_csv(report), expected_csv)

    def test_export_json(self):
        """Test exporting log reports to JSON format."""
        report = {
            "summary": {"ERROR": 2, "INFOR": 1},
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
        self.assertEqual(export_report_json(report), expected_json)


if __name__ == "__main__":
    unittest.main()
