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


def pass_to_hash():
    password = input('Придумайте пароль: ')
    if len(password) < 6:
        print('Пароль должен содержать больше 6 символов.')
        return pass_to_hash()
    else:
        salt = uuid4().hex
        res = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
        print(f'Хеш введенного пароля - {res}')
        with open('text.txt', 'w') as file:
            file.write(res)
        pass_chek = input('Введите пароль повторно: ')
        res_2 = hashlib.sha256(salt.encode() + pass_chek.encode()).hexdigest()
        with open('text.txt', 'r') as file:
            if file.read() == res_2:
                return f'Пароли совпадают.'
            else:
                print('Пароли не совпадают.')
                return pass_to_hash()


print(pass_to_hash())
