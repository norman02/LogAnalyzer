import unittest
from src.exporters import CSVExporter, JSONExporter


class TestExporters(unittest.TestCase):
    """Test cases for CSV and JSON exporters."""

    def test_csv_invalid_report_format(self):
        """Ensure CSVExporter raises an error for an invalid report format."""
        csv_exporter = CSVExporter()
        with self.assertRaises(ValueError):
            csv_exporter.export({"invalid": "data"})  # ✅ Trigger ValueError

    def test_json_invalid_report_format(self):
        """Ensure JSONExporter raises an error for an invalid report format."""
        json_exporter = JSONExporter()
        with self.assertRaises(ValueError):
            json_exporter.export("Not a dictionary")  # ✅ Trigger ValueError


if __name__ == "__main__":
    unittest.main()
