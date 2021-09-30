from uuid import uuid4
from hashlib import sha256


def hash_password(salt):
    user_input = input("Введите пароль: ")
    return sha256(salt.encode() + user_input.encode('utf-8')).hexdigest()


def write_password(password):
    with open("db.txt", "w") as file:
        file.write(password)
        print(f"В базе данных хранится строка: {password}")


def get_password():
    with open("db.txt") as file:
        return file.readline()


if __name__ == '__main__':
    secret = uuid4().hex
    write_password(hash_password(secret))
    second_input = hash_password(secret)

    if get_password() == second_input:
        print("Вы ввели правильный пароль!")
    else:
        print("Пароли не совпадают!")
