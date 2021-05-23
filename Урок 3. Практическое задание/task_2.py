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


import sqlite3
from datetime import datetime
import hashlib

"""Функция создания базы данных"""


def create_database():
    global sqlite_connection
    try:
        sqlite_connection = sqlite3.connect('users.db')
        sqlite_create_table_query = '''CREATE TABLE users(
                                    login TEXT(255) NOT NULL,
                                    password TEXT(255) NOT NULL,
                                    activate BOOLEAN NOT NULL,
                                    first_name TEXT(255) NOT NULL,
                                    second_name TEXT(255) NOT NULL,
                                    email TEXT(255) NOT NULL UNIQUE,
                                    phone_num TEXT(255) NOT NULL UNIQUE,
                                    date_reg DATETIME);'''

        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        print("Таблица SQLite создана")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


""" Функция запроса данных у пользователя, создание хеш паролей, внесение их в базу данных"""


def insert_user_data():
    #  Запрашиваем данные пользователя, хешируем пароль усиливаем  хешем от логина

    login = input('Введите ваш логин: ').lower()

    if login == '':
        print('Значение не может быть пустым!')
    else:
        login_hash = hashlib.sha256(login.encode())
    password = input('Введите ваш пароль: ')
    if password == '':
        print('Значение не может быть пустым!')
    else:
        password = hashlib.sha256(password.encode() + b'{login_hash}').hexdigest()

    activate = False
    first_name = input('Введите ваше имя: ')
    second_name = input('Введите вашу фамилию: ')
    email = input('Введите ваш e-mail: ')
    phone_num = input('Введите ваш номер: ')
    date_reg = datetime.now()

    #  Открываем базу данных для записи данных регистрации

    database = sqlite3.connect('users.db')
    cursor = database.cursor()
    data_user = '''INSERT INTO users(login, password, activate, first_name, second_name, email, phone_num, date_reg)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);'''
    # Формируем кортеж для записи
    data_tuple = (login, password, activate, first_name, second_name, email, phone_num, date_reg)

    cursor.execute(data_user, data_tuple)
    database.commit()
    cursor.close()
    print('Данные сохранены! Скопируйте выданный вам ключ для активации учетной записи!')
    print(password)
    activation()


"""Функция активации учетной записи"""


def activation():
    # Конектимся к DB
    database = sqlite3.connect('users.db')
    cursor = database.cursor()
    # Запрашиваем логин и выданый ключ для активации учетки
    # Не хватило терпения сделать проверку на наличия пользователя в базе.
    login = input('Введите ваш логин: ').lower()
    password_hash = input('Вставьте полученный код активации')
    cursor.execute("SELECT * FROM users WHERE login=?", [login])
    search = cursor.fetchone()
    # Сравнение хешей для активации, вносим данные об активации учетной записи
    if password_hash == search[1]:
        print('Поздравляю ваша учетная запись активирована! Можете войти используя свой логин и пароль!')
        cursor.execute("UPDATE users SET activate = 1 WHERE login=?", [login])
        database.commit()
        cursor.close()
        user_login()
    else:
        print('Ваш код активации не совпадает, запросите его еще раз!')


def user_login():
    # Конектимся к DB

    database = sqlite3.connect('users.db')
    cursor = database.cursor()

    login = input('Введите ваш логин: ').lower()
    password = input('Введите пароль: ')
    login_hash = hashlib.sha256(login.encode())
    password_hash = hashlib.sha256(password.encode() + b'{login_hash}').hexdigest()

    cursor.execute("SELECT * FROM users WHERE login=?", [login])
    search = cursor.fetchone()
    # Сравнение хешей для авторизации, вносим данные об активации учетной записи
    if password_hash == search[1]:
        print('Доступ разрешен!!')
        cursor.close()
    else:
        print('Логин/Пароль не верный')


# create_database()
insert_user_data()
# activation()
# user_login()
