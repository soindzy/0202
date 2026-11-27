from user_data import make_user
from message_builder import build_message

def main():

    users = [
        make_user("Иван", 25),
        make_user("Мария", 31),
        make_user("Олег", 1),
        make_user("Анна", 12),
        make_user("Пётр", 120),
    ]
ем
    for user in users:
   
        message = build_message(user)
        print(message)

if __name__ == "__main__":
    main()