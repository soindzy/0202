import sys
from age_validation import validate_age

if __name__ == "__main__":
    if "--interactive" in sys.argv:
        text = input("Возраст (целое число 0–120): ")
        try:
            print(f"Возраст принят: {validate_age(int(text))}")
        except (TypeError, ValueError) as error:
            print(f"Ошибка: {error}")
    else:
        for value in [0, 120, 35, -1, 121, "20", 20.5, True]:
            try:
                print(f"{value!r} -> допустимый возраст: {validate_age(value)}")
            except (TypeError, ValueError) as error:
                print(f"{value!r} -> Ошибка: {error}")
