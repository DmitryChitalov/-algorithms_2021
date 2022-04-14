"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей.

Самый просто вариант хранения хешей - просто в оперативной памяти (в переменных).

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""

import hashlib
from uuid import uuid4


with open('DB.txt', 'a', encoding='utf-8') as f:
    password = input('Please enter your password: ')
    salt = uuid4().hex
    f.write(hashlib.sha256(salt.encode() + password.encode()).hexdigest())

with open('DB.txt', 'r') as f:
    datebase = f.read()
    print(f'Datebase has this hash: {datebase}')
    password_2 = input('Please enter your password again: ')
    hash_psswd_2 = hashlib.sha256(salt.encode() + password_2.encode()).hexdigest()
    if datebase == hash_psswd_2:
        print('Password is correct')
    else:
        print('Password is incorrect')

