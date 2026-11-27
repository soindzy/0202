"""Автоматические проверки практического задания."""
import unittest

import tempfile
from conflict_demo import demonstrate

class Tests(unittest.TestCase):
    def test_real_conflict_resolution(self):
        with tempfile.TemporaryDirectory() as directory:
            result = demonstrate(directory)
            self.assertIn("<<<<<<<", result["conflict"])
            self.assertIn("=======", result["conflict"])
            self.assertIn(">>>>>>>", result["conflict"])
            self.assertEqual(result["result"], "timeout = 30\n")
            self.assertEqual(result["unmerged"], "")
            self.assertEqual(result["parents"], 2)
            self.assertTrue(result["clean"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
