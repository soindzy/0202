"""Автоматические проверки практического задания."""
import unittest

from pathlib import Path
import tempfile
from helper import greeting
from git_support import init_repository, git_run

class Tests(unittest.TestCase):
    def test_module(self):
        self.assertIn("модуль", greeting())
    def test_ignore_rules(self):
        with tempfile.TemporaryDirectory() as temp:
            repo = init_repository(temp)
            content = Path(__file__).with_name(".gitignore").read_text(encoding="utf-8")
            (repo / ".gitignore").write_text(content, encoding="utf-8")
            for name in ["__pycache__/x.pyc", ".venv/a.py", "draft.tmp", "run.log", "build/a", ".env"]:
                with self.subTest(ignored=name):
                    self.assertEqual(git_run(repo, "check-ignore", "--no-index", name, check=False).returncode, 0)
            for name in ["main.py", "helper.py", "tests.py", "docs/PROJECT.md", "README.md"]:
                with self.subTest(tracked=name):
                    self.assertEqual(git_run(repo, "check-ignore", "--no-index", name, check=False).returncode, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
