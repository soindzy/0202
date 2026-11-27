def convert_to_integer(text):
    try:
        result = int(text)
        return result
    except ValueError:
        return f"Ошибка: '{text}' не является допустимым целым числом"
    except TypeError:
        return f"Ошибка: ожидалась строка, получено {type(text).__name__}"

test_cases = [
    "15",   
    "abc",  
]

print("Результаты тестирования:")
print("=" * 60)

for i, test_input in enumerate(test_cases, 1):
    result = convert_to_integer(test_input)
    print(f"\nТест {i}:")
    print(f"  Входные данные: '{test_input}'")
    print(f"  Тип результата: {type(result).__name__}")
    print(f"  Результат: {result}")