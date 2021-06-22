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

import sqlite3, hashlib


def create_hash(string):
    salt = 'any_salt'
    return hashlib.sha256(salt.encode() + string.encode()).hexdigest()


def read_pwd(string):
    pwd = create_hash(string)
    conn = sqlite3.connect('task_2.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT pwd FROM users WHERE pwd=?', (pwd,))
    result = cursor.fetchone()
    conn.close()
    return result


def save_pwd(string):
    pwd = create_hash(string)
    conn = sqlite3.connect('task_2.sqlite')
    cursor = conn.cursor()
    if read_pwd(string) is not None and read_pwd(string)[0] == pwd:
        print(f'Пароль {string} уже хранится в базе данных')
    else:
        cursor.execute('INSERT INTO users VALUES (NULL, ?);', (pwd,))
        conn.commit()
        print(f'В базу данных записана строка: {pwd}')
    conn.close()


def ask_pwd():
    user_pwd_1 = input('Введите пароль: ')
    save_pwd(user_pwd_1)
    user_pwd_2 = input('Введите пароль еще раз для проверки: ')
    if read_pwd(user_pwd_2) == read_pwd(user_pwd_1):
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели неверный пароль')


ask_pwd()
