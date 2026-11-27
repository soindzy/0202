from text_length import string_length

if __name__ == "__main__":
    for text in ["", "Привет", "два слова", "   "]:
        print(f"{text!r} -> длина {string_length(text)}")
