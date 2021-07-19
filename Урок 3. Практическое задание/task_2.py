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

import sqlite3
from uuid import uuid4
import hashlib


class DbHash:
    def __init__(self):
        self.conn = sqlite3.connect("test_al.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS users;")
        self.cursor.execute("CREATE TABLE users(u_login varchar(255), password_hash varchar(255))")

    def create_hash(self):
        login = input('Введите логин: ')
        us_pass = input('Введите пароль: ')
        hash_passwd = hashlib.sha256(login.encode() + us_pass.encode()).hexdigest()
        return login, hash_passwd

    def sql_insert(self):

        login, hash_pass = self.create_hash()

        insert_log_hash = 'INSERT INTO users(u_login, password_hash) VALUES(?,?)'
        log_hash = (login, hash_pass)
        try:
            self.cursor.execute(insert_log_hash, log_hash)
        except sqlite3.IntegrityError:
            print('Такой login уже существует. Войдите в систему или введите другой login.')
        else:
            self.conn.commit()
            print('Вы зарегестрированы')

    def log_in(self):

        login, hash_pass = self.create_hash()

        select_log_hash = 'SELECT password_hash FROM users WHERE u_login = ?'

        self.cursor.execute(select_log_hash, (login,))

        db_hash = self.cursor.fetchone()
        db_hash = str(*db_hash)

        if hash_pass == db_hash:
            print('Вы ввели правильный пароль')
        else:
            print('Вы ввели неправильный пароль')

data_base_1 = DbHash()
data_base_1.create_table()
data_base_1.sql_insert()
data_base_1.log_in()

