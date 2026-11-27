from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def discounted_price(price):
    try:
        amount = Decimal(str(price))
    except (InvalidOperation, ValueError):
        raise ValueError("Цена должна быть числом") from None
    if not amount.is_finite() or amount < 0:
        raise ValueError("Цена должна быть конечной и неотрицательной")
    return (amount * Decimal("0.90")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
