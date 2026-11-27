def square_number(x):
    return x ** 2

test_cases = [
    {"input": 5, "expected": 25, "description": "Положительное целое число"},
    {"input": -4, "expected": 16, "description": "Отрицательное целое число"},
    {"input": 0, "expected": 0, "description": "Ноль (граничное условие)"},
    {"input": 2.5, "expected": 6.25, "description": "Вещественное число"}
]

print("Запуск тестов для функции square_number:")
print("-" * 50)

all_passed = True

for i, test in enumerate(test_cases, 1):
    input_val = test["input"]
    expected = test["expected"]
    description = test["description"]
    
    result = square_number(input_val)
    
    is_passed = abs(result - expected) < 1e-9
    
    status = " ПРОЙДЕН" if is_passed else " ПРОВАЛЕН"
    
    if not is_passed:
        all_passed = False
        
    print(f"Тест {i}: {description}")
    print(f"  Вход: {input_val}")
    print(f"  Ожидаемо: {expected}")
    print(f"  Получено: {result}")
    print(f"  Статус: {status}")
    print()

if all_passed:
    print(" Все тесты успешно пройдены!")
else:
    print(" Некоторые тесты не пройдены.")