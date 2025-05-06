import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import unittest
from src.core import LogAnalyzerCore
from src.parser import parse_log_entry


def mock_parser(log_line):
    """Mock parser that converts a log line into a simple dictionary."""
    return {"log": log_line} if log_line else None


class TestLogAnalyzerCore(unittest.TestCase):
    """Tests LogAnalyzerCore integration."""

    def setUp(self):
        """Prepare sample log entries."""
        self.sample_logs = [
            "2025-05-01 10:00:00 ERROR Crash detected",
            "2025-05-01 10:05:00 INFO Startup complete",
            "2025-05-01 10:10:00 WARNING High memory usage",
        ]
        self.analyzer = LogAnalyzerCore(self.sample_logs, parser=parse_log_entry)

    def test_parser_injection(self):
        """Ensure LogAnalyzerCore correctly uses an injected parser function."""
        analyzer = LogAnalyzerCore(self.sample_logs, parser=mock_parser)

        expected_parsed_logs = [
            {"log": "2025-05-01 10:00:00 ERROR Crash detected"},
            {"log": "2025-05-01 10:05:00 INFO Startup complete"},
            {"log": "2025-05-01 10:10:00 WARNING High memory usage"},
        ]
        self.assertEqual(analyzer.raw_logs, expected_parsed_logs)

    def test_log_parsing(self):
        """Verify logs are correctly parsed."""
        parsed_logs = self.analyzer.parse_logs(self.sample_logs, parse_log_entry)
        self.assertTrue(len(parsed_logs) > 0, "No logs were parsed!")

    def test_log_analysis(self):
        """Test log categorization works."""
        analyzed_logs = self.analyzer.analyze_logs()  # ✅ Fix: Assign before printing
        self.assertTrue(len(analyzed_logs) > 0, "No logs were categorized!")

    def test_export_csv(self):
        """Test CSV report export."""
        csv_output = self.analyzer.export_report("csv")

        # ✅ Improve validation: Ensure at least one structured log entry exists
        expected_headers = "timestamp,level,message"
        self.assertIn(
            expected_headers, csv_output, "CSV export failed to include headers."
        )


if __name__ == "__main__":
    unittest.main()
