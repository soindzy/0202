from square import square

CASES = [(2, 4), (0, 0), (-3, 9), (1.5, 2.25)]

if __name__ == "__main__":
    for value, expected in CASES:
        actual = square(value)
        print(f"Вход: {value}; ожидается: {expected}; получено: {actual}; {'PASS' if actual == expected else 'FAIL'}")
