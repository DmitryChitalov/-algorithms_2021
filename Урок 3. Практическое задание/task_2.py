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
import pymysql


connection = pymysql.connect(
            host='localhost',
            user='root',
            password='*******',
            db='library',
            charset='utf8mb4'
            )
cursor = connection.cursor()


def select_name():
    sql = """ 
        SELECT firstname FROM users
        """
    cursor.execute(sql)
    val = cursor.fetchall()
    return val


def select_password(firstname):
    sql = """
        SELECT password_hash FROM users
        WHERE firstname = ('%s')
        """ % firstname
    cursor.execute(sql)
    val = cursor.fetchall()
    return val[0][0]


def insert(first_name, last_name, e_mail, password):
    sql = """
        INSERT INTO users (firstname, lastname, email, password_hash)
        VALUES ('%s', '%s', '%s', '%s') 
        """ % (first_name, last_name, e_mail, password)
    try:
        cursor.execute(sql)
        connection.commit()
        print('Congratulations! You are registered')
    except pymysql.err.Error:
        connection.rollback()
        print('Fail')


def set_password(user):
    password = input('Enter password\n').encode()
    salt = user.encode()
    dk = hashlib.sha256(salt + password).hexdigest()
    print(dk)
    return dk


def authorisation(user, count=1):               # Шаг 1 запускаем авторизацию
    if user in [i[0] for i in select_name()]:   # если пользователь в базе
        val = set_password(user)                # запрашиваем пароль чере функцию set_password
        if val == select_password(user) and count > 0:
            print('Enter password again')
            count -= 1
            return authorisation(user, count)
        elif val == select_password(user) and count == 0:
            print('You entered the correct password')
            return True
        elif val != select_password(user) and count > 0:
            count -= 1
            print(f'Wrong password, try again\n count attempts: {count}')
            return authorisation(user, count)
        elif val != select_password(user) and count == 0:
            print('Wrong password! Access denied')
            return False
        else:
            print('Wrong password! Access denied')
            return False
    return registration()  # Иначе идем к регистрации


def registration():
    print('User not found please register')
    firstname = input('Enter firstname\n')
    lastname = input('Enter lastname\n')
    email = input('Enter e-mail\n')
    password = set_password(firstname)
    return insert(firstname, lastname, email, password)


client = input('Enter name:\n')
authorisation(client)

# Enter name:
# d
# User not found please register
# Enter firstname
# Davy
# Enter lastname
# Jones
# Enter e-mail
# DavyJones@gmail.com
# Enter password
# 123
# 60847385ea2a037c2503b5e6302a59ece2baf7035b11175058520c172c59402e
# Congratulations! You are registered
#
# Process finished with exit code 0
#
# Enter name:
# Davy
# Enter password
# 123
# 60847385ea2a037c2503b5e6302a59ece2baf7035b11175058520c172c59402e
# Enter password again
# Enter password
# 123
# 60847385ea2a037c2503b5e6302a59ece2baf7035b11175058520c172c59402e
# You entered the correct password
#
# Process finished with exit code 0
