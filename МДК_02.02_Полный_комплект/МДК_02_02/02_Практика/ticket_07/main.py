from price_source import get_prices
from price_total import total_prices
from price_output import format_total

if __name__ == "__main__":
    prices = get_prices()
    total = total_prices(prices)
    print(f"Цены: {', '.join(map(str, prices))}")
    print(format_total(total))
