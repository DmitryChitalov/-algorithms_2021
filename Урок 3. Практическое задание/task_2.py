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
import uuid
import sqlite3

def make_hash(password,salt_in=""):
    """ Generate password hash with salt. If salt not present, it random generate"""
    if salt_in == "":
        salt_in =uuid.uuid4().hex.encode('utf-8')[:4]
    return salt_in,hashlib.sha256(salt_in + password.encode('utf-8')).hexdigest()

def write_data(salt_in, hash_in):
    """Write salt and password hash in database"""
    with sqlite3.connect('pass_hash_db') as phdb:
        cursor = phdb.cursor()
        cursor.execute(""" DROP TABLE IF EXISTS password_hash""")
        cursor.execute("""CREATE TABLE  password_hash (salt TEXT, password_hash TEXT)""")
        cursor.execute("""INSERT INTO password_hash (salt, password_hash)
        VALUES (?, ?)""",(salt_in,hash_in))
        phdb.commit()

def get_hash_from_db():
    """get hash and salt from db"""
    with sqlite3.connect('pass_hash_db') as phdb:
        cursor = phdb.cursor()
        cursor.execute(""" SELECT salt, password_hash FROM password_hash""")
        return cursor.fetchone()

if __name__ == '__main__':
    salt, pass_hash = make_hash(input('Введите пароль:'))
    write_data(salt,pass_hash)
    print(f'В базу данных записан хеш пароля: {pass_hash}')
    salt, db_hash = get_hash_from_db()
    if db_hash == make_hash(input('Введите пароль еще раз:'), salt)[1]:
        print('Вы ввели правильный пароль.')
    else:
        print('Введенный пароль неверный.')
