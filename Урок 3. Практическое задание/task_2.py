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
import sqlite3 as sl
import hashlib
from uuid import uuid4


def encode(salt, password):
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest()


class User:
    def __init__(self, login='', password=''):
        self.salt = uuid4().hex
        self.login = login
        self.encoded_pass = encode(self.salt, password)

    @staticmethod
    def new():
        return User(
            input('Enter desired login...: '),
            input('Enter desired password...: '))

    def db_fill(self):
        try:
            with sl.connect("L3_hash.db") as conn:
                curr = conn.cursor()
                curr.execute("""CREATE TABLE IF NOT EXISTS users(
                            `id` INTEGER PRIMARY KEY AUTOINCREMENT,
                            `username` TEXT,
                            `hash_password` TEXT UNIQUE);
                """)
                print('Database connected! Table successfully created!\n')
                curr.execute("""SELECT username FROM users WHERE username=(?)""", (self.login,))
                exists = curr.fetchall()
                if not exists:
                    curr.execute("""INSERT INTO users(`username`, `hash_password`)
                                    VALUES(?, ?);""", (self.login, self.encoded_pass,))
                    conn.commit()
                    print('User created successfully...')
                    curr.execute("""SELECT `hash_password` FROM users WHERE username=?""", (self.login,))
                    result = curr.fetchone()[0]
                    print(f'Stored password hash is: {result}')
                else:
                    print("Error: Username already in use.")
        except sl.Error as err:
            print(f'Processing error: {err}')
        conn.close()
        print('Connection closed...')

    def check_hash(self, repeat_pass=''):
        repeat_pass = input('Repeat you password please...: ')
        with sl.connect("L3_hash.db") as conn:
            curr = conn.cursor()
            curr.execute("""SELECT `hash_password` FROM users WHERE username=?""", (self.login,))
            stored_hash = curr.fetchone()[0]
        if encode(self.salt, repeat_pass) == stored_hash:
            print('Passwords match!')
        else:
            print('Passwords do not match!')


user = User.new()
user.db_fill()
user.check_hash()
