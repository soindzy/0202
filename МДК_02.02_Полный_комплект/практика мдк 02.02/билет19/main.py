from safe_index import safe_get

def main():
    data = [10, 20, 30, 40, 50]

    print("Последовательность:", data)
    print("Длина:", len(data))
    print()

    print("--- Корректные случаи ---")
    for i in [0, 2, 4]:
        ok, val = safe_get(data, i)
        print(f"safe_get(data, {i}) = {val}   ok")

    print()

    print("--- Ошибочные случаи ---")
    bad = [5, -1, 100, 2.5, "2", True]
    for i in bad:
        ok, msg = safe_get(data, i)
        print(f"safe_get(data, {i!r:>6}) → {msg}   no")

if __name__ == "__main__":
    main()