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
from uuid import uuid4


""" Класс для работы с базой данных """


class MyBase:

    def __init__(self):
        self.conn = sqlite3.connect("myusers.db")
        self.cursor = self.conn.cursor()
        # self.cursor.execute('''DROP TABLE IF EXISTS users;''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                        id INTEGER PRIMARY KEY,
                        login TEXT,
                        salt_login TEXT,
                        pwd_hex TEXT,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP);''')
        self.conn.commit()

    def close_conn(self):
        self.conn.close()

    def info_db(self):
        self.cursor.execute('SELECT max(id), count(id) FROM users;')
        max_id = self.cursor.fetchone()
        return max_id

    def select_one(self, login):
        self.cursor.execute(f'SELECT * FROM users WHERE login="{login}"')
        search_user = self.cursor.fetchone()
        return search_user

    def select_all(self):
        self.cursor.execute('SELECT * FROM users ORDER BY login')
        all_user = self.cursor.fetchall()
        return all_user

    def new_user(self, login, pwd):
        salt = uuid4().hex  # создадим соль для нового пользователя
        res_hex = hashlib.sha256(salt.encode() + pwd.encode()).hexdigest()
        user_data = [login, salt, res_hex]
        self.cursor.execute("INSERT INTO users(login, salt_login, pwd_hex) VALUES(?, ?, ?)", user_data)
        self.conn.commit()
        return salt, res_hex


# Функция авторизации
def author():
    users_db = MyBase()
    login = input('Введите ваш логин (если новый, то пользователь будет создан в БД):')
    info_login = users_db.select_one(login)
    users_db.close_conn()  # закрываем соединение на время ожидания ввода
    if info_login is None:
        print('Пользователя не существует! Будет добавлен новый!')
        pwd = input('Введите пароль нового пользователя: ')
        users_db.__init__()
        salt, pwd_hex_db = users_db.new_user(login, pwd)
        users_db.close_conn()
    else:
        salt = info_login[2]
        pwd_hex_db = info_login[3]
    while True:
        pwd = input('Введите ранее созданный пароль: ')
        res_hex = hashlib.sha256(salt.encode() + pwd.encode()).hexdigest()
        if pwd_hex_db == res_hex:   # сравниваем хеши паролей
            break
        else:
            print("Вы ввели неверный пароль! Попробуйте еще раз!")

    print('\nДоступ в личный кабинет разрешен!\n В базе есть следующие пользователи:')
    users_db.__init__()
    print(*users_db.select_all(), sep='\n')
    del users_db


# Логинимся с разными пользователями в цикле до выхода по команде '0'
while True:
    user_resp = input('Для входа в личный кабинет нажмите Enter / Для выхода 0:')
    if user_resp == '0':
        print('Удачи!')
        break
    author()
