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


def get_hash(login, password):
    """Генерация hash"""
    return hashlib.sha256(login.encode() + password.encode()).hexdigest()


FILE_N = 'data.json'

# load data from json
try:
    with open(FILE_N, 'r', encoding='utf-8') as f:
        data = json.load(f)  # сохраняем ответ сервера в файл в человекочитаемой кодировке
except:
    data = {}

login = input('Enter your login: ')
password = input('Enter your password: ')
user_hash = get_hash(login, password)
data.update({login: user_hash})  # we ignore if user exists and has different password. we rewrite password to new.

# save data to json
with open(FILE_N, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)  # сохраняем ответ сервера в файл в человекочитаемой кодировке

print(f'The value {user_hash} saved to database.')
password = input('Enter your password again: ')
user_hash = get_hash(login, password)

# load data from json
try:
    with open(FILE_N, 'r', encoding='utf-8') as f:
        data = json.load(f)  # сохраняем ответ сервера в файл в человекочитаемой кодировке
except:
    pass

if user_hash == data.get(login):
    print('Password is correct.')
else:
    print('Password is incorrect.')
