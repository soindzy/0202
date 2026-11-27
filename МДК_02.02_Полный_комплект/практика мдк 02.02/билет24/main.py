from string_length import length, length_stripped

def main():
    tests = [
        ("пустая строка", ""),
        ("обычный текст", "Привет"),
        ("строка с пробелами", "   "),
        ("текст с пробелами по краям", "  abc  "),
        ("один пробел", " "),
    ]

    print(f"{'Случай':<30} {'Строка':<12} {'len':>4} {'strip':>6}")
    print("-" * 56)

    for name, s in tests:
        print(f"{name:<30} {repr(s):<12} {length(s):>4} {length_stripped(s):>6}")

if __name__ == "__main__":
    main()