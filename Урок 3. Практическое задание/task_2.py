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
import sqlite3
from uuid import uuid4

con = sqlite3.connect('passwd_hash.db')
cur = con.cursor()
# cur.execute('''DROP TABLE IF EXISTS passwds''')
cur.execute('''CREATE TABLE IF NOT EXISTS passwds
                (id INTEGER PRIMARY KEY,
                hash varchar(250) NOT NULL,
                salt varchar(250) NOT NULL)''')


def getting_data():
    """This function receives new password, generates unique salt and makes starting hash"""
    salt = uuid4().hex
    passwd = input("Введите пароль: ")
    hashvalue = hashlib.sha256((passwd + salt).encode())
    my_data = (hashvalue.hexdigest(), salt)
    return my_data


def sq_ins(my_hash_set):
    """This function makes an insert of hash and unique salt for it into database"""
    cur.execute('INSERT INTO passwds(hash, salt) VALUES (?,?)', my_hash_set)
    con.commit()


def sq_sel(my_only_hash):
    """This function makes a data select from database finding of specified hash"""
    cur.execute("SELECT hash, salt FROM passwds WHERE hash = ?", my_only_hash)
    one_result = cur.fetchone()
    return one_result


def confirmation(stored_salt, start_hash):
    """This function compares hashes both of passwordes"""
    passwd_confirm = input("Введите пароль еще раз для проверки: ")
    confirm_hash = hashlib.sha256((passwd_confirm + stored_salt).encode())
    if start_hash == confirm_hash.hexdigest():
        print("Вы ввели правильный пароль")
    else:
        print("Пароль введен неверно, попробуйте еще раз")
        confirmation(stored_salt, start_hash)


def passwd_authent():
    """This is the main authentication function that calls auxiliary functions"""
    start_data = getting_data()
    sq_ins(start_data)
    print(f"В базе данных хранится строка: {start_data[0]}")
    stored_data = sq_sel((start_data[0],))
    confirmation(stored_data[1], start_data[0])


passwd_authent()
