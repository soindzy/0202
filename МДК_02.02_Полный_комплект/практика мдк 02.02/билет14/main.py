def average_wrong(a, b):
    return a + b / 2

def average_correct(a, b):
    return (a + b) / 2

test_cases = [
    {"a": 10, "b": 20, "expected": 15.0, "description": "Два положительных целых числа"},
    {"a": 3.5, "b": 4.5, "expected": 4.0, "description": "Вещественные числа"},
    {"a": -5, "b": 15, "expected": 5.0, "description": "Отрицательное и положительное"}
]

print("Сравнение неправильного и правильного алгоритмов:")
print("=" * 70)

for i, test in enumerate(test_cases, 1):
    a = test["a"]
    b = test["b"]
    expected = test["expected"]
    description = test["description"]
    
    wrong_result = average_wrong(a, b)
    correct_result = average_correct(a, b)
    
    print(f"\nТест {i}: {description}")
    print(f"  Входные данные: a = {a}, b = {b}")
    print(f"  Ожидаемый результат: {expected}")
    print(f"  Неправильный алгоритм (a + b/2): {wrong_result}")
    print(f"  Правильный алгоритм ((a + b)/2): {correct_result}")
    
    if abs(correct_result - expected) < 1e-9:
        print(f" Правильный алгоритм: ПРОЙДЕН")
    else:
        print(f" Правильный алгоритм: ПРОВАЛЕН")