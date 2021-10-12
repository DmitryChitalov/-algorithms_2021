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

import hashlib
from os import path


def create_hash_from(password):
    salt = 'salt'
    return hashlib.sha256(salt.encode()+password.encode()).hexdigest()


def create_new_user():
    us_login = input('Придумайте логин: ')
    us_password = input('Придумайте пароль: ')
    us_hash = create_hash_from(us_password)

    with open('data.txt', 'a+') as file:
        file.write(f'{us_login}={us_hash}\n')


def authentication(path_to_BD):
    us_log = input('Введите логин: ')
    with open(path_to_BD, 'r') as file:
        for el in file.readlines():
            log, passw = el.split('=')
            if us_log == log:
                us_pass = input(f'Пользователь {us_log} теперь введите пароль: ')
                if passw == create_hash_from(us_pass) + '\n':
                    return '\033[92m{}\033[00m'.format(f'======>>>>> Welcome {us_log} <<<<<======')
                    # return f'Welcome {us_log}'
                else:
                    return '\033[91m{}\033[00m'.format(f'======>>>>> Пароль указан не верно! <<<<<======')
                    # return f'Пароль указан не верно!'    
        else:
            return '\033[93m{}\033[00m'.format(f'======>>>>> Пользователя с ником {us_log} не существует! <<<<<======')
            # return f'Пользователя с ником {us_log} не существует!'
            

create_new_user()
print(authentication(path_to_BD='data.txt'))




# Это оставлю здесь, чтобы не потерять, как с Python к MySQL
# from getpass import getpass
# from mysql.connector import connect, Error
# https://proglib.io/p/python-i-mysql-prakticheskoe-vvedenie-2021-01-06

