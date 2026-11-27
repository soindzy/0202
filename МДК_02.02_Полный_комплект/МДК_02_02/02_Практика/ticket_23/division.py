def divide(a, b):
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("Делимое должно быть числом")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("Делитель должен быть числом")
    if b == 0:
        raise ZeroDivisionError("Деление на ноль запрещено")
    return a / b
