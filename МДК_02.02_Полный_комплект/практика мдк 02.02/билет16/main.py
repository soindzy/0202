from string_validator import is_non_empty

def main():
    tests = ["Привет", "", "   ", "\t\n", "  текст  ", 123, None, "0"]

    for value in tests:
        ok, msg = is_non_empty(value)
        status = "ok" if ok else "no"
        print(f"{status} {value!r:>12} → {msg}")

    print("\n--- Использование результата ---")
    user_input = input("Введите имя: ")

    ok, msg = is_non_empty(user_input)
    if ok:
        print(f"Привет, {user_input.strip()}!")
    else:
        print(f"Ошибка ввода: {msg}")

if __name__ == "__main__":
    main()