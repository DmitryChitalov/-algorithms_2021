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


def entrance():
    salt = 'unique_user_login'
    my_pass_name = input('Введите пароль: ')
    my_pass = hashlib.sha256(salt.encode() + my_pass_name.encode()).hexdigest()
    print(f'В базе данных хранится строка: {my_pass}')
    conn = sqlite3.connect("algorithm_pass.db")
    cursor = conn.cursor()
    cursor.execute("""drop table if exists passwords""")
    cursor.execute("""CREATE TABLE if not exists passwords
                          (
                          id integer NOT NULL PRIMARY KEY autoincrement,
                          passw blob unique 
                          )
                   """)
    try:
        cursor.execute("insert into passwords(passw) values ('{}')".format(my_pass))
        conn.commit()
        cursor.execute("Select passw from passwords")
    except sqlite3.IntegrityError:
        cursor.execute("Select passw from passwords")
    db = cursor.fetchall()
    cursor.close()
    conn.close()
    pass_again = input('Введите пароль еще раз для проверки: ')
    check_pass = hashlib.sha256(salt.encode() + pass_again.encode()).hexdigest()
    for i in db:
        if i[0] == check_pass:
            return f'Вы ввели правильный пароль'
    return f'Вы ввели неправильный пароль'


print(entrance())
