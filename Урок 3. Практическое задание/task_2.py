#!/usr/bin/env python3

import os
import sqlite3
from hashlib import sha256
from uuid import uuid4

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


class DB:

    def __init__(self, dbname: str) -> None:
        self.__connection = None
        try:
            if not os.path.exists(dbname):
                self.__connection = sqlite3.connect(dbname)
                c = self.__connection.cursor()
                c.execute('CREATE TABLE IF NOT EXISTS tbl(password TEXT, salt TEXT)')
                self.__connection.commit()
            else:
                self.__connection = sqlite3.connect(dbname)

        except sqlite3.Error as e:
            self.__connection = None
            print(e)

    def get(self) -> tuple:
        pwd, salt = None, None
        if self.__connection:
            try:
                c = self.__connection.cursor()
                c.execute('SELECT * FROM tbl')
                records = c.fetchall()
                if len(records):
                    pwd = records[0][0]
                    salt = records[0][1]
            except sqlite3.Error as e:
                print(e)

        return pwd, salt

    def add(self, pwd: str, salt: str) -> None:
        if self.__connection:
            try:
                c = self.__connection.cursor()
                c.execute(f"INSERT INTO tbl (password, salt) VALUES ('{pwd}', '{salt}')")
                self.__connection.commit()
            except sqlite3.Error as e:
                print(e)


def password_check(user_pwd: str, salt: str, user_hash: str) -> bool:
    return sha256(f'{user_pwd}{salt}'.encode('utf-8')).hexdigest() == user_hash


def main():
    db = DB('users.db')
    user_pwd = input('Введите пароль: ')

    pwd, salt = db.get()
    if not pwd is None:
        print(f'В базе данных хранится строка: {pwd}')
        print('Вы ввели правильный пароль') if password_check(user_pwd, salt, pwd) else print('Неверный пароль')
    else:
        salt = uuid4().hex
        user_hash = sha256(f'{user_pwd}{salt}'.encode('utf-8')).hexdigest()
        db.add(user_hash, salt)


if __name__ == '__main__':
    main()
