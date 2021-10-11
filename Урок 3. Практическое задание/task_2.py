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

conn = sqlite3.connect('password.sqlite')

cursor = conn.cursor()


def create_tbl(name):
    create_table = f'CREATE TABLE {name} (id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, login VARCHAR(50) UNIQUE, password VARCHAR(255));'
    try:
        cursor.execute(create_table)
    except sqlite3.OperationalError:
        print('Таблица создана ранее.')
    else:
        conn.commit()
        print('Таблица добавлена')


def drop_tbl(name):
    drop_table = f'DROP TABLE {name};'
    try:
        cursor.execute(drop_table)
    except sqlite3.OperationalError:
        print('Таблицы не существует.')
    else:
        conn.commit()
        print('Таблица удалена')


def insert_in_tbl(name, login, password):
    insert = f'INSERT INTO {name} (login, password) VALUES ("{login}", "{password}");'
    try:
        cursor.execute(insert)
    except sqlite3.OperationalError as err:
        print('Попытка вставки не удалась.', err)
    else:
        conn.commit()
        print('Данные сохранены в БД')


def select_fr_tbl(name):
    select = f'SELECT password FROM {name} LIMIT 1;'
    try:
        cursor.execute(select)
    except sqlite3.OperationalError as err:
        print('Попытка извлечения данных не удалась.', err)
    else:
        result = cursor.fetchone()
        return result[0]


drop_tbl('users')
create_tbl('users')

login = input('Введите логин: ')
password = input('Введите пароль: ')
res_1 = hashlib.sha256(login.encode() + password.encode()).hexdigest()
print(res_1)
insert_in_tbl('users', login, res_1)
repeat_pass = input('Введите пароль повторно: ')
res_2 = hashlib.sha256(login.encode() + repeat_pass.encode()).hexdigest()
print(res_2)
check_password = select_fr_tbl('users')
if check_password == res_2:
    print('Доступ разрешён.')
else:
    print('Не верный пароль.')

conn.close()
