import sys
from input_data import parse_request
from calculator import calculate
from output_data import format_result


def evaluate(text):
    return format_result(calculate(*parse_request(text)))


if __name__ == "__main__":
    requests = [input("Пример (10 + 2): ")] if "--interactive" in sys.argv else ["10 + 2", "9 / 3", "1 / 0", "abc"]
    for text in requests:
        try:
            print(f"{text} -> {evaluate(text)}")
        except (ValueError, ZeroDivisionError) as error:
            print(f"{text} -> Ошибка: {error}")
