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
import sqlite3

connection = sqlite3.connect('users.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                    userid INTEGER primary key autoincrement,
                    login varchar(20),
                    password varchar(100)
                );""")
connection.commit()


def get_hash(usr, pwd):
    usr_hash = pbkdf2_hmac('sha256', pwd.encode(), usr.encode(), 100000)
    return usr_hash.hex()


def registration():
    login = input("Логин: ")
    cursor.execute(f"""SELECT userid FROM users WHERE login = '{login}';""")
    result = cursor.fetchone()
    if result == None:
        password = input("Пароль: ")
        cursor.execute(f"""INSERT INTO users(login, password) VALUES
                    ('{login}', '{get_hash(login, password)}');""")
        connection.commit()
    else:
        print('Такой пользователь уже создан')
        registration()


def validation(login=input("Логин: "), err=0):
    cursor.execute(f"""SELECT password FROM users WHERE login = '{login}';""")
    result = cursor.fetchone()
    if result == None:
        print('Такого пользователя не существует')
        validation(input("Логин: "))
    elif result[0] == get_hash(login, input('Введите пароль: ')):
        print(f"Добро пожаловать, {login}")
    else:
        if err != 3:
            print('Неверно указаны Пользователь/Пароль.')
            validation(login, err+1)
        else:
            print('Попытки закончились')


# registration()
validation()
