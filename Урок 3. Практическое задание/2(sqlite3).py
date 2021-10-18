import hashlib

import sqlite3
from sqlite3 import OperationalError


def conect_db():
    conn = sqlite3.connect("hesh_db.sqlite")
    connect = conn.cursor()
    return connect, conn


def creature():
    connect, conn = conect_db()
    result = "CREATE TABLE hash_table(user_login VARCHAR(255)," \
             "hash_password VARCHAR(255));"
    try:
        connect.execute(result)
    except OperationalError:
        print('Таблица уже есть!')
    else:
        conn.commit()
        print("операция прошла успешно")


def introductory():
    login = input('Введите логин: ')
    passwd = input('Введите пароль: ')
    hash_x = hashlib.sha256(login.encode() + passwd.encode()).hexdigest()
    return hash_x, login


def registration():
    connect, conn = conect_db()
    reg_hash, login = introductory()
    connect.execute(f"INSERT INTO hash_table (user_login, hash_password) VALUES ('{login}', '{reg_hash}')")
    conn.commit()
    print('Вы зарегестрировались')


def entrance():
    connect, conn = conect_db()
    check_hash, login = introductory()
    connect.execute(f"SELECT * FROM hash_table WHERE user_login = '{login}'")
    shipment = connect.fetchone()
    if check_hash == shipment[1]:
        print('Вы вошли в систему')
    else:
        print('Пароль или логин не совпадают!')


creature()
registration()
entrance()
