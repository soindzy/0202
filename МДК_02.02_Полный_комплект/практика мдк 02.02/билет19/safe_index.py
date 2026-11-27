def safe_get(sequence, index):
    
    if isinstance(index, bool) or not isinstance(index, int):
        return False, f"Ошибка типа: индекс должен быть целым числом, получено {type(index).__name__}"

    if index < 0 or index >= len(sequence):
        return False, f"Выход за границы: индекс {index}, длина {len(sequence)}"

    return True, sequence[index]