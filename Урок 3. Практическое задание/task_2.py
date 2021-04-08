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


def reg_func():
    with open('password_data.txt', 'r+') as data:
        login = input('Для регистрации введит новый логин:\n')
        password = input('Введите новый пароль')
        hash_password = hashlib.sha256(login.encode() + password.encode()).hexdigest()
        data.write(hash_password)
        password_check = input('Введите повторно пароль')
        hash_check = hashlib.sha256(login.encode() + password_check.encode()).hexdigest()
        check_data = data.readline()
        if check_data == hash_check:
            print('Добро пожаловать')
            return
    return hash_check, hash_password


print(reg_func())
