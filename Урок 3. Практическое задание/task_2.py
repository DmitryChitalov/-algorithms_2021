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
import json
from uuid import uuid4
import hashlib
import os
from mysql.connector import connect, Error


# Вариант хранения в переменных.
def init_user_p(users_dict):
    salt = uuid4().hex
    name = input('Введите имя: ')
    password = hashlib.sha3_256(salt.encode() + input('Введите пароль: ').encode()).hexdigest()
    print(f'Полученный хеш: {password}')
    users_dict[name] = (password, salt)


def check_user_p(user_dict):
    try:
        name = input('Введите имя для проверки: ')
        password = hashlib.sha3_256(user_dict.get(name)[1].encode() + input('Введите пароль: ').encode()).hexdigest()
        if password == user_dict.get(name)[0]:
            print('Пароль совпадает!')
        else:
            print('Пароль неверный!')
    except TypeError:
        print('Проверте вводимые данные!')


print('Вариант хранения в переменных.')
users = {}
init_user_p(users)
init_user_p(users)
check_user_p(users)
print()


# Вариант с хранением в файле.
def init_user_f():
    salt = uuid4().hex
    name = input('Введите имя: ')
    password = hashlib.sha3_256(salt.encode() + input('Введите пароль: ').encode()).hexdigest()
    print(f'Полученный хеш: {password}')
    user_dict = {name: [password, salt]}
    if os.path.isfile('users.json') and os.path.getsize('users.json'):
        with open('users.json', 'r') as f:
            tmp_dict = json.load(f)
            user_dict.update(tmp_dict)

    with open('users.json', 'w') as f:
        json.dump(user_dict, f)


def check_user_f():
    name = input('Введите имя для проверки: ')
    password = input('Введите пароль: ')

    with open('users.json', 'r') as f:
        user_dict = json.load(f)
    if name not in user_dict:
        print('Данного пользователя нет в базе.')
    elif hashlib.sha3_256(user_dict[name][1].encode() + password.encode()).hexdigest() == user_dict[name][0]:
        print('Пароль верный.')
    else:
        print('Пароль не верный.')


print('Вариант с хранением в файле.')
init_user_f()
init_user_f()
check_user_f()
print()

# Вариант хранения в БД.
print('Вариант хранения в БД.')
try:
    with connect(
        host="localhost",
        user=input('Введите имя пользоватля БД: '),
        password=input('Введите пароль: '),
    ) as connection:
        def input_user_bd():
            name = input('Введите имя пользователя: ')
            password = input('Введите пароль: ')
            salt = uuid4().hex
            print(f'Полученный хеш: {hashlib.sha3_256(salt.encode() + password.encode()).hexdigest()}')
            cursor.execute(f'INSERT INTO user (name, salt, hash_pass)'
                           f'VALUES'
                           f'   ("{name}", "{salt}", "{hashlib.sha3_256(salt.encode() + password.encode()).hexdigest()}")')
            connection.commit()


        def check_user_bd():
            name = input('Введите имя для проверки пароля пользователя: ')
            password = input('Введите пароль для проверки: ')
            cursor.execute(f'SELECT '
                           f'   name, '
                           f'   salt, '
                           f'   hash_pass '
                           f'FROM '
                           f'   user '
                           f'WHERE '
                           f'   name = "{name}"')
            res = cursor.fetchall()
            if len(res) == 0:
                print('Пользователь не найден.')
            elif hashlib.sha3_256(res[0][1] + password.encode()).hexdigest() == bytes.decode(res[0][2]):
                print('Пароль верный')
            else:
                print('Пароль не верный')


        with connection.cursor() as cursor:
            cursor.execute('DROP DATABASE IF EXISTS storage_pass')
            cursor.execute('CREATE DATABASE storage_pass')
            cursor.execute('USE storage_pass')

            cursor.execute('DROP TABLE IF EXISTS user')
            cursor.execute('CREATE TABLE user('
                           '    id SERIAL,'
                           '    name VARCHAR(255),'
                           '    salt TINYBLOB,'
                           '    hash_pass TINYBLOB)')

            input_user_bd()
            input_user_bd()
            check_user_bd()

except Error as e:
    print(e)


"""
Для вариантов хранения в переменных и фаиле не реализованно хранение паролей для пользователей с одинаковыми именами.
"""
