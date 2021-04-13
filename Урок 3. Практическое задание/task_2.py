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
from hashlib import sha256
from uuid import uuid4


def password_hash():
    password = input('Введите пароль: ')
    salt = uuid4().hex
    pw_first_hash = sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    file = open('db.txt', 'w')
    file.write(pw_first_hash + ':' + salt)
    file.close()
    print(f'В файл "db.txt" записана строка - {pw_first_hash}')


def password_check():
    password = input('Введите пароль повторно для проверки: ')
    file = open('db.txt', 'r')
    f_str = file.readline()
    file.close()
    f_str = f_str.split(':')
    pw_sec_hash = sha256(password.encode('utf-8') + f_str[1].encode('utf-8')).hexdigest()
    if pw_sec_hash == f_str[0]:
        print('Вы ввели правильный пароль')
    else:
        print('Неправильный пароль!')


password_hash()
password_check()
