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
import sqlite3 as sql


def hash_pass(passwd, salt = 'c46961d58f3347e89eec769d63d33a58'):
    res = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
    return res

conn = sql.connect('lesson3_2.db')
cur = conn.cursor()
cur.execute("""DROP TABLE IF EXISTS users;""")
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   hash TEXT);
""")
conn.commit()

user_input = input('Введите пароль: ')
key = hash_pass(user_input)
print(f'В базе данных хранится строка: {key}')
cur.execute("""INSERT INTO users(userid, hash) 
               VALUES (?,?);""", ('00001', key))
conn.commit()
user_input_2 = input('Введите пароль еще раз для проверки: ')
cur.execute("SELECT hash FROM users WHERE userid = '00001';")
one_result = cur.fetchone()
if one_result[0] == hash_pass(user_input_2):
    print('Вы ввели правильный пароль')
else:
    print('Вы ввели неправильный пароль')