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
import sqlite3
from sqlite3 import Error
from hashlib import pbkdf2_hmac
from binascii import hexlify
from uuid import uuid4


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print('Успешное подключение')
    except Error as err:
        print(f'Ошибка подключения {err}')
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Запрос выполнен')
    except Error as err:
        print(f'Ошибка: {err}')


def hash_password(password):
    salt = uuid4().hex
    obj_pass = pbkdf2_hmac(hash_name='sha256',
                           password=password.encode(),
                           salt=salt.encode(),
                           iterations=1000)
    rez_pass = hexlify(obj_pass)
    return rez_pass


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f'Ошибка: {err}')


def reg_func(connection):
    password = input('Введите пароль: ')
    create_password_table = 'CREATE TABLE IF NOT EXISTS password_tb (id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                            'password_hash CHAR(256),' \
                            'password CHAR(20))'  # сам пароль пишу в бд для отладки, можно убрать, но я оставила
    execute_query(connection, create_password_table)  # для наглядности
    insert_password = f'INSERT INTO password_tb(password_hash,password)' \
                      f'VALUES ("{hash_password(password)}","{password}")'
    execute_query(connection, insert_password)


def check_password(connection):
    check_password = input('Введите пароль для авторизации: ')
    rez_hash = hash_password(check_password).decode()
    select_password = f"SELECT * FROM password_tb"
    rez = execute_read_query(connection, select_password)
    count = 0
    for r in rez:  # мне кажется, не самы оптимальнй вариант решения, но другой не придумала, буду рада, если подскажете
        if r[1][2:-1] == rez_hash:  # как реализовать это более корректно
            count += 1
    if count > 0:
        print('Авторизация пройдена')
    else:
        print('Введен неверный пароль')


def work_func(connection):
    key = input('Для регистрации введите 0\nДля авторизации нажмите 1\nДля выхода нажмите 2\n: ')
    choice_dict = {'0': reg_func, '1': check_password}
    if key == '2':
        return None
    else:
        choice_dict[key](connection)
        return work_func(connection)


path = 'C:\\Users\\Meloch_Puzastiy\\Desktop\\курсы\\Алгоритмы\\HW_3\\db.sqlite'
connection = create_connection(path)
work_func(connection)
