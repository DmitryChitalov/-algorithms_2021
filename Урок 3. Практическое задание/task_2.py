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

import hashlib
import json
import uuid


def get_hash(login, password):
    return hashlib.sha256(login.encode('utf-8') + password.encode('utf-8')).hexdigest()


class Storage:

    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, 'r', encoding='utf-8') as file:
            self.data = json.load(file)

    def save(self, login, password, salt):
        self.data[login] = {'password': password, 'salt': salt}
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.data, file)

    def check_user(self, login, password):
        if login not in self.data:
            return False

        user_salt = self.data[login]['salt']
        user_password = self.data[login]['password']

        return get_hash(password, user_salt) == user_password


storage = Storage('storage.json')
salt = str(uuid.uuid4())

print('registration')
user_reg_login = input('login: ')
user_reg_password = input('password: ')
storage.save(user_reg_login, get_hash(user_reg_password, salt), salt)

print(f'The database stores the string: {get_hash(user_reg_password, salt)}')

print('authorization')
user_auth_login = input('login: ')
user_auth_password = input('password: ')

if storage.check_user(user_auth_login, user_reg_password):
    print('logged in')
else:
    print('authorization error')
