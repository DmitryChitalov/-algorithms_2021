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

import mysql.connector
from hashlib import pbkdf2_hmac
from binascii import hexlify
conn = mysql.connector.connect(host='localhost', database='users', user='root', password='1234')
cursor = conn.cursor()
insert_f = 'INSERT INTO user_info (user_login, user_password) VALUES (%s, %s)'


def insert_pass():
    reg_password = input('Введите пароль для регистрации')
    pass_hash_1 = pbkdf2_hmac(hash_name='sha256',
                              password=reg_password.encode(),
                              salt=reg_login.encode(),
                              iterations=100000)
    approve_pass = input('Подтвердите пароль')
    pass_hash_2 = pbkdf2_hmac(hash_name='sha256',
                              password=approve_pass.encode(),
                              salt=reg_login.encode(),
                              iterations=100000)
    if pass_hash_1 == pass_hash_2:
        hashed_pass = hexlify(pass_hash_2)
        user_info = (reg_login, hashed_pass)
        insert_function = "INSERT INTO user_info (user_login, user_password) VALUES (%s, %s)"
        cursor.execute(insert_function, user_info)
        conn.commit()
        print('Операция прошла успешно, вы зарегистрированы')
    else:
        print('Пароли не совпадают, вы будете перенаправлены на повторное введение пароля.')
        return insert_pass()


reg_login = input('Введите логин для регистрации')
insert_pass()
