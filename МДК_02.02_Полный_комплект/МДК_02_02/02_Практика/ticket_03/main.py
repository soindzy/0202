from temperature import celsius_to_fahrenheit

if __name__ == "__main__":
    for celsius in [0, 100, -40]:
        print(f"{celsius} °C = {celsius_to_fahrenheit(celsius):g} °F")
