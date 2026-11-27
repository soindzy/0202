from parity import is_even

if __name__ == "__main__":
    for number in [8, 7, 0, -4]:
        print(f"{number}: {'чётное' if is_even(number) else 'нечётное'}")
