"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
# sqlite, postgres, db_api, orm

import sqlite3
import hashlib

conn = sqlite3.connect(r'db/users.db')
cur = conn.cursor()

cur.execute("""DROP TABLE IF EXISTS users;""")
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   login TEXT NOT NULL UNIQUE,
   pass TEXT);
""")
conn.commit()

print("#" * 100)
print("Регистрация пользователя")
user = input("Введите логин: ")
pass_log = input("Введите пароль: ")
res = hashlib.sha256(user.encode() + pass_log.encode()).hexdigest()
log_pass = (user, res)
print("пароль {}, хэш пароля {}".format(pass_log, res))
cur.execute("INSERT INTO users(login,pass) VALUES(?, ?);", log_pass)

print("#" * 100)
print("Вход в систему")
user = input("Введите логин: ")
pass_log = input("Введите пароль: ")

cur.execute("SELECT pass FROM users WHERE login = ?;", (user,))
res_bd = cur.fetchone()

if res_bd is None:
    print("Не верный логин!")
else:
    res_bd = "".join(res_bd)
    if res_bd == hashlib.sha256(user.encode() + pass_log.encode()).hexdigest():
        print("#" * 100)
        print("Пароль в базе {}".format(res_bd))
        print("Введенный Пароль {}".format(hashlib.sha256(user.encode() + pass_log.encode()).hexdigest()))
        print("#" * 100)
        print("Вы вошли в сисему!")
    else:
        print("#" * 100)
        print("Пароль в базе {}".format(res_bd))
        print("Введенный Пароль {}".format(hashlib.sha256(user.encode() + pass_log.encode()).hexdigest()))
        print("#" * 100)
        print("Пароли не совпадают")
