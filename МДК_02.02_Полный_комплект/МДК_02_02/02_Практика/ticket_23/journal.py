from division import divide

# Ожидания заданы явно до запуска проверяемой функции.
CASES = [(10, 2, 5.0), (0, 5, 0.0), (-9, 3, -3.0),
         (5, 0, "ZeroDivisionError"), ("abc", 2, "TypeError")]


def collect_results():
    rows = []
    for number, (a, b, expected) in enumerate(CASES, 1):
        try:
            actual = divide(a, b)
        except (ZeroDivisionError, TypeError) as error:
            actual = type(error).__name__
        rows.append({"id": number, "a": repr(a), "b": repr(b),
                     "expected": expected, "actual": actual,
                     "status": "PASS" if actual == expected else "FAIL"})
    return rows


def markdown_journal():
    lines = ["# Журнал тестирования деления", "",
             "| Тест | a | b | Ожидаемый результат | Фактический результат | Статус |",
             "|---|---|---|---|---|---|"]
    for row in collect_results():
        lines.append("| {id} | {a} | {b} | {expected} | {actual} | {status} |".format(**row))
    return "\n".join(lines) + "\n"
