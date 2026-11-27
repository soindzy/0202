def calculate(a, operation, b):
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b
    if operation == "/":
        if b == 0:
            raise ZeroDivisionError("Деление на ноль запрещено")
        return a / b
    raise ValueError("Неизвестная операция")
