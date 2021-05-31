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


class DbSession:
    def __init__(self, db_name):
        self._db_name = db_name
        self.conn, self.cursor = self.create_connection()

    def create_connection(self) -> tuple:
        """
        Create connection with the database. If the db not exists -> create db.
        :return: connection obj, cursor obj
        """
        conn = sqlite3.connect(self._db_name)
        cursor = conn.cursor()
        return conn, cursor

    def close_connection(self) -> None:
        self.conn.close()

    def create_table(self) -> None:
        """
        Create the main table with user_id, login and password_hash columns
        :return: None
        """
        try:
            self.cursor.executescript("""BEGIN TRANSACTION;
                                            CREATE TABLE IF NOT EXISTS login_info(
                                                `user_id` INTEGER PRIMARY KEY AUTOINCREMENT,
                                                `login` VARCHAR(100) UNIQUE,
                                                `password_hash` TEXT(300) UNIQUE);
                                        COMMIT;
            """)
        except sqlite3.Error as e:
            print('Ошибка БД: ' + str(e))
        return None

    def create_login(self) -> User:
        """
        Insert user into database if the uniqueness condition is True
        :return: User obj
        """
        while True:
            try:
                login = input('Придумайте имя пользователя: ')
                password = input('Введите пароль: ')
                user = User(login, password)
                self.register_user_to_db(user)
                print(f'В базе данных хранится строка: {user.password}')
            except sqlite3.Error as e:
                print(f'Ошибка БД: {e}. Выберете другое имя')
            else:
                return user

    def check_user(self, user: User, next_try='') -> str:
        """
        Checking the second password against data
        :param user: User obj
        :param next_try: empty string
        :return: positive test result
        """
        while user.hash_password(user.salt, next_try) != self.get_pw_hash_from_db(user):
            next_try = input('Введите пароль еще раз: ')
        else:
            return 'Вы ввели правильный пароль'

    def register_user_to_db(self, user: User) -> None:
        """
        Insert new user to db
        :return: None
        """
        self.cursor.execute("""INSERT INTO login_info(`login`, `password_hash`)
                                VALUES (:login, :password_hash);       
        """, {'login': user.login, 'password_hash': user.password})
        self.conn.commit()

    def get_pw_hash_from_db(self, user: User) -> str:
        """
        Receive password_hash from db
        :param user: User ibj
        :return: password_hash string
        """
        return self.cursor.execute("""SELECT `password_hash` FROM login_info
                                    WHERE `login`= :login;       
        """, {'login': user.login}).fetchone()[0]


class User:
    def __init__(self, login: str, password: str) -> None:
        self._login = login
        self.salt = uuid4().hex
        self._password_hash = self.hash_password(self.salt, password)

    @property
    def login(self) -> str:
        return self._login

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


def main():
    db_session = DbSession('users.sqlite')
    db_session.create_table()
    user = db_session.create_login()
    print(db_session.check_user(user))
    db_session.close_connection()


if __name__ == '__main__':
    main()
