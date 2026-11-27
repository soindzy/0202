def is_even(number):
    if type(number) is not int:
        raise TypeError("Ожидается целое число")
    return number % 2 == 0
