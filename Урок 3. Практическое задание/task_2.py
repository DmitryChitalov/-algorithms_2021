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
from os.path import join, dirname
from sqlite3 import OperationalError, connect, IntegrityError


# login = "Testuser"
# print(login)
# password_input = input("Введите пароль ")
#
# hashed_password = hashlib.sha256((login+password_input).encode('utf-8')).hexdigest()
# print(hashed_password)
# password_check = input("Введите пароль ")
# hashed_password_check = hashlib.sha256((login+password_check).encode('utf-8')).hexdigest()
#
# if hashed_password == hashed_password_check:
#     print(f"Пароль верный")

class HashClass:
    def __init__(self):
        self.db_obj = join(dirname(__file__), "demo.sqlite")
        self.conn = connect(HashClass.db_obj)
        self.crs = self.conn.cursor()

    def create_table(self):

        create_statement = "CREATE TABLE user_info ((user_login varchar(255) " \
                           "unique, user_password varchar(255));"
        try:
            self.crs.exectue(create_statement)
        except OperationalError:
            print("Таблица уже есть")
        else:
            self.conn.commit()
            print("Таблица добавлена в БД")

    @staticmethod
    def get_hash():
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        hash_obj = hashlib.sha256(login.encode() + password.encode()).hexdigest()
        return login, hash_obj

    def register(self):
        login, reg_hash = self.get_hash()

        insert_statement = "INSERT INTO user_info (user_login, user_password)" \
                           " VALUES (?, ?)"
        user_info = (login, reg_hash)
        try:

            self.crs.execute(insert_statement, user_info)
        except IntegrityError:
            print("Вы уже в базе, выполните вход.")
        else:
            self.conn.commit()
            print("Операция прошла успешно, вы зарегистрировались")

    def log_in(self):

        login, check_hash = self.get_hash()

        select_statement = "SELECT user_password FROM user_info WHERE user_login = ?"

        self.crs.execute(select_statement, (login,))

        out_hash = self.crs.fetchone()

        if check_hash == out_hash[0]:
            print('Аутентификация успешна')
        else:
            print('Неверные данные для входа, или не выполнена регистрация')


network = HashClass()
# network.create_table()
# network.register()
network.log_in()
# ORM

