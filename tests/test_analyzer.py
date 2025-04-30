import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.analyzer import categorize_log

if __name__ == "__main__":  # pragma: no cover
    unittest.main()


class TestAnalyzer(unittest.TestCase):
    def test_categorize_log(self):
        test_cases = [
            ({"level": "ERROR"}, "Critical Issue"),
            ({"level": "WARNING"}, "Potential Problem"),
            ({"level": "INFO"}, "General Info"),
            ({"level": "DEBUG"}, "Unknown Category"),  # Unrecognized level
            ({"level": ""}, "Unknown Category"),  # Empty level
            ({}, "Unknown Category"),  # Missing level
            ({"level": "error"}, "Critical Issue"),  # Lowercase input
            ({"level": "  WARNING  "}, "Potential Problem"),  # Leading/trailing spaces
        ]

        for log_entry, expected in test_cases:
            with self.subTest(log_entry=log_entry):
                self.assertEqual(categorize_log(log_entry), expected)

    def test_unrecognized_log_levels(self):
        test_cases = [
            {"level": "VERBOSE"},
            {"level": None},
            {"level": 123},
        ]

        for entry in test_cases:
            with self.subTest(log_entry=entry):
                result = categorize_log(entry)
                self.assertEqual(result, "Unknown Category")


if __name__ == "__main__":
    unittest.main()
