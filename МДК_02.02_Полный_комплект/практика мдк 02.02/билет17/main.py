def sort_sequence(seq):
    return sorted(seq)
test_cases = [
    {
        "input": [],
        "expected": [],
        "description": "Пустая последовательность"
    },
    {
        "input": [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
        "expected": [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9],
        "description": "Повторяющиеся значения"
    },
    {
        "input": [5, 4, 3, 2, 1],
        "expected": [1, 2, 3, 4, 5],
        "description": "Обратный порядок"
    },
    {
        "input": [42],
        "expected": [42],
        "description": "Одноэлементная последовательность"
    },
    {
        "input": [3.14, -2, 0, 7, -5.5, 1, 0],
        "expected": [-5.5, -2, 0, 0, 1, 3.14, 7],
        "description": "Смешанные значения"
    }
]

print("Запуск тестов модуля сортировки:")
print("=" * 60)

all_passed = True

for i, test in enumerate(test_cases, 1):
    input_val = test["input"]
    expected = test["expected"]
    description = test["description"]
    
    result = sort_sequence(input_val)
    is_passed = result == expected
    
    if not is_passed:
        all_passed = False
    
    status = " ПРОЙДЕН" if is_passed else " ПРОВАЛЕН"
    
    print(f"\nТест {i}: {description}")
    print(f"  Вход:    {input_val}")
    print(f"  Ожидаемо: {expected}")
    print(f"  Получено: {result}")
    print(f"  Статус:  {status}")

print("\n" + "=" * 60)
if all_passed:
    print(" Все тесты успешно пройдены!")
else:
    print(" Некоторые тесты не пройдены.")