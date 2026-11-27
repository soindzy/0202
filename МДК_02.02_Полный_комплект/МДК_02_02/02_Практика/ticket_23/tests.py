"""Автоматические проверки практического задания."""
import unittest

from journal import collect_results, markdown_journal

class Tests(unittest.TestCase):
    def test_measured_results(self):
        rows = collect_results()
        self.assertEqual(len(rows), 5)
        self.assertEqual([row["actual"] for row in rows], [5.0, 0.0, -3.0, "ZeroDivisionError", "TypeError"])
        self.assertTrue(all(row["status"] == "PASS" for row in rows))
    def test_journal(self):
        self.assertIn("Фактический результат", markdown_journal())
        self.assertEqual(markdown_journal().count("| PASS |"), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
