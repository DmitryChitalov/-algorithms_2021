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

import random
import hashlib

salt = str(random.randint(100000, 10000000))


def gen_password(password):
    with open('password.txt', 'w') as file_object:
        file_object.write(hashlib.sha256(salt.encode() + password.encode()).hexdigest())

    return print(f'В базе данных хранится строка: {hashlib.sha256(salt.encode() + password.encode()).hexdigest()}')


def check_password(old_pass):
    with open('password.txt') as file_object:
        hashed_password = file_object.readline()
        if hashed_password == hashlib.sha256(salt.encode() + old_pass.encode()).hexdigest():
            return print(f'Вы ввели правильный пароль')
        else:
            return f'Вы ввели неправильный пароль'


gen_password(input('Введите пароль: '))
check_password(input('Введите пароль еще раз для проверки: '))
