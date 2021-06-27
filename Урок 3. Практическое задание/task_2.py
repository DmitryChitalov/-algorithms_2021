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

import hashlib


hash_password = hashlib.sha256(input('Введите пароль: ').encode('utf-8'))
hash_login = hashlib.sha256(input('Введите логин: ').encode('utf-8'))
list_hesh = []


def heshing_func(hash_password, hash_login):
    hex_dig_result = hash_password.hexdigest() + hash_login.hexdigest()
    print(hex_dig_result)
    list_hesh.append(hex_dig_result)
    print(list_hesh)


heshing_func(hash_password, hash_login)

hash_password2 = hashlib.sha256(input('Введите пароль: ').encode('utf-8'))
hash_login2 = hashlib.sha256(input('Введите логин: ').encode('utf-8'))

heshing_func(hash_password2, hash_login2)

if list_hesh[0] == list_hesh[1]:
    print('Пароли совпадают!')
else:
    print("Не верно")

print("_" * 100)


import uuid


def hash_password(password):
    # uuid используется для генерации случайного числа
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


new_pass = input('Введите пароль: ')
hashed_password = hash_password(new_pass)
print('Строка для хранения в базе данных: ' + hashed_password)
old_pass = input('Введите пароль еще раз для проверки: ')

if check_password(hashed_password, old_pass):
    print('Вы ввели правильный пароль')
else:
    print('Извините, но пароли не совпадают')