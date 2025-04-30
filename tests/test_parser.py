import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)
import unittest
from src.parser import parse_log_entry


class TestParser(unittest.TestCase):
    def test_parse_log_entry(self):
        log_entry = "2025-04-29 14:04:02 ERROR Something went wrong"
        expected_output = {
            "timestamp": "2025-04-29 14:04:02",
            "level": "ERROR",
            "message": "Something went wrong",
        }
        self.assertEqual(parse_log_entry(log_entry), expected_output)

    def test_parse_invalid_log_entry(self):
        log_entry = "Invalid log format that doesn't match"
        expected_output = None
        self.assertEqual(parse_log_entry(log_entry), expected_output)


if __name__ == "__main__":
    unittest.main()
