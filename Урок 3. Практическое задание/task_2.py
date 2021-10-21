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

from uuid import uuid4
import hashlib
import sqlite3

# 1 простой вариант
salt = uuid4().hex
passw = '123'

def get_hash(p):
    return hashlib.sha256(salt.encode() + p.encode()).hexdigest()

base_passw = get_hash(passw)
print(base_passw)

def login_1():
    if get_hash(input('Введите пароль: ')) == base_passw:
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели неправильный пароль')

login_1()


# 2 вариант через БД
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS users;")
cursor.execute("""CREATE TABLE users
                  (password_hash VARCHAR(100))
               """)
cursor.execute(f"""INSERT INTO users
                  VALUES ('{base_passw}')
                  """)

sql_pass = cursor.execute("SELECT password_hash FROM users;").fetchone()[0]
conn.close()
print(sql_pass)

def login_2():
    if get_hash(input('Введите пароль: ')) == sql_pass:
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели неправильный пароль')

login_2()