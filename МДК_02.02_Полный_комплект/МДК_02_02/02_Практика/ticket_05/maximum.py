def find_maximum(values):
    iterator = iter(values)
    try:
        result = next(iterator)
    except StopIteration:
        raise ValueError("Пустая последовательность не имеет максимума") from None
    for value in iterator:
        if value > result:
            result = value
    return result
