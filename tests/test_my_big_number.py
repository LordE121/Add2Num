import subprocess
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from my_big_number import MyBigNumber


class TestMyBigNumber(unittest.TestCase):
    def setUp(self):
        self.calculator = MyBigNumber()

    def test_sample_from_requirement(self):
        self.assertEqual(self.calculator.sum("1234", "897"), "2131")

    def test_different_lengths(self):
        self.assertEqual(self.calculator.sum("1000", "23"), "1023")

    def test_final_carry(self):
        self.assertEqual(self.calculator.sum("999", "1"), "1000")

    def test_very_large_numbers(self):
        self.assertEqual(
            self.calculator.sum("123456789123456789", "987654321987654321"),
            "1111111111111111110",
        )

    def test_zero_values(self):
        self.assertEqual(self.calculator.sum("0", "0"), "0")


class TestCli(unittest.TestCase):
    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "main.py", *args],
            check=True,
            capture_output=True,
            cwd=PROJECT_ROOT,
            text=True,
        )

    def test_cli_prints_sum(self):
        completed = self.run_cli("1234", "897")

        self.assertEqual(completed.stdout.strip(), "2131")

    def test_cli_can_print_operation_log(self):
        completed = self.run_cli("99", "1", "--log")

        self.assertIn("Step 1:", completed.stderr)
        self.assertEqual(completed.stdout.strip(), "100")


if __name__ == "__main__":
    unittest.main()
