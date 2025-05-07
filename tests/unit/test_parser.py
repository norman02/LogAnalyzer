import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.parser import parse_log_entry
import unittest


class TestParser(unittest.TestCase):
    def test_standard_format(self):
        """Test parsing a correctly formatted log entry"""
        log_entry = "2025-04-29 14:04:02 ERROR Something went wrong"
        expected_output = {
            "timestamp": "2025-04-29 14:04:02",
            "level": "ERROR",
            "message": "Something went wrong",
        }
        self.assertEqual(parse_log_entry(log_entry), expected_output)

    def test_missing_timestamp(self):
        """Test log entry without a timestamp."""
        log_entry = "ERROR Something went wrong"
        expected = None

        self.assertEqual(parse_log_entry(log_entry), expected)

    def test_missing_log_level(self):
        """Test log entry without a log level."""
        log_entry = "2025-04-30 09:27:00 Something went wrong"
        expected = None

        self.assertEqual(parse_log_entry(log_entry), expected)

    def test_empty_log_entry(self):
        """Ensure an empty log entry returns None."""
        self.assertIsNone(parse_log_entry(""), "Empty log should return None")
        self.assertIsNone(parse_log_entry(None), "None input should return None")
        self.assertIsNone(
            parse_log_entry("  "), "Whitespace-only log should return None"
        )


if __name__ == "__main__":
    unittest.main()
