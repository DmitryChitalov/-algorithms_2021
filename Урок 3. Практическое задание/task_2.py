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
import os.path


class MyDatabaseConnector:
    """
    Класс для работы с БД sqlLite3.
    """
    __path_to_db = os.path.join(os.path.dirname(__file__), "test.db")

    def __init__(self):
        """
        Инициализация.
        """
        self.__connect = None
        try:
            self.__connect = sqlite3.connect(self.__path_to_db)
            self.cursor = self.__connect.cursor()
        except sqlite3.Error as e:
            print(e)

    def create_table(self):
        """
        Создание/Пересоздание таблицы.
        """
        sql = """drop TABLE IF EXISTS credentials;
                 CREATE TABLE credentials(
                        id INTEGER NOT NULL UNIQUE,
                        user_name	TEXT,
                        password_hash	TEXT,
                        PRIMARY KEY(id)
                 );
                 drop INDEX IF EXISTS index_of_user_name;
                 CREATE UNIQUE INDEX index_of_user_name ON credentials(user_name);"""
        try:
            self.cursor.executescript(sql).fetchall()
        except sqlite3.Error as e:
            print(e)

    def save_password_hash(self, user_name, password_hash):
        """
        Сохранение хеша введенного пароля.
        :param user_name:
        :param password_hash:
        :return:
        """
        if user_name and password_hash:
            sql = """insert into credentials(user_name, password_hash) values(?, ?);"""
            try:
                self.cursor.execute(sql, (user_name, password_hash))
                self.__connect.commit()
            except sqlite3.Error as e:
                print(e)

    def get_password_hash(self, user_name):
        """
        Получения хеша пароля по имени пользователя.
        :param user_name:
        :return:
        """
        sql = """select c.password_hash
                 from credentials c
                 where c.user_name = :user_name;"""

        try:
            password_hash_list = self.cursor.execute(sql, {"user_name": user_name}).fetchall()
        except sqlite3.Error as e:
            print(e)

        password_hash = None

        if len(password_hash_list) > 0:
            password_hash = password_hash_list[0][0]

        return password_hash


# Подготовка БД.
m_sql = MyDatabaseConnector()
m_sql.create_table()

salt = "user1"

password = input("Введите пароль: \n")

# Соль-часть хеша.
res = hashlib.sha256(salt.encode() + password.encode()).hexdigest()

m_sql.save_password_hash(salt, res)

pass_hash = m_sql.get_password_hash(salt)

print(f"В базе данных хранится строка: {pass_hash}\n")

password = input("Введите пароль еще раз для проверки: \n")

res2 = hashlib.sha256(salt.encode() + password.encode()).hexdigest()

if pass_hash == res2:
    print("Вы ввели правильный пароль!")
else:
    print("Вы ввели не правильный пароль!")
