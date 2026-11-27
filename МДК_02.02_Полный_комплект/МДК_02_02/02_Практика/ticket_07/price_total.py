from decimal import Decimal


def total_prices(prices):
    return sum(prices, Decimal("0.00"))
