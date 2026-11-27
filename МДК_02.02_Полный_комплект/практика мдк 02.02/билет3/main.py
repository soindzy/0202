from temperature import celsius_to_fahrenheit

def main():
    try:
        celsius = float(input("Введите температуру в °C: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} °C = {fahrenheit} °F")
    except ValueError:
        print("Ошибка: введите число")

if __name__ == "__main__":
    main()