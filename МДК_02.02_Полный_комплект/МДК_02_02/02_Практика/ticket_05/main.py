from maximum import find_maximum

if __name__ == "__main__":
    for values in [[3, 8, 2, 5], [-7, -2, -9], []]:
        try:
            print(f"{values} -> максимум {find_maximum(values)}")
        except ValueError as error:
            print(f"{values} -> Ошибка: {error}")
