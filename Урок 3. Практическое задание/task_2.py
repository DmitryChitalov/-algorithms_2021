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


import sqlite3
import hashlib


def hex_digit(salt, text):
    hash_obj = hashlib.sha256(salt.encode() + text.encode())
    hex_dig = hash_obj.hexdigest()
    return hex_dig


conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        name TEXT UNIQUE, 
        password TEXT)
""")
conn.commit()
login = input('Введите ваш логин: ')
cursor.execute('SELECT name, password FROM users WHERE name = ?', (login,))
user = cursor.fetchone()
if user is None:
    password = input('Такого пользователя не существует, введите пароль для добавления в базу: ')
    hex_dig = hex_digit(login, password)
    create_user = 'INSERT INTO users(name, password) VALUES (?, ?);'
    data_tuple = (login, hex_dig)
    cursor.execute(create_user, data_tuple)
    conn.commit()
    print('Пользователь успешно добавлен!!!')
else:
    password = input('Такой пользователь существует, введите пароль для проверки: ')
    hex_dig = hex_digit(login, password)
    if user[1] == hex_dig:
        print('Вы ввели правельный пароль!!!')
    else:
        print('Пароль не верный!!!')