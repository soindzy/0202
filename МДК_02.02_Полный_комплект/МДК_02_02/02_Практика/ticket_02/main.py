from geometry import rectangle_area

if __name__ == "__main__":
    for width, height in [(4, 6), (0, 5), (-1, 3)]:
        try:
            print(f"Стороны {width}, {height}: площадь {rectangle_area(width, height)}")
        except ValueError as error:
            print(f"Стороны {width}, {height}: ошибка: {error}")
