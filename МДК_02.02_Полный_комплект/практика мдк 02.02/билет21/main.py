def sum_sequence_wrong(sequence):
    total = 0
    for num in sequence:
        total = num  
    return total

def sum_sequence_correct(sequence):
    total = 0
    for num in sequence:
        total = total + num  
    return total

test_case = {
    "input": [1, 2, 3, 4, 5],
    "expected": 15,
    "description": "Сумма последовательности [1, 2, 3, 4, 5]"
}

print("Проверочный тест для алгоритма суммирования:")
print("=" * 60)

input_seq = test_case["input"]
expected = test_case["expected"]

wrong_result = sum_sequence_wrong(input_seq)
correct_result = sum_sequence_correct(input_seq)

print(f"\nВходные данные: {input_seq}")
print(f"Ожидаемый результат: {expected}")
print(f"\nРезультат НЕПРАВИЛЬНОГО алгоритма: {wrong_result}")
print(f"  - Возвращает последний элемент, а не сумму!")

print(f"\nРезультат ПРАВИЛЬНОГО алгоритма: {correct_result}")

if correct_result == expected:
    print(f"\n ПРАВИЛЬНЫЙ алгоритм: ПРОЙДЕН тест")
else:
    print(f"\n ПРАВИЛЬНЫЙ алгоритм: ПРОВАЛЕН тест")

if wrong_result == expected:
    print(f"  НЕПРАВИЛЬНЫЙ алгоритм случайно дал верный ответ")
else:
    print(f" НЕПРАВИЛЬНЫЙ алгоритм: ПРОВАЛЕН тест")

print("\n" + "=" * 60)
print("Пошаговая демонстрация работы обоих алгоритмов:")
print("-" * 60)
print(f"{'Элемент':<10}{'Неправильный total':<22}{'Правильный total':<20}")
print("-" * 60)

wrong_total = 0
correct_total = 0
for num in input_seq:
    wrong_total = num
    correct_total = correct_total + num
    print(f"{num:<10}{wrong_total:<22}{correct_total:<20}")

print("-" * 60)
print(f"{'ИТОГ:':<10}{wrong_total:<22}{correct_total:<20}")