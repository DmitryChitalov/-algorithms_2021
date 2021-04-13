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

import re
from storage import Storage


def get_passwd_hash(_login, _passwd):
    from hashlib import pbkdf2_hmac
    from binascii import hexlify
    passwd_hash = pbkdf2_hmac(hash_name='sha256',
                              password=_passwd.encode(),
                              salt=_login.encode(),
                              iterations=100000)
    return hexlify(passwd_hash)


def update_passwd(upd_login=''):
    pattern = re.compile(r'^[0-9a-zA-Z]{4,}$')

    if upd_login:
        _login = upd_login
    else:
        _login = input('Введите имя пользователя: ')
        if storage.get_login_time(_login) is not None:
            return 'Пользователь с таким логином уже существует.'

    new_passwd = input('Введите пароль: ')

    if pattern.match(new_passwd):
        passwd_hash = get_passwd_hash(_login, new_passwd)
        print(passwd_hash)

        _result = storage.update_account(_login, passwd_hash) if upd_login \
            else storage.create_account(_login, passwd_hash)
        return _result
    else:
        return 'Длина пароля не менее 4 символов, только латинские буквы и цифры'


def authorization(check_login, check_passwd):
    storage_hash = storage.get_passwd_hash(check_login)
    if storage_hash is not None:
        if get_passwd_hash(check_login, check_passwd) == storage_hash[0]:
            return 'ok'


storage = Storage()

while True:
    print('Главное меню:')
    answer = input('  1 - Вход\n  2 - Регистрация\n  3 - Выход\nВыберете пункт меню: ')

    if answer == '1':
        login = input('Введите имя пользователя: ')
        passwd = input('Введите пароль: ')
        if authorization(login, passwd) == 'ok':
            print('Вы успешно авторизовались!')
            print(f'Последнмй вход в систему: {storage.get_login_time(login)[0]}')
            storage.update_login_time(login)
            while True:
                answer = input('  1 - Изменить пароль\n  2 - Удалить учетную запись\n  3 - Вернуться в главное меню'
                               '\nВыберете пункт меню: ')
                if answer == '1':
                    result = update_passwd(login)
                    print(f'Пароль для пользователя {login} успешно обновлен.') if result == 'ok' else print(result)
                elif answer == '2':
                    result = storage.delete_account(login)
                    if result == 'ok':
                        print(f'Учетная запись {login} успешно удалена')
                        break
                    else:
                        print(result)
                        continue
                elif answer == '3':
                    break
        else:
            print('Неверное имя пользователя или пароль!')

    elif answer == '2':
        result = update_passwd()
        print(f'Аккаунт успешно создан.') if result == 'ok' else print(result)

    elif answer == '3':
        print('Выход')
        storage.close()
        break
