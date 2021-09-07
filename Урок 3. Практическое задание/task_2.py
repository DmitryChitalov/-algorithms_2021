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
import mysql.connector


def pass_input():
    global password, salt
    password = input('Введите пароль: ')
    salt = uuid4().hex


def pass_output():
    print(f'В базе данных хранится строка: {password_hash}')
    password_repeat = input('Введите пароль еще раз для проверки: ')
    if password_hash == hashlib.sha256(salt.encode() + password_repeat.encode()).hexdigest():
        print('Вы ввели правильный пароль')
    else:
        print('Проверьте пароль')


# Запись хэша в файл
pass_input()

with open("hash.txt", "w", encoding="utf-8") as f:
    f.write(str(hashlib.sha256(salt.encode() + password.encode()).hexdigest()))
with open("hash.txt", "r", encoding="utf-8") as f:
    for row in f:
        password_hash = row

pass_output()

# -------------------------------------------------------------------------------------------------------
# Запись хэша в БД MySQL
pass_input()

conn = mysql.connector.connect(host='localhost', database='hash', user='root', password='qwer1234')
cursor = conn.cursor()
cursor.execute("""TRUNCATE TABLE passwords""")
sql_write = """INSERT INTO passwords (id, password_hash) VALUES (%s, %s)"""
cursor.execute(sql_write, (1, hashlib.sha256(salt.encode() + password.encode()).hexdigest()))
conn.commit()
sql_read = """SELECT password_hash FROM passwords WHERE id = 1"""
cursor.execute(sql_read)
results = cursor.fetchall()
password_hash = str(results).split("'")[1]
# print(password_hash)
conn.close()

pass_output()
