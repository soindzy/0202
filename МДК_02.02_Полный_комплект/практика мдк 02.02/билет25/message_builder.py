def build_message(user):
    name = user["name"]
    age = user["age"]

    if age % 10 == 1 and age % 100 != 11:
        word = "год"
    elif age % 10 in (2, 3, 4) and age % 100 not in (12, 13, 14):
        word = "года"
    else:
        word = "лет"

    return f"Пользователь: {name}, возраст: {age} {word}."