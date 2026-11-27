"""Автоматические проверки практического задания."""
import unittest

import tempfile
from branch_demo import demonstrate

class Tests(unittest.TestCase):
    def test_branch_and_merge(self):
        with tempfile.TemporaryDirectory() as directory:
            result = demonstrate(directory)
            self.assertEqual(result["branch"], "main")
            self.assertEqual(result["feature"], "Новая функция")
            self.assertEqual(result["parents"], 2)
            self.assertTrue(result["clean"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
