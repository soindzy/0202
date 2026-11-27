def is_non_empty(value, strip=True):
  
    if not isinstance(value, str):
        return False, f"Ошибка типа: ожидалась строка, получено {type(value).__name__}"

    s = value.strip() if strip else value
    if len(s) == 0:
        return False, "Ошибка: строка пустая"

    return True, "OK"