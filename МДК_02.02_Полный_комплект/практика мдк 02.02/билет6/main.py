from positive_counter import c

def main():
    data = [3, -7, 0, 9, 5, -1, 2]
    print("Последовательность:", data)

    result = c(data)
    print("Положительных чисел:", result)

if __name__ == "__main__":
    main()