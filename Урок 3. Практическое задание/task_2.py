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
# sqlite, postgres, db_api, orm
from mysql.connector import connect, Error
from hashlib import pbkdf2_hmac
from binascii import hexlify
# from getpass import getpass

try:
    with connect(
            host='192.168.1.100',
            user='root',  # input('username: '),
            password='password',  # getpass('password: ')
    ) as connection:
        db_query = """DROP DATABASE IF EXISTS py_test_db;
        CREATE DATABASE py_test_db;"""
        with connection.cursor() as cursor:
            cursor.execute(db_query, multi=True)
            connection.commit()
except Error as e:
    print(f'Ошибка: {e}')


def create_connection(host, user, password, db):
    try:
        connection = connect(
            host=host,
            user=user,  # input('username: '),
            password=password,  # getpass('password: ')
            database=db
        )
        return connection
    except Error as e:
        print(f'Ошибка: {e}')


def register():
    login = input('login: ')
    password = input('Введите пароль: ')
    password2 = input('Повторите пароль: ')
    while password != password2:
        print('Пароли не совпадают!')
        password = input('Введите пароль: ')
        password2 = input('Повторите пароль: ')
    else:
        password_hash = hexlify(pbkdf2_hmac(hash_name="sha256",
                                            password=password.encode(),
                                            salt=b'some_salt',
                                            iterations=10))
        try:
            insert_query = f'''INSERT INTO users (login, password_hash) VALUES ("{login}", 
                            "{password_hash.decode()}")'''
            for result in cursor.execute(insert_query, multi=True):
                pass
            connection.commit()
        except Error as e:
            print(f'Ошибка: {e}')


def validate():
    login = input('login: ')
    password = input('Введите пароль: ')
    password = hexlify(pbkdf2_hmac(hash_name="sha256",
                                   password=password.encode(),
                                   salt=b'some_salt',
                                   iterations=10)).decode()
    try:
        db_query = f'''SELECT password_hash FROM users
        WHERE login = "{login}"'''
        cursor.execute(db_query)
        selected_hash = cursor.fetchone()
        if selected_hash is None:
            print('Логин или пароль указан неверно')
            return
        if password in selected_hash:
            print('success')
        else:
            print('Логин или пароль указан неверно')
    except Error as e:
        print(f'Ошибка: {e}')


connection = create_connection('192.168.1.100', 'root', 'password', 'py_test_db')

db_query = """DROP TABLE IF EXISTS users;
            CREATE TABLE users (
                id serial PRIMARY KEY,
                login VARCHAR(100) UNIQUE,
                password_hash VARCHAR(255));"""

cursor = connection.cursor()
for result in cursor.execute(db_query, multi=True):
    pass

register()
validate()

connection.close()
