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
from uuid import uuid4
import pymysql

SALT = uuid4().hex


def salted_hash(pw: str, slt=SALT) -> str:
    return hashlib.sha256(pw.encode() + slt.encode()).hexdigest()


def password_memory(salt=SALT) -> str:
    print('ЧЕРЕЗ ПАМЯТЬ'.center(40, '*'))
    p = input('Введите пароль: ')
    hashed_pass = salted_hash(p)
    p = input('Введите пароль еще раз для проверки: ')
    return 'Вы ввели правильный пароль' \
        if salted_hash(p) == hashed_pass \
        else 'Пароль не верный'


def password_file(salt=SALT, name='passwd.txt'):
    print('ЧЕРЕЗ ФАЙЛ'.center(40, '*'))
    p = input('Введите пароль: ')
    hashed_pass = salted_hash(p)
    with open(name, 'w') as f:
        f.write(hashed_pass)
    p = input('Введите пароль еще раз для проверки: ')
    with open(name, 'r') as f:
        hashed_pass = f.readline()
    return 'Вы ввели правильный пароль' \
        if salted_hash(p) == hashed_pass \
        else 'Пароль не верный'


def passwd_db(salt=SALT):
    print('ЧЕРЕЗ MARIA-DB'.center(40, '*'))
    p = input('Введите пароль: ')
    hashed_pass = salted_hash(p)
    con = pymysql.connect(host='localhost', user='root', password='', database='pythontest')
    with  con:
        cur = con.cursor()
        cur.execute('CREATE DATABASE IF NOT EXISTS pythontest')
        cur.execute('DROP TABLE IF EXISTS task2')
        cur.execute('CREATE TABLE task2 (pw VARCHAR(255))')
        cur.execute('INSERT INTO task2(pw) VALUES (%s)', (hashed_pass))
        con.commit()
    p = input('Введите пароль еще раз для проверки: ')
    with pymysql.connect(host='localhost', user='root', password='', database='pythontest') as con:
        cur = con.cursor()
        cur.execute('SELECT pw FROM task2')
        res = cur.fetchone()[0]
    return 'Вы ввели правильный пароль' \
        if salted_hash(p) == res \
        else 'Пароль не верный'


if __name__ == '__main__':
    print(password_memory())
    print(password_file())
    print(passwd_db())
    exit(0)

'''
**************ЧЕРЕЗ ПАМЯТЬ**************
Введите пароль: 1
Введите пароль еще раз для проверки: 1
Вы ввели правильный пароль
***************ЧЕРЕЗ ФАЙЛ***************
Введите пароль: 2
Введите пароль еще раз для проверки: 2
Вы ввели правильный пароль
*************ЧЕРЕЗ MARIA-DB*************
Введите пароль: 3
Введите пароль еще раз для проверки: 3
Вы ввели правильный пароль
'''
