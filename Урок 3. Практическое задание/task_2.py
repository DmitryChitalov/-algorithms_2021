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


from sqlite3 import connect, OperationalError, IntegrityError
from hashlib import sha256
import os


class HashDB:
    def __init__(self):
        self.db_name = input("Введите название базы данных (на латинице!): ")
        self.db = os.path.join(os.path.dirname(__file__), f'{self.db_name}.sqlite')

    def create_hash_table(self):
        with connect(self.db) as conn:
            c = conn.cursor()
            c.execute(f"DROP TABLE IF EXISTS pass_hash;")
            c.execute(f'CREATE TABLE pass_hash (login varchar(255) unique, password_hash varchar(255));')
            conn.commit()
            print("Info: Таблица pass_hash успешко создана!")

    def get_hash(self):
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        password_hash = sha256(login.encode('utf-8')+password.encode('utf-8')).hexdigest()
        return login, password_hash

    def user_reg(self):
        print("Регистрация пользователя:")
        login, password_hash = self.get_hash()
        with connect(self.db) as conn:
            c = conn.cursor()
            try:
                c.execute(f"INSERT INTO pass_hash (login, password_hash) VALUES (?,?)", (login, password_hash))
            except IntegrityError as e:
                print(e, "Данный пользователь уже зарегистрирован!")
            else:
                conn.commit()
                print(f"Вы успешно зарегестрированы!")

    def login(self):
        print("Вход в систему:")
        login, password_hash = self.get_hash()
        with connect(self.db) as conn:
            c = conn.cursor()
            try:
                print("Проверка пароля")
                db_hash = c.execute(f"SELECT password_hash FROM pass_hash WHERE login = ?;",(login,)).fetchone()[0]
                print(db_hash)
                print(password_hash)
                if password_hash == db_hash:
                    print(f"Вы успешно авторизировались!")
                    return exit(0)
                print(f"Неверный логин или пароль, попробуйте заново!")
                return exit(0)
            except TypeError as e:
                print(e, "Неверный логин, попробуйте заново!")


Authorization = HashDB()
Authorization.create_hash_table()
Authorization.user_reg()
Authorization.login()
