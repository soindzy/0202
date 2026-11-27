from sorting import sort_numbers

CASES = [([], []), ([3, 1, 2], [1, 2, 3]), ([2, 1, 2, 1], [1, 1, 2, 2]),
         ([-1, -5, 0], [-5, -1, 0]), ([1, 2, 3], [1, 2, 3])]

if __name__ == "__main__":
    for values, expected in CASES:
        print(f"Вход {values}; ожидается {expected}; получено {sort_numbers(values)}")
