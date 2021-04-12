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

from storage import Storage

import datetime
from uuid import uuid4
import hashlib
import re

pattern = re.compile(r'^[0-9a-zA-Z]{8,}$')
last_login = datetime.datetime.now()
temp_passwd = '123'

storage = Storage()


def create_passwd():
    salt = uuid4().hex
    while True:
        passwd = input('Введите пароль: ')
        if pattern.match(passwd):
            res = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
            # if res not in storage.res => proceed
            print(res)
            if res == hashlib.sha256(salt.encode() + input('Введите пароль еще раз: ').encode()).hexdigest():
                result = res
                print('ok')
                break
            else:
                print('Пароли не свопадают!')
        else:
            print('Длина пароля не менее 8 символов, только латинские букрвы и цифры')


while True:
    print('Главное меню:')
    answer = input('  1 - Вход\n  2 - Регистрация\n  3 - Выход\nВыберете пункт меню: ')

    if answer == '1':
        passwd = input('Введите пароль: ')
        login = storage.get_account(passwd)
        if login is not None:
            print('Вы успешно авторизовались!')
            print(f'Последнмй вход выполнен: {login}')
            answer = input('  1 - Изменить пароль\n  2 - Удалить учетную запись\n  3 - Вернуться в главное меню'
                           '\nВыберете пункт меню: ')
        else:
            print('Неверный пароль!')

    elif answer == '2':
        create_passwd()

    elif answer == '3':
        print('Выход')
        break

