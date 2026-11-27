def parse_request(text):
    """Формат: число операция число, например 10 / 2."""
    parts = text.split()
    if len(parts) != 3:
        raise ValueError("Ожидается: число операция число")
    left, operation, right = parts
    return float(left), operation, float(right)
