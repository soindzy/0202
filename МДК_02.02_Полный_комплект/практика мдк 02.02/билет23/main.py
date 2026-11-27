def divide(a, b):

    try:
        if b == 0:
            raise ZeroDivisionError("Деление на ноль")
        return a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"
    except Exception as e:
        return f"Ошибка: {str(e)}"

test_cases = [
    {
        "id": "TC-01",
        "description": "Деление целых чисел без остатка",
        "input": {"a": 10, "b": 2},
        "expected": 5.0
    },
    {
        "id": "TC-02",
        "description": "Деление на ноль (обработка ошибки)",
        "input": {"a": 5, "b": 0},
        "expected": "Ошибка: деление на ноль"
    },
    {
        "id": "TC-03",
        "description": "Деление вещественных чисел",
        "input": {"a": 7.5, "b": 2.5},
        "expected": 3.0
    },
    {
        "id": "TC-04",
        "description": "Деление отрицательного числа на положительное",
        "input": {"a": -8, "b": 4},
        "expected": -2.0
    }
]

print("=" * 80)
print("ЖУРНАЛ ТЕСТИРОВАНИЯ ОПЕРАЦИИ ДЕЛЕНИЯ ДВУХ ЧИСЕЛ")
print("=" * 80)
print(f"Дата проведения: 24.11.2026")
print(f"Объект тестирования: Функция divide(a, b)")
print("=" * 80)
print()

results = []
all_passed = True

for test in test_cases:
    test_id = test["id"]
    description = test["description"]
    a = test["input"]["a"]
    b = test["input"]["b"]
    expected = test["expected"]
    
    actual = divide(a, b)
    
    if isinstance(expected, float):
        is_passed = abs(actual - expected) < 1e-9
    else:
        is_passed = actual == expected
    
    status = "УСпешно" if is_passed else "Не успешно"
    
    if not is_passed:
        all_passed = False
    
    results.append({
        "id": test_id,
        "description": description,
        "input": f"a={a}, b={b}",
        "expected": expected,
        "actual": actual,
        "status": status
    })

print(f"{'ID':<8} {'Описание':<40} {'Вход':<15} {'Ожидаемо':<20} {'Фактически':<20} {'Статус':<12}")
print("-" * 120)

for result in results:
    print(f"{result['id']:<8} {result['description']:<40} {result['input']:<15} {str(result['expected']):<20} {str(result['actual']):<20} {result['status']:<12}")

print("-" * 120)
print()

print("=" * 80)
print("ИТОГОВОЕ ЗАКЛЮЧЕНИЕ")
print("=" * 80)
if all_passed:
    print(" Все тесты пройдены успешно!")
    print("Функция деления работает корректно для всех проверенных сценариев.")
else:
    print(" Некоторые тесты не пройдены.")
    print("Обнаружены дефекты в работе функции.")
print("=" * 80)