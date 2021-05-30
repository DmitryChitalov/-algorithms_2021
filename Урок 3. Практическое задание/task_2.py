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
from __future__ import annotations
import sqlite3
import hashlib
from uuid import uuid4
import os


def create_connection(db_name: str) -> tuple:
    """
    Create connection with the database. If the db not exists -> create db.
    :param db_name: name of db
    :return: connection obj, cursor obj
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    return conn, cursor


def create_table(db_name: str, cursor: Cursor) -> None:
    """
    Create the main table with user_id, login and password_hash columns
    :param db_name: name of db
    :param cursor: cursor obj
    :return: None
    """
    cwd = os.getcwd()
    db_path = os.path.join(cwd, db_name)

    if not os.path.exists(db_path):
        try:
            cursor.executescript("""BEGIN TRANSACTION;
                                        CREATE TABLE IF NOT EXISTS login_info(
                                            `user_id` INTEGER PRIMARY KEY AUTOINCREMENT,
                                            `login` VARCHAR(100) UNIQUE,
                                            `password_hash` TEXT(300) UNIQUE);
                                    COMMIT;
            """)
        except sqlite3.Error as e:
            print('Ошибка БД: ' + str(e))
    return None


def create_login(cursor: Cursor, conn: Connection):
    """
    Insert user into database if the uniqueness condition is True
    :param cursor: cursor obj
    :param conn: connection obj
    :return: User obj
    """
    while True:
        try:
            login = input('Придумайте имя пользователя: ')
            password = input('Введите пароль: ')
            user = User(login, password)
            user.register_user_to_db(cursor, conn)
            print(f'В базе данных хранится строка: {user.password}')
        except sqlite3.Error as e:
            print(f'Ошибка БД: {e}. Выберете другое имя')
        else:
            return user


def check_user(user: User, cursor: Cursor, next_try=''):
    """
    Checking the second password against data
    :param user: User obj
    :param cursor: cursor obj
    :param next_try: empty string
    :return: positive test result
    """
    while user.hash_password(user.salt, next_try) != user.get_pw_hash_from_db(cursor):
        next_try = input('Введите пароль еще раз: ')
    else:
        return 'Вы ввели правильный пароль'


class User:
    def __init__(self, login: str, password: str) -> None:
        self._login = login
        self.salt = uuid4().hex
        self._password_hash = self.hash_password(self.salt, password)

    @property
    def password(self) -> str:
        return self._password_hash

    @staticmethod
    def hash_password(salt, pw: str) -> str:
        """
        Hash two strings with sha256
        :param salt: additional string
        :param pw: user password
        :return: hash string
        """
        return hashlib.sha256(salt.encode('utf-8') + pw.encode('utf-8')).hexdigest()

    def register_user_to_db(self, cursor: Cursor, conn: Connection) -> None:
        """
        Insert new user to db
        :param cursor: Cursor obj
        :param conn: Connection obj
        :return: None
        """
        cursor.execute("""INSERT INTO login_info(`login`, `password_hash`)
                                VALUES (:login, :password_hash);       
        """, {'login': self._login, 'password_hash': self._password_hash})
        conn.commit()

    def get_pw_hash_from_db(self, cursor: Cursor) -> str:
        """
        Receive password_hash from db
        :param cursor: Cursor obj
        :return: password_hash string
        """
        return cursor.execute("""SELECT `password_hash` FROM login_info
                                    WHERE `login`= :login;       
        """, {'login': self._login}).fetchone()[0]


def main():
    conn, cursor = create_connection('users.sqlite')
    create_table('users.sqlite', cursor)
    user = create_login(cursor, conn)
    print(check_user(user, cursor))
    conn.close()


if __name__ == '__main__':
    main()
