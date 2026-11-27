import sys
from conversion import parse_integer

if __name__ == "__main__":
    values = [input("Введите целое число: ")] if "--interactive" in sys.argv else ["15", "abc"]
    for text in values:
        try:
            print(f"{text!r} -> {parse_integer(text)}")
        except (TypeError, ValueError) as error:
            print(f"{text!r} -> Ошибка: {error}")
