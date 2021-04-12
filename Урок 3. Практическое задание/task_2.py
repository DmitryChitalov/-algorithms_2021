"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
# sqlite, postgres, db_api, orm

from uuid import uuid4
import hashlib


def hash_pass(password, salt):
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest()


def create_password():
    salt = uuid4().hex
    password = hash_pass(input('Введите пароль: '), salt)
    print(password)
    with open("user_password.txt", "w") as f:
        f.write(salt + '\n' + password)


def check_password():
    with open("user_password.txt", "r") as f:
        from_file = f.read().splitlines()
    salt = from_file[0]
    password_from_file = from_file[1]
    if password_from_file == hash_pass(input('Введите пароль еще раз: '), salt):
        print('Пароли совпадают')
    else:
        print('Пароли не совпадают')


create_password()
check_password()
