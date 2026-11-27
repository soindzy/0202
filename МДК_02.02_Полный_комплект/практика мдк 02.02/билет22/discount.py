DISCOUNT_RATE = 0.10   

def apply_discount(price):
  
    if price < 0:
        raise ValueError(f"Цена не может быть отрицательной: {price}")
    return price * (1 - DISCOUNT_RATE)

def discount_amount(price):
  
    if price < 0:
        raise ValueError(f"Цена не может быть отрицательной: {price}")
    return price * DISCOUNT_RATE