from positive import count_positive

if __name__ == "__main__":
    for values in [[-2, 0, 3, 5, -1], [], [0, -3]]:
        print(f"{values} -> положительных: {count_positive(values)}")
