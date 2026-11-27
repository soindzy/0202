from age_validator import validate_age

def main():
    tests = [25, 0, 120, -1, 121, 3.5, "25", None, True, 200]

    for value in tests:
        ok, msg = validate_age(value)
        status = "ок" if ok else "неудачно"
        print(f"{status} {value!r:>8} → {msg}")

if __name__ == "__main__":
    main()