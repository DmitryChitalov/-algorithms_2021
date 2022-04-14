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
from hashlib import pbkdf2_hmac
from binascii import hexlify


def hash_pass(pass_1):
    result = pbkdf2_hmac(hash_name='sha256', password=pass_1.encode(), salt=b'salt_salt_salt', iterations=100000)
    print('This string is stored in the database: ', hexlify(result))
    return hexlify(result)


def authentication(data_1, data_2):
    if data_1 == data_2:
        return print('Everything is ok, password is confirmed')
    else:
        return print("Password isn't confirmed, please retry")


authentication(hash_pass(input('Enter your password here: ')), hash_pass(input('Enter your password again to confirm it: ')))
