import unittest
import os
import logging
import time
from src.main import get_logs_from_file, main


class TestMainExecution(unittest.TestCase):
    """Tests for the main execution logic in main.py."""

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

    def test_file_not_found_error(self):
        """Ensure FileNotFoundError is handled properly."""
        exit_code = main(log_file="missing_logs.txt")
        time.sleep(0.1)  # Allow time for logs to be flushed/written.
        self.assertEqual(exit_code, 1, "Main should return 1 on failure.")
        self.assertTrue(
            os.path.exists("error.log"), "Error log file should be created."
        )

    def test_successful_execution(self):
        """Ensure main.py runs successfully with a valid log file."""
        result = main(log_file=self.test_log_file, export_format="csv")
        self.assertEqual(result, 0, "Main should return 0 on successful execution.")


if __name__ == "__main__":
    unittest.main()
