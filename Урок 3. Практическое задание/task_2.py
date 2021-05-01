from hashlib import sha256
from uuid import uuid4
import ast

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


def hashing_password(password, salt=uuid4().hex):
    try:
        sha256(password.encode() + salt.encode()).hexdigest()
    except AttributeError:
        return f'Password must be alphanumeric!'
    return sha256(password.encode() + salt.encode()).hexdigest(), salt


def write_in_file():
    with open(file='users_data.txt', encoding='UTF-8', mode='a') as file:
        user_login = input('Enter your login: ')
        user_password = input('Enter your password: ')
        data = (user_login, hashing_password(user_password))
        file.write(str(data) + '\n')
        print(f'\nDone!')


def validation_check():
    with open(file='users_data.txt', encoding='UTF-8', mode='r') as file:
        user_login = input('Enter your login: ')
        user_password = input('Enter your password: ')
        data = file.readlines()
        for line in data:
            if user_login in line:
                if hashing_password(user_password, ast.literal_eval(line)[1][1]) == ast.literal_eval(line)[1]:
                    return f'Correct password'
                else:
                    return f'Invalid password'
        return f'User not exists.'


print(f'{hashing_password(12345)}\n'
      f'{hashing_password("1q2w3e4")}\n')

write_in_file()
print(f'{validation_check()}\n')
