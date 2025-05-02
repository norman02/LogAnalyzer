import os
import sys
import subprocess
import unittest
import logging

logging.disable(logging.CRITICAL)  # Suppresses all logs below CRITICAL
# Ensure the project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.analyzer import LogCategorizer  # Import your categorizer


class TestAnalyzer(unittest.TestCase):
    """Tests for log categorization and main module execution."""

    def setUp(self):
        """Initialize LogCategorizer before each test."""
        self.categorizer = LogCategorizer()

    def test_standard_levels(self):
        """Test categorization for standard severity levels."""
        test_cases = [
            ({"level": "ERROR"}, "Critical Issue"),
            ({"level": "WARNING"}, "Potential Problem"),
            ({"level": "INFO"}, "General Info"),
        ]

        for log_entry, expected in test_cases:
            with self.subTest(log_entry=log_entry):
                self.assertEqual(self.categorizer.categorize(log_entry), expected)

    def test_unrecognized_levels(self):
        """Test handling of unexpected log levels."""
        test_cases = [
            ({"level": "DEBUG"}, "Unknown Category"),
            ({"level": "VERBOSE"}, "Unknown Category"),
            ({"level": "TRACE"}, "Unknown Category"),
            ({"level": "CUSTOM"}, "Unknown Category"),
        ]

        for log_entry, expected in test_cases:
            with self.subTest(log_entry=log_entry):
                self.assertEqual(self.categorizer.categorize(log_entry), expected)

    def test_invalid_inputs(self):
        """Test handling of invalid log entries."""
        test_cases = [
            (None, "Unknown Category"),  # Completely invalid entry
            ([], "Unknown Category"),  # Invalid type: list
            ("ERROR", "Unknown Category"),  # Invalid type: string
            ({"message": "No level here"}, "Unknown Category"),  # Missing "level" key
            ({"level": "   "}, "Unknown Category"),  # Whitespace-only level
            ({"level": None}, "Unknown Category"),  # Null level
            ({"level": 123}, "Unknown Category"),  # Numeric level
        ]

        for log_entry, expected in test_cases:
            with self.subTest(log_entry=log_entry):
                self.assertEqual(self.categorizer.categorize(log_entry), expected)


if __name__ == "__main__":
    unittest.main()
