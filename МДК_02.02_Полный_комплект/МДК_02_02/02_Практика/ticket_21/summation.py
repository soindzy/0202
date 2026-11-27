def sum_numbers(values):
    total = 0
    for value in values:
        # Было: total = value. Исправление: накапливать, а не заменять.
        total += value
    return total
