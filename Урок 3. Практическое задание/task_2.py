"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""

from uuid import uuid4
from hashlib import sha256


def authorization():
    user_password = input('Введите пароль: ')
    hash_password = hash_salt(user_password, user_salt)
    print(f'В базе данных хранится строка: {hash_password}')
    save_password(hash_password)
    check_password = input('Повторите пароль: ')
    hash_password = hash_salt(check_password, user_salt)
    load_password(hash_password)


def hash_salt(password, salt):
    return sha256(salt.encode() + password.encode()).hexdigest()


def save_password(dct):
    with open('password.txt', 'w') as file:
        file.write(dct)


def load_password(dct):
    with open('password.txt', 'r') as file:
        if dct == file.readline():
            print('Вход в систему.')
        else:
            print('Неверный пароль!')


user_salt = uuid4().hex
authorization()
