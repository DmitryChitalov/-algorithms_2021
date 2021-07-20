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
import sqlite3


def create_base():
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        password TEXT);""")
    conn.commit()


def login_in():
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    name_input = input('Введите логин: ')
    pass_input = input('Введите пароль: ')
    password_to_hash = hashlib.sha256(pass_input.encode('utf-8') + name_input.encode('utf-8')).hexdigest()
    print(f'Хеш пароля: {password_to_hash}')
    sql_insert = 'INSERT INTO users (name, password) VALUES (?, ?)'
    cursor.execute(sql_insert, ([name_input, password_to_hash]))
    conn.commit()


def login():
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    name_input = input('Введите логин: ')
    pass_input = input('Введите пароль: ')
    password_to_hash = hashlib.sha256(pass_input.encode('utf-8') + name_input.encode('utf-8')).hexdigest()
    cursor.execute('SELECT password FROM users WHERE name=?', (name_input,))
    result = cursor.fetchone()
    if result is None:
        return f'Такой пользователь уже существует'
    if password_to_hash == result[0]:
        return f'Вы ввели правильный пароль'
    else:
        return f'Неверный пароль'

# create_base()
# login_in()
print(login())