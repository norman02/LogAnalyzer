import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.core import LogAnalyzerCore
import unittest


class TestLogAnalyzerCore(unittest.TestCase):
    """Tests LogAnalyzerCore integration."""

    def setUp(self):
        """Prepare sample log entries."""
        self.sample_logs = [
            "2025-05-01 10:00:00 ERROR Crash detected",
            "2025-05-01 10:05:00 INFO Startup complete",
            "2025-05-01 10:10:00 WARNING High memory usage",
        ]
        self.analyzer = LogAnalyzerCore(self.sample_logs)

    def test_log_parsing(self):
        """Verify logs are correctly parsed."""
        self.assertEqual(len(self.analyzer.parsed_logs), 3)
        self.assertEqual(self.analyzer.parsed_logs[0]["level"], "ERROR")

    def test_log_analysis(self):
        """Test log categorization works."""
        categorized_logs = self.analyzer.analyze_logs()
        self.assertEqual(categorized_logs[0]["category"], "Critical Issue")

    def test_export_csv(self):
        """Test CSV report export."""
        csv_output = self.analyzer.export_report("csv")
        self.assertIn("timestamp,level,message", csv_output)


if __name__ == "__main__":
    unittest.main()
