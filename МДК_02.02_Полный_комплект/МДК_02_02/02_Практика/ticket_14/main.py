from average import average

if __name__ == "__main__":
    for a, b, expected in [(2, 4, 3), (-4, 4, 0), (0, 0, 0)]:
        print(f"({a} + {b}) / 2 = {average(a, b)}; ожидается {expected}")
