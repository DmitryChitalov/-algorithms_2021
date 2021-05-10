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

import hashlib
import json
from uuid import uuid4

def hash_func(user_name, password, hash_dict={}):
    phrase = 'some salt text'
    salt = user_name + phrase
    hash_obj = hashlib.sha256(salt.encode('UTF-8') + password.encode('UTF-8'))
    user_pass_hash = hash_obj.hexdigest()
    print(f'Созданный хеш - {user_pass_hash}')
    hash_dict[user_name] = user_pass_hash

    with open('passwd.json', 'w', encoding='UTF-8') as file:
        json.dump(hash_dict, file)

def authorize(user_name, password):
    phrase = 'some salt text'
    salt = user_name + phrase
    hash_obj = hashlib.sha256(salt.encode('UTF-8') + password.encode('UTF-8'))
    user_input_pass_hash = hash_obj.hexdigest()
    print(user_input_pass_hash)

    with open('passwd.json', 'r', encoding='UTF-8') as file:
        hash_dict = json.load(file)
        user_pass_hash = hash_dict.get(user_name)

    if user_input_pass_hash == user_pass_hash:
        return True


if __name__ == '__main__':
    print('Создание учетной записи')
    user_name = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')
    hash_func(user_name, password)
    print('======================================')
    print('Авторизация')
    user_name = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')
    if authorize(user_name, password):
        print('Пароль верный! Вход разрешен.')
    else:
        print('Не верный пароль!')



