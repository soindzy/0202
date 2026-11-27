def format_money(amount, currency="₽"):

    text = f"{amount:,.2f}"        
    text = text.replace(",", " ").replace(".", ",")  
    return f"{text} {currency}"