def rectangle_area(length, width):
    
    if length <= 0 or width <= 0:
        raise ValueError("Стороны должны быть положительными")
    return length * width