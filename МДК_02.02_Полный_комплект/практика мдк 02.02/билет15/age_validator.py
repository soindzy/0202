"""Модуль проверки возраста."""

MIN_AGE = 0
MAX_AGE = 120

def validate_age(value):
    
    if isinstance(value, bool) or not isinstance(value, int):
        return False, f"Ошибка типа: возраст должен быть целым числом, получено {type(value).__name__}"

    if not (MIN_AGE <= value <= MAX_AGE):
        return False, f"Ошибка диапазона: возраст должен быть от {MIN_AGE} до {MAX_AGE}, получено {value}"

    return True, "OK"