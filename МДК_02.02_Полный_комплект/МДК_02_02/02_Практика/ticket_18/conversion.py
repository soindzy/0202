def parse_integer(text):
    if not isinstance(text, str):
        raise TypeError("Ожидается текстовая строка")
    try:
        return int(text)
    except ValueError:
        raise ValueError("Введите целое число, например 15") from None
