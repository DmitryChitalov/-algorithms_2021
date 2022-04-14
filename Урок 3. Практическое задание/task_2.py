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
from pymongo import MongoClient

CLIENT = MongoClient('127.0.0.1', 27017)
DB = CLIENT['passwords']
PASSWORDS = DB.passwords


def create_hash(passw, salt):
    """
    Генерирует хеш к паролю
    """
    return hashlib.sha256(salt.encode() + passw.encode()).hexdigest()


def add_to_db(passw_hash, salt):
    """
    Добавляет хеш в базу данных
    :param passw_hash: хеш пароля
    :param salt: соль пароля
    """
    PASSWORDS.insert_one({'hash': passw_hash, 'salt': salt})


SALT = uuid4().hex
PASSWORD = input('Введите пароль: ')
PASSWORD_HASH = create_hash(PASSWORD, SALT)
add_to_db(PASSWORD_HASH, SALT)
print(f'В базе данных хранится строка: {PASSWORD_HASH}')
CHECK_PASS = input('Введите пароль еще раз для проверки: ')
CHECK_HASH = create_hash(CHECK_PASS, SALT)

if PASSWORDS.count_documents({'hash': CHECK_HASH}):
    print('Вы ввели правильный пароль')
else:
    print('Вы ввели неверный пароль')
