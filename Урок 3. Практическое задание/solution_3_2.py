import pymysql
import hashlib
from uuid import uuid4

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


def to_hash(val, salt):
    return hashlib.sha256(val.hexdigest().encode() + salt.encode()).hexdigest()


def valid_pass(n, slt):
    res = to_hash(n, slt)
    print(res)
    check_pswrd = hashlib.sha256(input('Повторите пароль - ').encode())
    res_check = to_hash(check_pswrd, slt)
    if res == res_check:
        con = pymysql.connect(host="localhost", user="root", password="*******", db="******")
        with con:
            cur = con.cursor()
            cur.execute("USE password")
            cur.execute(f"INSERT INTO salt (salt) VALUES ('{slt}')")
            cur.execute(f"INSERT INTO passwords (pswrd) VALUES ('{res}')")
            con.commit()
        cur.close()
        print('Пароль успешно сохранен')
    elif res != res_check:
        print('Пароли не совпадают')
    else:
        print('Error password')


con = pymysql.connect(host="localhost", user="root", password="*******", db="******")

with con:
    cur = con.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS password")
    cur.execute("USE password")
    cur.execute("CREATE TABLE IF NOT EXISTS passwords(id SERIAL, pswrd VARCHAR(255))")
    cur.execute("CREATE TABLE IF NOT EXISTS salt(id SERIAL, salt VARCHAR(255))")
cur.close()

valid_pass(hashlib.sha256(input('Введите пароль - ').encode()), uuid4().hex)
