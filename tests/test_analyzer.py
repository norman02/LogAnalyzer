import unittest
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)
from src.analyzer import categorize_log


class TestAnalyzer(unittest.TestCase):
    def test_categorize_log(self):
        log_entry = {
            "timestamp": "2025-04-29 14:04:02",
            "level": "ERROR",
            "message": "Something went wrong",
        }
        expected_output = "Critical Issue"
        self.assertEqual(categorize_log(log_entry), expected_output)


if __name__ == "__main__":
    unittest.main()
