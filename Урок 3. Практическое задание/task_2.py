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


import hashlib
import pickle
import pymysql
from uuid import uuid4
from pymysql.cursors import DictCursor


def conect_db():
    con = pymysql.connect(
        host='localhost',
        user='root',
        password='ASV1870asv1977',
        db='lesson_3_db',
        charset='utf8mb4',
        cursorclass=DictCursor
    )
    return con


def insert_pass(salt, hash_pass):
    con = conect_db()
    with con.cursor() as cur:
        ins = "INSERT INTO users (salt, password_hash) VALUES ( %s, %s)"
        val = [(salt, hash_pass)]
        cur.executemany(ins, val)
        con.commit()
    print(f'Хешь пароля: {hash_pass}\n'
          f'записан в базу данных')


def select_pass():
    con = conect_db()
    with con.cursor() as cur:
        cur.execute("SELECT salt, password_hash FROM users")
        rows = cur.fetchall()
    return rows


def clear_table():
    con = conect_db()
    with con.cursor() as cur:
        cur.execute("TRUNCATE TABLE users")


def gen_salt():
    salt = uuid4().hex
    return salt


def gen_pass(pass_user, salt):
    hash_pass = hashlib.sha256(salt.encode() + pass_user.encode()).hexdigest()
    return hash_pass


# ------------------------ main ---------------------------
while True:
    print('=' * 50)
    act = input(f'Для выхода введите         => 0\n'
                f'Запись пароля в СУБД MySQL => 1\n'
                f'Запись пароля в файл       => 2\n'
                f'Очистить базу данных       => 999\n'
                f'Введите значение: ')
    if act == '0':
        print('-' * 50)
        print('Выход')
        break

    elif act == '1':
        clear_table()
        print('-' * 50)
        passwd = input(f'Введите пароль: ')
        salt = gen_salt()
        hash_passwd = gen_pass(passwd, salt)
        insert_pass(salt, hash_passwd)

        passwd = input(f'Введите пароль для проверки: ')
        old_db = select_pass()
        salt = old_db[0]['salt']
        old_pass = old_db[0]['password_hash']
        new_pass = gen_pass(passwd, salt)
        if new_pass == old_pass:
            print('Введен ПРАВИЛЬНЫЙ пароль!!!')
        else:
            print('Пароль НЕВЕРНЫЙ. Попробуйте еще раз!!!')
        continue

    elif act == '2':
        print('-' * 50)
        passwd = input(f'Введите пароль: ')
        salt = gen_salt()
        hash_passwd = gen_pass(passwd, salt)
        work_dict = {'salt': salt, 'password_hash': hash_passwd}
        with open('users.dat', 'wb') as f:
            pickle.dump(work_dict, f)
            print(f'Хешь пароля: {hash_passwd}\n'
                  f'записан в файл')

        passwd = input(f'Введите пароль для проверки: ')
        with open('users.dat', 'rb') as f:
            old_db = pickle.load(f)

        salt = old_db['salt']
        old_pass = old_db['password_hash']
        new_pass = gen_pass(passwd, salt)
        if new_pass == old_pass:
            print('Введен ПРАВИЛЬНЫЙ пароль!!!')
        else:
            print('Пароль НЕВЕРНЫЙ. Попробуйте еще раз!!!')
        continue

    elif act == '999':
        clear_table()
        print('База данных очищена. Данные отсутствуют')
        continue
    else:
        print('Действие не выбрано!!!')
        continue

































