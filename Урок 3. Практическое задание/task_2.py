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
from sqlite3 import Connection

SALT = b'Salted__'


def create_structure(con: Connection):
    create_table = """
    CREATE TABLE passwords(
        password TEXT       
    );
    """
    con.execute(create_table)


def create_credential(con: Connection):
    password = input('введите пароль\n')
    hashed_pass = hashlib.sha256(SALT + password.encode()).hexdigest()
    print(hashed_pass)
    sql = f"""
        INSERT INTO 'passwords'(password) VALUES ('{hashed_pass}')
    """
    with con:
        con.execute(sql)


def check_credential(con: Connection):
    password = input('введите пароль\n')
    hashed_pass = hashlib.sha256(SALT + password.encode()).hexdigest()
    sql = f"""
        SELECT ROWID, * FROM passwords
        WHERE password = '{hashed_pass}'
    """
    cur = con.cursor()
    cur.execute(sql)
    print(cur.fetchone())


if __name__ == '__main__':
    connection = sqlite3.connect(":memory:")
    create_structure(connection)
    create_credential(connection)
    check_credential(connection)
