def get_element(sequence, index):
    if type(index) is not int:
        raise TypeError("Индекс должен быть целым числом")
    # Учебный контракт: индексы только от 0 до len(sequence) - 1.
    if not 0 <= index < len(sequence):
        raise IndexError("Индекс выходит за границы последовательности")
    return sequence[index]
