def divide_numbers(a, b):
  
    if b == 0:
        return "Ошибка: деление на ноль невозможно!"
    else:
        return a / b

test_cases = [
    (10, 2),    
    (5, 0),     
    (-8, 4),    
    (7.5, 2.5), 
    (0, 3),     
]

print("Результаты тестирования:")
for i, (a, b) in enumerate(test_cases, 1):
    result = divide_numbers(a, b)
    print(f"Тест {i}: {a} / {b} = {result}")