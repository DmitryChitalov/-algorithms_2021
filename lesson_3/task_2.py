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
            self.data = set(json.load(file))

    def save(self, password):
        """
        сохранить пароль (будут сохраняться только уникальные пароли)
        """
        self.data.add(password)
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(list(self.data), file)


storage = Storage('storage.json')
SALT = 'my_salt'

user_password = input('Введите пароль: ')
storage.save(hash_password(user_password, SALT))

print(f'В базе данных хранится строка: {hash_password(user_password, SALT)}')

password_retry = input('Введите пароль еще раз для проверки: ')

if hash_password(user_password, SALT) == hash_password(password_retry, SALT):
    print('Вы ввели правильный пароль!')
else:
    print('Вы ввели не правильный пароль!')
