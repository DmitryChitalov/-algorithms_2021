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
import uuid
import json


def get_hash(base):
    return hashlib.sha256(base.encode('utf-8') + MY_ID.encode('utf-8')).hexdigest()


def in_out_hash(file_name, mode, file_dict=None):
    with open(file_name, mode, encoding='utf-8') as log_file:
        if mode == 'w':
            json.dump(file_dict, log_file)
            return True
        elif mode == 'r':
            return json.load(log_file)
        else:
            return False


my_dict = {}
MY_ID = str(uuid.uuid1())

in_str = input('Введите пароль: ')
my_dict[in_str] = get_hash(in_str)
in_out_hash('data.txt', 'w', my_dict)
print('Пароль сохранен в базу')

new_str = input('Введите пароль еще раз для проверки: ')
my_dict = in_out_hash('data.txt', 'r')
my_hash = my_dict[new_str]
print(f'В базе данных хранится строка: {my_hash}')
if get_hash(new_str) == my_hash:
    print('Вы ввели правильный пароль')
