from discount import discounted_price
from formatting import format_price

if __name__ == "__main__":
    for price in ["1000.00", "250.50"]:
        result = discounted_price(price)
        print(f"Цена {price}, скидка 10% -> {format_price(result)}")
