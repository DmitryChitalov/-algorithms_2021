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

conn = sqlite3.connect('users.sqlite')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS user_info(
    login INT PRIMARY KEY,
    password VARCHAR(255));
    """)
conn.commit()


def set_password(login):
    passwd = input('Введите пароль: ')
    res = hashlib.sha256(login.encode() + passwd.encode()).hexdigest()
    cur.execute("INSERT INTO user_info (login, password) VALUES (?, ?)", (login, res))
    conn.commit()
    cur.execute("SELECT password FROM user_info WHERE login = ?", (login,))
    result = cur.fetchone()
    print(f'В базе данных хранится строка: {result[0]}')


def auth(login):
    password = input('Введите пароль еще раз для проверки: ')
    check = hashlib.sha256(login.encode() + password.encode()).hexdigest()
    cur.execute("SELECT password FROM user_info WHERE login = ?", (login,))
    result = cur.fetchone()
    if result[0] == check:
        print('Вы ввели правильный пароль')
    else:
        print('Пароль неверен')


set_password('user1')
auth('user1')
set_password('user2')
auth('user2')
conn.close()
