from user_data import create_user
from user_message import format_user

if __name__ == "__main__":
    for name, age in [("Анна", 20), ("Иван", 35)]:
        user = create_user(name, age)
        print(format_user(user))
