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


import sqlite3 as sqlite
from hashlib import sha256
from uuid import uuid4


def sqlite3_connect(database_path):
    connect = sqlite.connect(database_path)

    cursor = connect.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT, salt TEXT)')
    return connect


def registration(connection):
    __salt__ = uuid4().hex
    __username__ = input_value('логин')
    __password__ = input_value("пароль")
    __password_str__ = f'{__password__}{__salt__}'
    __password_obj__ = sha256(__password_str__.encode('utf-8'))
    __pass_hex_dig__ = __password_obj__.hexdigest()

    cursor = connection.cursor()

    cursor.execute('INSERT INTO users(username, password, salt) VALUES(?, ?, ?)', (__username__.lower(), __pass_hex_dig__, __salt__))
    connection.commit()

    print(f'Вы успешно зарегистрировались. Ваш хеш-пароль: {__pass_hex_dig__}')


def authorization(connection):
    authorization_data = {'registered': False}

    __username__ = input('Введите логин:\n')

    cursor = connection.cursor()

    if __username__ is not None:
        cursor.execute('SELECT * FROM users WHERE username=:username', {'username': __username__.lower()})
        query_result = cursor.fetchall()

        if len(query_result):
            authorization_data = {'registered': True, 'password': query_result[0][1], 'salt': query_result[0][2]}

    return authorization_data


def register_question():
    result = input('Вы не зарегистрированы. Желаете зарегистрироваться? (Y/n): ')
    if result == 'n':
        return False
    elif result == 'Y':
        return True
    else:
        return register_question()


def input_value(desc):
    __value__ = input(f'Введите новый {desc}:\n')

    if __value__ == '':
        return input_value(desc)
    else:
        return __value__


def check_password(__password__, __auth_data__):
    __salt__ = __auth_data__.get('salt')
    __password_str__ = f'{__password__}{__salt__}'
    __password_obj__ = sha256(__password_str__.encode('utf-8'))
    __pass_hex_dig__ = __password_obj__.hexdigest()

    return __password_obj__.hexdigest() == __auth_data__.get('password')


if __name__ == '__main__':

    db_path = './volkovan_task2.db'
    sqlite_connection = sqlite3_connect(db_path)
    auth_data = authorization(sqlite_connection)
    if not auth_data.get('registered'):
        if register_question():
            registration(sqlite_connection)
    else:
        input_password = input('Введите Ваш пароль для авторизации:\n')
        if check_password(input_password, auth_data):
            print('Вы успешно авторизовались')
        else:
            print('Неверный пароль')
