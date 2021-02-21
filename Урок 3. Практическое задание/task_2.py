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


from hashlib import pbkdf2_hmac
from os import urandom
from psycopg2 import OperationalError, connect
from binascii import hexlify


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def password_hash():
    user = input("Введите логин: ")
    password = input("Введите пароль: ")
    salt = urandom(32)
    obj = pbkdf2_hmac(hash_name="sha256",
                      password=password.encode(),
                      salt=salt,
                      iterations=1000)
    return user, hexlify(obj), hexlify(salt)


def check_password():
    connection = create_connection("postgres", "postgres", "", "192.168.1.37", "5433")
    user1 = input("Введите логин: ")
    password = input("Введите пароль: ")
    select_users = f"SELECT * FROM users WHERE users = '{user1}'"
    users = execute_read_query(connection, select_users)
    salt = bytes(users[3])
    obj = pbkdf2_hmac(hash_name="sha256",
                      password=password.encode(),
                      salt=salt,
                      iterations=1000)
    x = bytes(users[2])
    y = hexlify(obj)
    if bytes(users[2]) == hexlify(obj):
        return "Вы ввели правильный пароль!"
    else:
        return "Пароль неверный!"


con = create_connection("postgres", "postgres", "", "192.168.1.37", "5433")
# Создаем таблицу в БД
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  users TEXT NOT NULL,
  password bytea,
  salt bytea
)
"""
# Запрашиваем логин, пароль
execute_query(con, create_users_table)
# Заливаем логин, хэш и соль в БД
user = [password_hash()]
user_records = ", ".join(["%s"] * len(user))
insert_query = (
    f"INSERT INTO users (users, password, salt) VALUES {user_records}"
)
con.autocommit = True
cursor = con.cursor()
cursor.execute(insert_query, user)
# Проверка логина/пароля
print(check_password())
