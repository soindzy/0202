from summation import sum_numbers

if __name__ == "__main__":
    for values in [[1, 2, 3], [], [-2, 5, -3]]:
        print(f"{values} -> сумма {sum_numbers(values)}")
