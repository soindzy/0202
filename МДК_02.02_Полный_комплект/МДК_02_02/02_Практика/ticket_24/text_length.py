def string_length(text):
    if not isinstance(text, str):
        raise TypeError("Ожидается строка")
    return len(text)
