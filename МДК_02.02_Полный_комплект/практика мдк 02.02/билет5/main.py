from max_finder import find_max

def main():
    data = [3, 7, 2, 9, 5, 9, 1]
    print("Последовательность:", data)
    result = find_max(data)
    print("Максимум:", result)
    data2 = [-5, -12, -3, -8]
    print("Последовательность:", data2)
    print("Максимум:", find_max(data2))

if __name__ == "__main__":
    main()