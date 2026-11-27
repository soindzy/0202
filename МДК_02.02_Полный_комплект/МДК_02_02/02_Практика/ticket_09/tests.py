"""Автоматические проверки практического задания."""
import unittest

import tempfile
from repository_demo import demonstrate

class Tests(unittest.TestCase):
    def test_actual_repository(self):
        with tempfile.TemporaryDirectory() as directory:
            result = demonstrate(directory)
            self.assertEqual(result["files"], ["hello.py"])
            self.assertEqual(result["commits"], 1)
            self.assertTrue(result["clean"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
