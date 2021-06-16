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


import hashlib
import sqlite3


def check_hash(login, hash_obj):
    conn = sqlite3.connect('My_DB.sqlite')
    cursor = conn.cursor()
    cursor.execute('select hash from users where login = ?', (login,))
    result = cursor.fetchone()
    conn.close()
    if result is None:
        print('Вы ввели некорректный логин/пароль')
    elif result[0] == hash_obj:
        print('Все корректно')
        return False
    else:
        print('Вы ввели некорректный логин/пароль')

    return


def set_data_db(login, hash_obj):
    conn = sqlite3.connect('My_DB.sqlite')
    cursor = conn.cursor()
    try:
        cursor.execute('insert into users values (?, ?);', (login, hash_obj))
    except sqlite3.IntegrityError:
        print('Данный пользователь уже есть в базе')
    conn.commit()
    conn.close()
    return


Login = input('Для регистрации введите логин ')
Passwd = input('Для регистрации введите пароль ')

My_hash = hashlib.sha256(Login.encode() + Passwd.encode()).hexdigest()
set_data_db(Login, My_hash)

Repeat_login = input('Повторите ввод логина ')
Repeat_pass = input('Повторите ввод пароля ')
Repeat_hash = hashlib.sha256(Repeat_login.encode() + Repeat_pass.encode()).hexdigest()
check_hash(Repeat_login, Repeat_hash)
