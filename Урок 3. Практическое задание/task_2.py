"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей.

Самый просто вариант хранения хешей - просто в оперативной памяти (в переменных).

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


def name_password_input():
    user_name = input('Ведите Ваше имя: ')
    password = input('Введите пароль: ')
    return user_name, password


def calculation_hash(password, salt):
    return hashlib.sha256(password.encode(encoding='UTF-8') + salt.encode(encoding='UTF-8')).hexdigest()


def authorization():
    user_name, password = name_password_input()
    salt = uuid4().hex
    return user_name, calculation_hash(password, salt), salt


def authentication():
    user_name, password = name_password_input()
    salt = a[2]
    if a[1] == calculation_hash(password, salt) and user_name == a[0]:
        print(f'Доступ открыт')
    else:
        print(f'Неверное имя пользователя или пароль!')
        authentication()


a = authorization()
print(a)
# authentication()
print(authentication())

'''Очень хотел успеть созранять в файл, думал про *.json, но времени совсем не хватает.'''
