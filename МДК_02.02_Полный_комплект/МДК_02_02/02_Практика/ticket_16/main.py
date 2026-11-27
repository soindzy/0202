import sys
from text_validation import is_nonempty


def process(text):
    if not is_nonempty(text):
        return "Ошибка: ввод не должен быть пустым"
    return f"Принято: {text.strip()}"


if __name__ == "__main__":
    values = [input("Введите текст: ")] if "--interactive" in sys.argv else ["Привет", "", "   "]
    for text in values:
        print(f"{text!r} -> {process(text)}")
