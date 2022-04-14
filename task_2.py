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
import json
from uuid import uuid4
import hashlib


def input_logi():
    log = input("Введите логин: ")
    passwd = input("Введите пароль: ")
    salt = log
    return log, passwd, salt


def create_hesh(p, s):
    return hashlib.sha256(s.encode('utf-8') + p.encode('utf-8')).hexdigest()


def create_dict(l, r, s_d):
    if l in s_d:
        return s_d
    else:
        s_d.update({l: r})
        return s_d


def add_in_file(l_d):
    with open('task_2.json', 'w') as f:
        json.dump(l_d, f)
    return True


def load_from_file():
    try:
        with open('task_2.json', 'r') as f:
            l_d = json.load(f)
            return l_d
    except FileNotFoundError:
        print("Файла с данными еще не существует")
        l_d = {}
        return l_d


def check_user(d_u):
    log, passwd, salt = input_logi()
    res = create_hesh(passwd, salt)
    if res == d_u[log]:
        print("Ваш логин и пароль верны")
        return True
    else:
        print("Ваш логин и пароль не верны. Попробуйте еще раз")
        return False


user_login, user_password, user_salt = input_logi()
res = create_hesh(user_password, user_salt)
start_dict = load_from_file()
login_date = create_dict(user_login, res, start_dict)
add_in_file(login_date)
date_users = load_from_file()
print("Проверка правильности логина и пароля")
print(check_user(date_users))
