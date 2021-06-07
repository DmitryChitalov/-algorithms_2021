"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

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

conn = sqlite3.connect('sqlite_task2.db')
cur = conn.cursor()
"""Создадим тестовую БД"""
cur.execute(""" CREATE TABLE IF NOT EXISTS users (
    id INT(11) PRIMARY KEY,
    user VARCHAR(50),
    password VARCHAR(256)
    ); """)

""" Это три польз-ля по умолчанию. Пароли я предварительно захешировал и поместил
готовые хеши в звпрос
max - 123, 
srj - 456, 
egor - 789
Для новых польз-ей хеширование происходит в ф-и reg_user() """

cur.execute("""INSERT INTO users (user, password) VALUES
    ('max', '74ba7e49e963635164033eb502fb4d47ad7b0ee662a7e0370a0ea0c66659ef88'),
    ('srj', 'ee61e92bd55cd39d85310371195f532109fdb359d418993bb5435a92793e484a'),
    ('egor', '52842e8d1f4f8b64a888141c5eba075f6ee3237e47c9040687c03a3fe46de80f');
    """)
conn.commit()

def check_user(login):
    """ Ф-я проверят сущ-ет ли пользователь в БД,
    возвращает True  или False взависимости от рещультата """
    cur.execute(f"""SELECT user, password FROM users WHERE user = '{login}';""")
    sample = cur.fetchone()
    conn.commit()
    if sample:
        return sample[1]    # Если поль-ль существует, то возвр-ет его хеш-пароль
    else:
        return False

def reg_user(n):
    """ Ф-я для регистрации новых пользователй, вызывается, если польз-ль
    не сущ-ет в БД
    n - Кол-во попыток """
    login = input('Введите новый логин: ')
    password = input('Придумайте пароль: ')
    password_hash = hashlib.sha256(login.encode() + password.encode()).hexdigest()
    conn = sqlite3.connect('sqlite_task2.db')
    cur = conn.cursor()
    sql = f"""INSERT INTO users (user, password) VALUES ('{login}', '{password_hash}');"""
    if cur.execute(sql):
        conn.commit()
        print(f'Регистрация пройдена успешно. Авторизуйтесь!')
        return auth_user(input('Введите логин: '), input('Введите пароль: '))
    else:
        print(f'Попробуйте снова')
        return reg_user(n - 1)

def auth_user(login, password):
    """ Ф-я для авторизация польз-ей. В качестве "соли" добавил логин пользователя"""
    salt = login
    sample = check_user(login)  # Выполняем проверку польз-ля
    if sample:
        hash_password = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
        if hash_password == sample:
            return f'Вы ввели правильный пароль'
        else:
            return f'Пароль не верный'
    else:
        print(f'Нет пользователя с таким именем.\nПройдите регистрацию')
        return reg_user(n=3)

print(auth_user(input('Введите логин: '), input('Введите пароль: ')))


