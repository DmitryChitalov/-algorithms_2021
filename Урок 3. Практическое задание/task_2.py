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
from hashlib import sha256
import sqlite3


def new_user():
    conn = sqlite3.connect('TaskThird.sqlite')
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE TABLE users (user_login varchar(255) unique not null, password varchar(255) not null)")
    except sqlite3.OperationalError:
        print('Таблица готова')
    else:
        conn.commit()
        print('Таблица создана')
    user_login = input('Введите логин:')
    password = input('Введите пароль: ')
    try:
        password = sha256(user_login.encode() + password.encode()).hexdigest()
        print(password)
        cursor.execute("INSERT INTO users values (?,?)", (user_login, password))
    except sqlite3.IntegrityError:
        cursor.execute("SELECT password FROM users WHERE user_login = :limit", {'limit': user_login})
        if cursor.fetchone()[0] == password:
            print('Пароли совпадают. Вход выполнен успешно')
        else:
            print('Неправильный пароль! Вход запрещен')
    else:
        conn.commit()
        print('Вы успешно зарегестрированы')
        password = sha256(
            user_login.encode() + input('Проверка пароля. Введите ваш пароль снова: ').encode()).hexdigest()
        cursor.execute("SELECT password FROM users WHERE user_login = :limit", {'limit': user_login})
        if cursor.fetchone()[0] == password:
            print('Пароли совпадают.')
        else:
            print('Неправильный пароль')

    conn.close()


new_user()
