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
import os
import binascii
import sqlite3


def password_hash_gen(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("utf-8")
    pass_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 1000)
    pass_hash = binascii.hexlify(pass_hash)
    return (salt + pass_hash).decode("utf-8")


def password_verify(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pass_hash = hashlib.pbkdf2_hmac("sha256", provided_password.encode("utf-8"), salt.encode("utf-8"), 1000)
    pass_hash = binascii.hexlify(pass_hash).decode("utf-8")
    return stored_password == pass_hash


def registration(user_login, user_password):
    with sqlite3.connect('test_database.db') as db:
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INT, name TEXT, password TEXT)""")
        cursor.execute(f"""INSERT INTO users (id, name, password) 
                    VALUES (1, '{user_login}', '{password_hash_gen(user_password)}')""")
        db.commit()
    return f"Registration success"


def authorization(user_login, user_password):
    with sqlite3.connect('test_database.db') as db:
        cursor = db.cursor()
        cursor.execute(f"""SELECT password FROM users WHERE name='{user_login}'""")
        base_password = cursor.fetchall()
        check_password = password_verify(base_password[0][0], user_password)
        if check_password:
            return f"Welcome"
        else:
            return "Access denied"


if __name__ == '__main__':
    print("Registration")
    print(registration('test', 'test'))
    print('Authorization...')
    print(authorization('test', 'test'))
    print(authorization('test', 'wrongpass'))
