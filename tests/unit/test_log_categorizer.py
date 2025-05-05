import unittest
from src.analyzer import LogCategorizer


class TestLogCategorizer(unittest.TestCase):
    def test_invalid_entry_logs_warning(self):
        """Verify that an invalid log entry triggers a warning log."""

        categorizer = LogCategorizer()

        # Create a list to record warning messages
        warning_messages = []

        # Save the original log_warning method (optional, if you need to call it)
        original_log_warning = categorizer.log_warning

        # Override the log_warning method so it appends messages to our list.
        def fake_log_warning(message):
            warning_messages.append(message)
            # Optionally, you can also call the original if desired:
            # original_log_warning(message)

        categorizer.log_warning = fake_log_warning

        # Call categorize with an invalid input (not a dict)
        categorizer.categorize("Invalid Entry")

        # Assert that a warning message was recorded and that it contains the expected text.
        self.assertTrue(
            any("Invalid log entry type" in w for w in warning_messages),
            "Expected warning log not found!",
        )


if __name__ == "__main__":
    unittest.main()
