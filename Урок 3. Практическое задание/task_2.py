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
import random
import string
from hashlib import sha256

bd = {}
ls = []


def create_random_password(length=12):
    from os import urandom
    salt = urandom(length)
    symbols = string.ascii_letters + string.digits + '!#$!&_+-?@^_^'
    password = ''.join(random.choice(symbols) for _ in range(length))
    password_hash = sha256(password.encode('UTF-8') + salt).hexdigest()
    return password, password_hash, salt


def generate_hash(pwd):
    from os import urandom
    salt = urandom(12)
    hash_password = sha256(pwd.encode('utf-8') + salt).hexdigest()
    print(hash_password)
    return hash_password, salt


def check_hash(password, user_data):
    import hashlib

    if hashlib.sha256(
            password.encode('utf-8') + user_data['salt']).hexdigest() == user_data['password']:
        return True
    else:
        return False


def generate_password():
    for i in range(10):
        pwd, hash_pwd, salt = create_random_password()
        print(f'user{i}: {pwd}')
        bd[f'user{i}'] = {'password': hash_pwd, 'salt': salt}


def main():
    pwd = input('Введите пароль: ').lower()
    ls.append(generate_hash(pwd))
    pwd = input('Введите пароль еще раз для проверки: ')
    if sha256(
            pwd.encode('utf-8') + ls[0][1]).hexdigest() == ls[0][0]:
        print(True)
    else:
        return False


main()

# def main():
#     #   generate_password()
#     print(bd)
#     user_name, pwd = input('Введите логин: ').lower(), input('Введите пароль: ')
#     if bd.get(user_name):
#         if check_hash(pwd, bd[user_name]):
#             print('Доступ разрешен.')
#         else:
#             print('Доступ запрещен.')

#   main()
