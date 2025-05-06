import unittest
import subprocess
import os
import sys

from src.main import get_logs_from_file

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


class TestMainExecution(unittest.TestCase):
    """Tests main.py execution as an entry point."""

    def test_main_runs(self):
        """Ensure main.py executes without emitting output."""
        result = subprocess.run(
            [
                "python3",
                "-m",
                "src.main",
            ],  # Invoking as a module for proper package context.
            stdout=subprocess.DEVNULL,  # Suppresses STDOUT.
            stderr=subprocess.DEVNULL,  # Suppresses STDERR.
        )
        self.assertEqual(result.returncode, 0, "main.py did not execute successfully.")

    def test_log_retrieval(self):
        """Ensure logs are retrieved correctly."""
        logs = get_logs_from_file()

        self.assertTrue(len(logs) > 0, "No logs were retrieved!")


if __name__ == "__main__":
    unittest.main()
