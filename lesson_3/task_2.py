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


def hash_password(password, salt):
    """
    хешируем пароль с солью
    """
    return hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()


class Storage:
    """
    хранитель паролей
    """

    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, 'r', encoding='utf-8') as file:
            self.data = json.load(file)

    def save(self, login, password, salt):
        """
        сохранить пароль (будут сохраняться только уникальные пароли)
        """
        self.data[login] = {'password': password, 'salt': salt}
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.data, file)

    def check_user(self, login, password):
        if login not in self.data:
            return False

        user_password = self.data[login]['password']
        user_salt = self.data[login]['salt']

        return hash_password(password, user_salt) == user_password


storage = Storage('storage.json')
salt = str(uuid.uuid4())

print('Регистрация')
user_login = input('Введите логин: ')
user_password = input('Введите пароль: ')
storage.save(user_login, hash_password(user_password, salt), salt)

print(f'В базе данных хранится строка: {hash_password(user_password, salt)}')

print('Авторизация')
user_retry_login = input('Введите логин: ')
user_retry_password = input('Введите пароль: ')

if storage.check_user(user_retry_login, user_password):
    print('Вы успешно авторизованы!')
else:
    print('Произошла ошибка авторизации!')
