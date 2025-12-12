import io
import json
import tempfile
import unittest
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast
from unittest.mock import patch

from flake8.formatting import base

from flake8_sarif_formatter.flake8_sarif_formatter import SarifFormatter


@dataclass(frozen=True)
class FakeViolation:
    code: str
    text: str
    filename: str
    line_number: int
    column_number: int


class TestSarifFormatter(unittest.TestCase):
    def _make_formatter(self, rules):
        formatter = SarifFormatter.__new__(SarifFormatter)
        formatter.output_fd = io.StringIO()

        with patch("flake8_sarif_formatter.flake8_sarif_formatter.get_flake8_rules", return_value=rules):
            SarifFormatter.after_init(formatter)

        return formatter

    def test_handle_adds_result_and_rule(self):
        rules = {"E501": {"message": "Line too long"}}
        formatter = self._make_formatter(rules)

        with tempfile.TemporaryDirectory() as tmp:
            file_path = Path(tmp) / "example.py"
            file_path.write_text("print('x')\n", encoding="utf-8")

            SarifFormatter.handle(
                formatter,
                cast(Any, FakeViolation(
                    code="E501",
                    text="Line too long",
                    filename=str(file_path),
                    line_number=3,
                    column_number=10,
                )),
            )

        self.assertEqual(len(formatter.sarif_results), 1)
        self.assertEqual(len(formatter.sarif_rules), 1)

        result = formatter.sarif_results[0]
        self.assertEqual(result["ruleId"], "flake8/E501")
        self.assertEqual(result["message"]["text"], "Line too long")

        location = result["locations"][0]["physicalLocation"]
        self.assertTrue(location["artifactLocation"]["uri"].startswith("file:"))
        self.assertEqual(location["region"]["startLine"], 3)
        self.assertEqual(location["region"]["startColumn"], 10)
        self.assertEqual(location["region"]["endLine"], 3)
        self.assertEqual(location["region"]["endColumn"], 10)

        rule = formatter.sarif_rules[0]
        self.assertEqual(rule["id"], "flake8/E501")
        self.assertEqual(rule["shortDescription"]["text"], "Line too long")

    def test_handle_dedupes_rules(self):
        rules = {"F401": {"message": "Unused import"}}
        formatter = self._make_formatter(rules)

        SarifFormatter.handle(
            formatter,
            cast(Any, FakeViolation(code="F401", text="Unused import os", filename="a.py", line_number=1, column_number=1)),
        )
        SarifFormatter.handle(
            formatter,
            cast(Any, FakeViolation(code="F401", text="Unused import sys", filename="b.py", line_number=2, column_number=4)),
        )

        self.assertEqual(len(formatter.sarif_results), 2)
        self.assertEqual(len(formatter.sarif_rules), 1)

    def test_stop_emits_valid_sarif_json(self):
        rules = {"E123": {"message": "Example rule"}}
        formatter = self._make_formatter(rules)

        SarifFormatter.handle(
            formatter,
            cast(Any, FakeViolation(code="E123", text="Example error", filename="a.py", line_number=1, column_number=1)),
        )

        with patch.object(base.BaseFormatter, "stop", return_value=None):
            SarifFormatter.stop(formatter)

        output = formatter.output_fd.getvalue()
        sarif = json.loads(output)

        self.assertEqual(sarif["version"], "2.1.0")
        self.assertIn("runs", sarif)
        self.assertEqual(sarif["runs"][0]["tool"]["driver"]["name"], "Flake8")
        self.assertEqual(len(sarif["runs"][0]["results"]), 1)
        self.assertEqual(len(sarif["runs"][0]["tool"]["driver"]["rules"]), 1)


if __name__ == "__main__":
    unittest.main()
