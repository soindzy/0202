from discount import apply_discount, discount_amount
from formatter import format_money

def process(price):
   
    final = apply_discount(price)
    saved = discount_amount(price)
    print(f"Цена:            {format_money(price)}")
    print(f"Скидка 10%:      {format_money(saved)}")
    print(f"Итого со скидкой:{format_money(final)}")
    print()

def main():
    print("=== Пример 1: цена 1000 ===")
    process(1000)

    print("=== Пример 2: цена 2499.99 ===")
    process(2499.99)

if __name__ == "__main__":
    main()