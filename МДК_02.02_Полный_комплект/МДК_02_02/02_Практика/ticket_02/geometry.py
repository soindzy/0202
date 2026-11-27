def rectangle_area(width, height):
    if width < 0 or height < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return width * height
