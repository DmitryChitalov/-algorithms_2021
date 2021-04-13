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

import datetime
from uuid import uuid4

import re

from storage import Storage


last_login = datetime.datetime.now()
temp_passwd = '123'

storage = Storage()


def get_passwd_hash(login, passwd):
    from hashlib import pbkdf2_hmac
    from binascii import hexlify
    passwd_hash = pbkdf2_hmac(hash_name='sha256',
                              password=passwd.encode(),
                              salt=login.encode(),
                              iterations=100000)
    return hexlify(passwd_hash)


def create_passwd(new_login):
    pattern = re.compile(r'^[0-9a-zA-Z]{8,}$')

    while True:
        new_passwd = input('Введите пароль: ')
        if pattern.match(new_passwd):
            res = get_passwd_hash(new_login, new_passwd)
            print(res)

            if storage.create_account(new_login, res) == 'ok':
                print(f'Аккаунт для пользователя {new_login} успешно создан.')
                return
            else:
                print('Внутренняя ошибка сервиса - не удалось записать данные.')
                return
        else:
            print('Длина пароля не менее 8 символов, только латинские букрвы и цифры')


def update_passwd(login):
    pattern = re.compile(r'^[0-9a-zA-Z]{8,}$')

    new_passwd = input('Введите пароль: ')
    if pattern.match(new_passwd):
        res = get_passwd_hash(new_login, new_passwd)

        storage.update_account(res)


def authorization(check_login, check_passwd):
    if get_passwd_hash(check_login, check_passwd) == storage.get_passwd_hash(check_login):
        return 'ok'


while True:
    print('Главное меню:')
    answer = input('  1 - Вход\n  2 - Регистрация\n  3 - Выход\nВыберете пункт меню: ')

    if answer == '1':
        login = input('Введите имя пользователя: ')
        passwd = input('Введите пароль: ')
        if authorization(login, passwd) == 'ok':
            print('Вы успешно авторизовались!')
            print(f'Последнмй вход в систему: {storage.get_last_login(login)[0]}')
            storage.update_account(login)
            answer = input('  1 - Изменить пароль\n  2 - Удалить учетную запись\n  3 - Вернуться в главное меню'
                           '\nВыберете пункт меню: ')
            if answer == '1':
                update_passwd(login)
            if answer == '2':
                storage.delete_account(login)
            if answer == '3':
                continue
        else:
            print('Неверное имя пользователя или пароль!')

    elif answer == '2':
        new_login = input('Введите имя пользователя: ')
        if storage.get_last_login(new_login)[0]:
            print('Пользователь с таким логином уже существует.')
            continue
        create_passwd(new_login)

    elif answer == '3':
        print('Выход')
        storage.close()
        break

