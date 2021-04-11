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

import sqlite3
from binascii import hexlify
from hashlib import pbkdf2_hmac, blake2b

sqlite_connection = sqlite3.connect('sqlite.db')
cursor = sqlite_connection.cursor()

sqlite_create_table_query = '''CREATE TABLE password_db (
                                id INTEGER PRIMARY KEY,
                                hash_password TEXT NOT NULL
                                );'''

#cursor.execute(sqlite_create_table_query)


def check_password(password, login, variant):
    password_generate = blake2b()
    password_generate.update(pbkdf2_hmac(hash_name='sha256',
                                     password=password.encode(),
                                     salt=login.encode(),
                                     iterations=100000)
    )
    sqlite_select_pass_query = f'''select count(hash_password) from password_db where hash_password = '{password_generate.hexdigest()}';'''
    cursor.execute(sqlite_select_pass_query)
    cursor_fet = cursor.fetchone()
    if ( cursor_fet[0] > 0):
        if( variant == 1):
            print('Повтор ввода пароля')
            return 1
        else:
            print('Вы ввели правильный пароль')
    else:
        if( variant == 0):
            print('Вы ввели не правильный пароль')

def new_password(password,login):
    if (check_password(password, login , 1) == 1):
        exit(1)
    else:
        password_generate = blake2b()
        password_generate.update(pbkdf2_hmac(hash_name='sha256',
            password=password.encode(),
            salt=login.encode(),
            iterations=100000)
        )
        sqlite_insert_pass_query = f'''insert into password_db (hash_password) values ('{password_generate.hexdigest()}');'''
        print(f"В базе данных хранится строка: {password_generate.hexdigest()}")
        cursor.execute(sqlite_insert_pass_query)
        sqlite_connection.commit()
        
login = input('Введите логин: ')
new_password(input('Введите пароль: '), login)
check_password(input('Введите пароль еще раз для проверки: '), login, 0)

