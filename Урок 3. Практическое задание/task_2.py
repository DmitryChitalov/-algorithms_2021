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

Д опускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
# sqlite, postgres, db_api, orm

import hashlib


def hash_password(input_str):
    return hashlib.sha256(input_str.encode() + salt.encode()).hexdigest()


salt = "salt"
user_input_str = input("Введите пароль:")
hash_psw = hash_password(user_input_str)
print(hash_psw)

with open("password.txt", "w") as password:
    password.write(hash_psw)

user_input_str = input("Введите пароль:")
hash_psw = hash_password(user_input_str)

with open("password.txt") as password:
    hash_password_from_file = password.read()
    print(hash_psw)
if hash_psw == hash_password_from_file:
    print("Введен верный пароль")
else:
    print("Введен неверный пароль!")
