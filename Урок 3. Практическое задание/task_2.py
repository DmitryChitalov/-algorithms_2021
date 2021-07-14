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
from hashlib import sha256


def write_data(login, pass_hash):
    # Просто пишем даннные.
    conn = sqlite3.connect("passwd.tmp")
    cursor = conn.cursor()
    cursor.execute("""create table if not exists logins (login text unique, hash_data text)""")
    cursor.execute("""insert or ignore into logins (login, hash_data) VALUES (?, ?)""", [login, pass_hash])
    cursor.execute("""update or ignore logins set hash_data = ? where login = ?""", [pass_hash, login])
    conn.commit()

def read_data(login):
    conn = sqlite3.connect("passwd.tmp")
    cursor = conn.cursor()
    cursor.execute("""select hash_data from logins where login = ?""", [login])
    for row in cursor:
        yield [row[el] for el in range(0, len(row))]


def login():
    user = input('Введите логин: ')
    passw = input('Введите пароль: ')
    write_data(user, sha256(user.encode() + passw.encode()).hexdigest())
    return user


usr = login()
hash = list(*read_data(usr))[0]
print(f'Записана хеш строка: {hash}')
new_p = input('Повторите пароль: ')
if sha256(usr.encode() + new_p.encode()).hexdigest() == hash:
    print('Вы ввели правильный пароль!')
else:
    print('Пароли не совпадают!')
