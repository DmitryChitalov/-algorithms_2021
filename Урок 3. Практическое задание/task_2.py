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

import sqlite3
from uuid import uuid4
import hashlib


us_pass = input('Введите пароль: ')

salt = uuid4().hex

passwd = hashlib.sha256(salt.encode() + us_pass.encode()).hexdigest()

# cursor.execute("""INSERT INTO users(password_hash)
#                   VALUES (passwd)
#                 """)

print(passwd)


conn = sqlite3.connect("test_al.db")
cursor = conn.cursor()

cursor.execute("""DROP TABLE IF EXISTS users
                """)
cursor.execute("""CREATE TABLE users
                   (id primary_key AUTO_INCREMENT, password_hash text)
                """)


def sql_insert(conn, password_hash):


    cursor.execute('INSERT INTO users(id, password_hash) VALUES(?,?)', password_hash)

    conn.commit()

password_hash = (1, passwd)

sql_insert(conn, password_hash)

select_passwd = cursor.execute("SELECT password_hash FROM users WHERE id = 1")

result = cursor.fetchone()
passwd_2 = str(*result)

us_pass = input('Введите пароль для потдверждения: ')

passwd_3 = hashlib.sha256(salt.encode() + us_pass.encode()).hexdigest()

if passwd_2 == passwd_3:
    print('Вы ввели правильный пароль')
else:
    print('Вы ввели неправильный пароль')
