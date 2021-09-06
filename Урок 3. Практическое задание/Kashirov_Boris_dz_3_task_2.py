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

import hashlib
from uuid import uuid4

SALT = uuid4().hex


def write_pass_hash(w_pass):
    with open('password_hash.txt', 'w') as f:
        f.write(w_pass)


def read_pass_hash(s_pass):
    with open('password_hash.txt', 'r') as f:
        r_pass = f.read()
    print('2.Контрольная сумма: ', s_pass)
    if s_pass == r_pass:
        print('Контрольные суммы совпадают')
    else:
        print('Введенные данные отличаются')


def create_pass_hash(f_pass, flag):
    pass_hash = hashlib.sha256(SALT.encode() + f_pass.encode()).hexdigest()
    if flag:
        write_pass_hash(pass_hash)
        print('Пароль: ', f_pass, '\n1.Контрольная сумма: ', pass_hash)
    else:
        return pass_hash


password = str(input('Введите пароль: '))
create_pass_hash(password, True)

password = str(input('Введите пароль: '))
read_pass_hash(create_pass_hash(password, False))
