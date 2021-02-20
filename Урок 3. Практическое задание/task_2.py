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

import hashlib
from uuid import uuid4

pass_hash_list = []
salt = uuid4().hex

def sign_up():
    password = input("Введите пароль для добавления в ДБ ")
    return password

def pass_hash():
    password = sign_up()
    pass_hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    print(pass_hash)
    pass_hash_list.append(pass_hash)

def login():
    password = input("Введите пароль ")
    return password

def pass_hash_check():
    password = login()
    pass_hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    print(pass_hash)
    if pass_hash in pass_hash_list:
        print("Вы авторизовались")
    else:
        print("Неверный пароль")

pass_hash()
pass_hash_check()
