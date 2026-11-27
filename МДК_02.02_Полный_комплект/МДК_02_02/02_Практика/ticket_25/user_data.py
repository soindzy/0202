from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    name: str
    age: int


def create_user(name, age):
    if not isinstance(name, str):
        raise TypeError("Имя должно быть строкой")
    name = name.strip()
    if not name:
        raise ValueError("Имя не должно быть пустым")
    if type(age) is not int:
        raise TypeError("Возраст должен быть целым числом")
    if not 0 <= age <= 120:
        raise ValueError("Возраст должен быть от 0 до 120")
    return User(name, age)
