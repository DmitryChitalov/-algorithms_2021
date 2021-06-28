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

from uuid import uuid4
import hashlib
import sqlite3
import random

def s_password(value):
    #salt = uuid4().hex
    #ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars = str()
    for i in range(16):
        chars.format(i)
    return hashlib.sha256(chars.encode("utf-8") + value.encode("utf-8")).hexdigest()


with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    user_password = input("Введите пароль: ")
    query = """ CREATE TABLE IF NOT EXISTS password (id INTEGER, name TEXT)"""
    cursor.execute(query)
    salt_user_password = s_password(user_password)
    query1 = f"""INSERT INTO password (id, name) VALUES(1, '{salt_user_password}')"""
    cursor.execute(query1)
    db.commit()
    print(f'В базе данных хранится строка: {salt_user_password}')
    check_password = input("Введите пароль еще раз для проверки: ")
    s_password(check_password)
    cursor.execute("SELECT * FROM password WHERE id=1")
    result = cursor.fetchall()
    for row in result:
        if s_password(check_password) == row[1]:
            print("Вы ввели правильный пароль")
        else:
            print("Вы ввели не правильный пароль")

db.close()





















"""import hashlib
from uuid import uuid4


def hash_password(value):
    salt = "password"
    return hashlib.sha256(salt.encode("utf-8") + value.encode("utf-8")).hexdigest()



def password():
    with open("hash.txt", 'w+', encoding='utf-8') as f:
        user_answer = input("Введите пароль: ")
        hash_obj = hash_password(user_answer)
        print(hash_obj)
        f.write(hash_obj)
        check_answer = input("Введите пароль еще раз для проверки: ")
        hash_obj_1 = hash_password(check_answer)
        print(hash_obj_1)
        f.seek(0)
        if hash_obj_1 == f.read():
            print("Вы ввели правильный пароль")
        else:
            print("Вы ввели не правильный пароль")


password()"""