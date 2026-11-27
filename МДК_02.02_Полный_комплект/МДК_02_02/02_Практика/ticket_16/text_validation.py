def is_nonempty(text):
    if not isinstance(text, str):
        raise TypeError("Ожидается строка")
    return len(text.strip()) > 0
