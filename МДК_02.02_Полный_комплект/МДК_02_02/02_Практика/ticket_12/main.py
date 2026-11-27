from division import divide

if __name__ == "__main__":
    for a, b in [(10, 2), (0, 5), (5, 0), ("abc", 2)]:
        try:
            print(f"{a!r} / {b!r} = {divide(a, b)}")
        except (ZeroDivisionError, TypeError) as error:
            print(f"{a!r} / {b!r} -> Ошибка: {error}")
