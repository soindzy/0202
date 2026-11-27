from area import rectangle_area

def main():
    try:
        length = float(input("Введите длину: "))
        width  = float(input("Введите ширину: "))

        result = rectangle_area(length, width)

        print(f"Площадь прямоугольника: {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()