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
# Первый раз работаю с MySQL через питон
# И у меня уже создана бд test_db в ней таблица logins столбцы id, login, pass_log
import mysql.connector
from mysql.connector import Error
from hashlib import sha256


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection("localhost", "root", "1234", 'test_db')


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Запрос выполнен')
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def hash_created(login, password):
    salt = login
    return sha256(password.encode() + salt.encode()).hexdigest()


def insert_db(login, password):
    query = f"""
    INSERT INTO
        `logins` (`login`, `pass_log`)
    VALUES
        ('{login}','{password}');
    """
    return query


def read_db(login):
    query = f"""
    SELECT 
        login, pass_log 
    FROM 
        logins 
    WHERE 
        logins.login = '{login}'
    """
    return query


def login(result):
    if len(result) == 0:
        print('Логин не верный!')
    elif result[0][1] != pass_in_db:  # проверка хэшей
        print('Пороль не верный!')
    elif result[0][1] == pass_in_db:
        print('Вход выполнен')


while True:
    user_input = input('Если вы хотите зарегестрироваться введите "1" для входа "2" для выхода "q": ')
    if user_input == '1':
        login_in_db = input("Введите логин: ")  # Ввод логина
        pass_input = input('Введите пороль: ')  # Ввод пороля
        pass_in_db = hash_created(login_in_db, pass_input)  # высчитывание хэша
        execute_query(connection, insert_db(login_in_db, pass_in_db))  # исполнение запроса на добовление в db
    elif user_input == '2':
        login_in_db = input("Введите логин: ")  # Ввод логина
        pass_input = input('Введите пороль: ')  # Ввод пороля
        pass_in_db = hash_created(login_in_db, pass_input)  # высчитывание хэша
        result = execute_read_query(connection, read_db(login_in_db))  # выполнение запроса на поиск по логину
        # в базе данных и выбока столбцов логин и пароль
        login(result)
    elif user_input == 'q':
        break
