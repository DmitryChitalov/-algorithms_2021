import hashlib

import MySQLdb
from MySQLdb import OperationalError


def creature(connect):
    try:
        connect.execute("CREATE TABLE hash_table(hash_password VARCHAR(255));")
        result = connect.fetchone()
        return result
    except OperationalError:
        print('Таблица уже есть!')


def registration():
    login = input('Введите логин: ')
    passwd = input('Введите пароль: ')
    hash_x = hashlib.sha256(login.encode() + passwd.encode()).hexdigest()
    return hash_x


def entrance(connect):
    reg_hash = registration()
    insert_table = f"INSERT INTO hash_table (hash_password) VALUES ('{reg_hash}')"
    connect.execute(insert_table)
    conclusion = "select * from hash_table"
    reg_hash_2 = registration()
    connect.execute(conclusion)
    data = connect.fetchall()
    if reg_hash_2 == data[0:]:
        print('вы вошли в систему')
    else:
        print('неправильный логин или пароль')


conn = MySQLdb.connect('localhost', 'root', '0895', 'python')
creating_logging = conn.cursor()
creature(creating_logging)
entrance(creating_logging)
