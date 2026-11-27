"""Повторная проверка всех практических работ. Только стандартная библиотека."""
import ast
from datetime import datetime, timezone
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def execute(path, script, env):
    try:
        result = subprocess.run([sys.executable, "-X", "utf8", script], cwd=path,
                                env=env, capture_output=True, text=True,
                                encoding="utf-8", errors="replace", timeout=120)
        return result.returncode, result.stdout + result.stderr
    except subprocess.TimeoutExpired as error:
        return 124, f"Превышен тайм-аут: {error}"


def main():
    env = os.environ.copy()
    env.pop("PYTHONPATH", None)
    env["PYTHONIOENCODING"] = "utf-8"
    logs = ROOT / "verification_logs"
    logs.mkdir(exist_ok=True)
    report = ["# Отчёт о проверке практических работ МДК 02.02", "",
              "Дата UTC: " + datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
              "Python: " + sys.version.split()[0], "",
              "Проверки: синтаксис всех .py, автоматические тесты unittest, запуск main.py.",
              "Ожидания в тестах заданы независимо от проверяемых функций.", "",
              "| Билет | Синтаксис | Методов тестирования | Тесты | Демонстрация |",
              "|---|---|---|---|---|"]
    passed = 0
    total_tests = 0
    total_sources = 0
    imports = set()
    for number in range(1, 26):
        folder = ROOT / f"ticket_{number:02d}"
        syntax_ok = True
        details = []
        for source in sorted(folder.rglob("*.py")):
            try:
                text = source.read_text(encoding="utf-8")
                compile(text, source.name, "exec")
                total_sources += 1
                for node in ast.walk(ast.parse(text)):
                    if isinstance(node, ast.Import):
                        imports.update(item.name.split(".")[0] for item in node.names)
                    elif isinstance(node, ast.ImportFrom) and node.module:
                        imports.add(node.module.split(".")[0])
            except (SyntaxError, UnicodeError) as error:
                syntax_ok = False
                details.append(str(error))
        test_code, test_output = execute(folder, "tests.py", env)
        demo_code, demo_output = execute(folder, "main.py", env)
        match = re.search(r"Ran (\d+) tests?", test_output)
        count = int(match.group(1)) if match else 0
        total_tests += count
        tests_ok = test_code == 0 and count > 0
        demo_ok = demo_code == 0
        ok = syntax_ok and tests_ok and demo_ok
        passed += int(ok)
        status = lambda value: "PASS" if value else "FAIL"
        report.append(f"| {number:02d} | {status(syntax_ok)} | {count} | {status(tests_ok)} | {status(demo_ok)} |")
        log = "СИНТАКСИС\n" + ("OK" if syntax_ok else "\n".join(details))
        log += "\n\nТЕСТЫ\n" + test_output + "\nДЕМОНСТРАЦИЯ\n" + demo_output
        (logs / f"ticket_{number:02d}.txt").write_text(log, encoding="utf-8")
        print(f"Билет {number:02d}: {status(ok)}, тестовых методов: {count}")
    local_modules = {p.stem for p in ROOT.rglob("*.py")}
    external = sorted(imports - local_modules - set(sys.stdlib_module_names))
    report.extend(["", f"Итог: {passed}/25 билетов прошли проверки.",
                   f"Всего методов тестирования: {total_tests}. Внутри отдельных методов также выполняются проверки нескольких случаев через subTest.",
                   f"Проверено Python-файлов в билетах: {total_sources}.",
                   "Сторонние Python-импорты: " + (", ".join(external) if external else "не обнаружены"),
                   "", "Git в билетах 08–11 вызывается как отдельная программа, а не Python-пакет.",
                   "Подробности каждого запуска: verification_logs/ticket_XX.txt."])
    (ROOT / "CHECK_REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"Итого: {passed}/25; методов тестирования: {total_tests}.")
    return 0 if passed == 25 and not external else 1


if __name__ == "__main__":
    raise SystemExit(main())
