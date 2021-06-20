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


from uuid import uuid4
import hashlib


salt = uuid4().hex


def hash_func():
    user_password_1 = input('Введите пароль: ')
    result_1 = hashlib.sha256(salt.encode() + user_password_1.encode()).hexdigest()
    print(f'хеш пароля - {result_1}')
    user_password_2 = input('Введите пароль еще раз: ')
    result_2 = hashlib.sha256(salt.encode() + user_password_2.encode()).hexdigest()
    print(f'хеш пароля - {result_2}')
    if result_1 == result_2:
        print("Пароль совпадает")
        with open('users_data.txt', 'a') as f:
            f.write(f'{result_2}')
    else:
        print('Пароли не совпали.')
        hash_func()


def read_hash():
    with open('users_data.txt', 'r') as f:
        print(f.readlines())


hash_func()
read_hash()
