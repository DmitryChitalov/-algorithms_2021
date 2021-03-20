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

# т.к. решил использовать sqlite, пришлось немного изменить задание, чтоб соответствовать духу СУБД

from hashlib import pbkdf2_hmac
import sqlite3

sqlite_connection = sqlite3.connect(':memory:')
cursor = sqlite_connection.cursor()
cursor.execute("""DROP TABLE IF EXISTS users;""")
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                    user_id INTEGER primary key autoincrement
                    ,login varchar(10)
                    ,password varchar(50)
                );""")
cursor.execute("""INSERT INTO users (login, password) VALUES
                ('user1', 'pass1')
                ,('user2', 'pass2')
                ,('user3', 'pass3')
                ,('user4', 'pass4')
                ,('user5', 'pass5')
                ,('user6', 'pass1')
                ;""")  # чтоб не мучать пользователя вводом данных, заполним сами
sqlite_connection.commit()


def get_hash(usr, pwd):
    user_hash = pbkdf2_hmac('sha256', pwd.encode(), usr.encode(), 100000)
    return user_hash.hex()


def hashing():
    """
    заменим в таблице users пароли на хэши паролей
    """
    cursor.execute(f"""SELECT login, password FROM users""")
    records = cursor.fetchall()
    print('Список пользователей и паролей и хэшей: ')
    for row in records:
        print(f'login: {row[0]}\t password: {row[1]}\t hash: ', end='')
        cursor.execute(f"""UPDATE users SET password='{get_hash(row[0], row[1])}' WHERE login='{row[0]}';""")
        print(get_hash(row[0], row[1]))
        sqlite_connection.commit()
    # после выполнения цикла пароли необратимо удалены, остались только хэши
hashing()

def login_validation(login=input("Логин: "), wrong_pass_try=3):
    """
    Проверка логина/пароля
    :param login: запрашивается логин
    :param wrong_pass_try: количество попыток неправильного ввода пароля
    """
    cursor.execute(f"""SELECT password FROM users WHERE login = '{login}';""")
    result = cursor.fetchone()
    if result is None:
        print("Учетная запись не найдена")
        login_validation(input("Логин: "))
    elif result[0] == get_hash(login, input('Введите пароль: ')):
        print(f"Добро пожаловать, {login}")
    else:
        if wrong_pass_try >= 1:
            print(f'Неправильный пароль. Осталось попыток: {wrong_pass_try}')
            login_validation(login, wrong_pass_try - 1)
        else:
            print('Попытки закончились')

login_validation()