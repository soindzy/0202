def is_even(number):
    return number % 2 == 0

test_cases = [
    {
        "input": 4,
        "expected": True,
        "description": "Чётное положительное число"
    },
    {
        "input": 7,
        "expected": False,
        "description": "Нечётное положительное число"
    },
    {
        "input": 0,
        "expected": True,
        "description": "Ноль (граничный случай)"
    },
    {
        "input": -3,
        "expected": False,
        "description": "Отрицательное нечётное число"
    }
]

print("Автоматизированные проверки функции is_even:")
print("=" * 60)

all_passed = True

for i, test in enumerate(test_cases, 1):
    input_val = test["input"]
    expected = test["expected"]
    description = test["description"]
    
    result = is_even(input_val)
    is_passed = result == expected
    
    if not is_passed:
        all_passed = False
    
    status = " ПРОЙДЕН" if is_passed else " ПРОВАЛЕН"
    
    print(f"\nТест {i}: {description}")
    print(f"  Входные данные: {input_val}")
    print(f"  Ожидаемый результат: {expected}")
    print(f"  Фактический результат: {result}")
    print(f"  Статус: {status}")

print("\n" + "=" * 60)
if all_passed:
    print(" Все  проверки успешно пройдены!")
else:
    print(" Некоторые проверки не пройдены.")