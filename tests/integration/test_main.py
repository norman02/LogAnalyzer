import unittest
import os
import logging
from src.main import get_logs_from_file, main


class TestMainExecution(unittest.TestCase):
    """Tests for the main execution logic in main.py (without error logging test)."""

    def setUp(self):
        """Create a temporary log file for testing purposes."""
        self.test_log_file = "test_logs.txt"
        with open(self.test_log_file, "w") as temp_log:
            temp_log.write("2025-05-01 10:00:00 ERROR Crash detected\n")

    def tearDown(self):
        """Cleanup test artifacts."""
        for file in [self.test_log_file, "error.log"]:
            if os.path.exists(file):
                os.remove(file)
        logging.shutdown()

    def test_log_retrieval(self):
        """Ensure logs are retrieved correctly from a valid log file."""
        logs = get_logs_from_file(self.test_log_file)
        self.assertTrue(len(logs) > 0, "No logs were retrieved!")

    def test_main_runs(self):
        """Ensure main.py executes successfully with a valid log file."""
        result = main(log_file=self.test_log_file, export_format="csv")
        self.assertEqual(result, 0, "main.py did not execute successfully.")


if __name__ == "__main__":
    unittest.main()
