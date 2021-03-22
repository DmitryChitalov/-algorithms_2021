"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""

from hashlib import pbkdf2_hmac
from binascii import hexlify
import sqlite3


def connection_database():
    """
    Функция для создания подключения к БД
    :return: возращает подключение
    """
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    return cursor, conn


def create_table(cursor, conn):
    """
    Функция для создания таблиц БД
    :param cursor: для обращения к БД
    :param conn: для обращения к БД
    :return: -
    """
    cursor.execute("""DROP TABLE IF EXISTS users;""")
    cursor.execute("""
        CREATE TABLE users (
                            user_name varchar(255),
                            password text,
                            salt text);
        """)
    conn.commit()


def read_database_users(cursor, user_name):
    """
    Функция для поиска пользователя в БД
    :param cursor: для обращения к БД
    :param user_name: исковый пользователь, логин
    :return: информация по пользователю
    """
    cursor.execute("""
                    SELECT user_name, password, salt FROM users
                    WHERE user_name = ?
                    ;
            """, user_name)
    records = cursor.fetchall()
    return records


def insert_database(cursor, conn, data_users):
    """
    Функция для добавления пользователей в БД
    :param cursor: для обращения к БД
    :param conn: для обращения к БД
    :param data_users: информация для добавления
    :return: -
    """
    cursor.execute("""
                    SELECT user_name, password, salt FROM users
                    WHERE user_name = ?
                    ;
            """, [data_users[0]])
    records = cursor.fetchall()
    if not records:
        cursor.execute("""
                            INSERT INTO users VALUES (?, ?, ?);
                            """, data_users)
        conn.commit()
    else:
        print(f'Пользователь: {data_users[0]} уже есть в БД!')


def password_hash(user_name, user_password):
    """
    Функция для проверки у/з, сверка с данными БД
    :param user_name: логин для проверки
    :param user_password: пароль для проверки
    :return: результат проверки
    """
    pass_obj = pbkdf2_hmac(hash_name='sha256',
                           password=user_password.encode('UTF-8'),
                           salt=user_name.encode('UTF-8'),
                           iterations=10000)
    return user_name, hexlify(pass_obj), hexlify(user_name.encode('UTF-8'))


def check_password(cursor):
    login = input('Введите ваш логин: ').lower()
    password = input('Введите ваш пароль: ')
    data = read_database_users(cursor, [login])
    if data:
        if data[0][1] == (password_hash(login, password))[1]:
            print('Доступ разрешен! Пароль верный!')
        else:
            print('Ошибка, пароль не верный!')
    else:
        print('Ошибка, не найден пользователь с таким логином')


# создаем подключение
cur, connect = connection_database()
# создаем таблицы
create_table(cur, connect)
# выполняем хеширование
data_from_base = password_hash(input('Введите логин: ').lower(), input('Введите пароль: '))
print(f'Данные до БД: {data_from_base}')
# добавляем данные пользователя в бд
insert_database(cur, connect, list(data_from_base))
# авторизация (проверка)
check_password(cur)
