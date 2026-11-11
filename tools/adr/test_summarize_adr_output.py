import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from summarize_adr_output import parse_report, render_report


FIXTURE = """\
DON checker ADR validation output
===== api/one =====
Diagnostics: 3 (errors 2, warnings 1, info 0, hints 0)

Errors (2)
  1. rule:error
     message: First | value
  2. rule:error
     message: Second value
Warnings (1)
  3. rule:warning
     message: Warning

===== api/two =====
Diagnostics: 2 (errors 1, warnings 0, info 1, hints 0)
Errors (1)
  1. rule:error
     message: First | value
Info (1)
  2. rule:info
     message: Informational
"""


class SummaryTests(unittest.TestCase):
    def test_counts_variants_and_escapes_markdown(self):
        report = render_report(parse_report(FIXTURE), Path("input.txt"))
        self.assertIn("| Errors | 3 |", report)
        self.assertIn("| Warnings | 1 |", report)
        self.assertIn("| rule:error | 3 | 2 | First \\| value |", report)
        self.assertIn("| api/two | 1 | 0 | 1 |", report)
        self.assertIn("1 info-meldingen en 0 hints", report)

    def test_zero_diagnostics(self):
        result = parse_report(
            "===== empty =====\n"
            "Diagnostics: 0 (errors 0, warnings 0, info 0, hints 0)\n"
        )
        self.assertIn("| empty | 0 | 0 | 0 |", render_report(result, Path("input")))

    def test_rejects_missing_message_and_incomplete_sections(self):
        with self.assertRaisesRegex(ValueError, "melding.*ontbreekt"):
            parse_report(FIXTURE.replace("     message: Warning\n", ""))
        with self.assertRaisesRegex(ValueError, "komen niet overeen"):
            parse_report(FIXTURE.replace("errors 2, warnings 1", "errors 1, warnings 2"))
        with self.assertRaisesRegex(ValueError, "diagnostiektotalen ontbreekt"):
            parse_report("===== missing =====\nDirectory not found\n")
        with self.assertRaisesRegex(ValueError, "Geen validatieresultaten"):
            parse_report("unexpected output\n")

    def test_cli_preserves_existing_output_on_invalid_input(self):
        script = Path(__file__).with_name("summarize_adr_output.py")
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "input.txt"
            output = Path(directory) / "output.md"
            source.write_text("invalid", encoding="utf-8")
            output.write_text("existing", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(script), str(source), "-o", str(output)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("Fout bij verwerken", completed.stderr)
            self.assertEqual(output.read_text(encoding="utf-8"), "existing")


if __name__ == "__main__":
    unittest.main()
