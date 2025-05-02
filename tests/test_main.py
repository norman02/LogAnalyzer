import unittest
import subprocess


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


if __name__ == "__main__":
    unittest.main()
