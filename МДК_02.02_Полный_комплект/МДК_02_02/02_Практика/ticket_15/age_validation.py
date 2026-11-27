def validate_age(value):
    # bool является подклассом int, поэтому проверяем точный тип.
    if type(value) is not int:
        raise TypeError("Возраст должен быть целым числом")
    if not 0 <= value <= 120:
        raise ValueError("Возраст должен быть от 0 до 120 включительно")
    return value
