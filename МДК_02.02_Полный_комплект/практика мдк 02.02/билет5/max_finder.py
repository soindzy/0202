def find_max(sequence):
    if not sequence:
        raise ValueError("Последовательность пуста")
    maximum = sequence[0]
    for x in sequence[1:]:
        if x > maximum:
            maximum = x
    return maximum