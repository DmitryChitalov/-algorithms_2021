import hashlib
from binascii import hexlify
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


def make_hash(login, n_pass):
    hash_password = hashlib.pbkdf2_hmac(hash_name='sha256',
                                        salt=login.encode(),
                                        iterations=100,
                                        password=n_pass.encode())
    hash_password = hexlify(hash_password)
    return hash_password


def password():
    your_password = input("Введите пароль:")
    your_login = input("Введите логин:")
    your_hash = make_hash(your_login, your_password)
    print(f'В базе данных хранится строка: {your_hash}')
    your_password = input("Введите пароль:")
    your_new_hash = make_hash(your_login, your_password)
    if your_hash == your_new_hash:
        return "Вы ввели правильный пароль"
    else:
        return "Вы ввели неправильный пароль"


print(password())
