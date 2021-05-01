"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

Избегайте дублирования выражений при выислении хешей! Это можно вынести в отдельную ф-цию.

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
user_salt = uuid4().hex
user_password = input('Введите пароль: ')


def get_hash(salt, value: str):
    return sha256(salt.encode() + value.encode()).hexdigest()


password_hash = get_hash(user_salt, user_password)

with open('password.txt', 'w') as file:
    file.write(password_hash)

password_again = input('Введите пароль ещё раз для проверки: ')
password_hash = get_hash(user_salt, password_again)

with open('password.txt', 'r') as file:
    if password_hash == file.readline():
        print('OK')
    else:
        print('Пароль неверный')
