"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
# sqlite, postgres, db_api, orm

from uuid import uuid4
import hashlib


def generate_salt():
    return uuid4().hex


def generate_password_hash(password, salt=generate_salt()):
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest()


password = input('Введите пароль: ')
salt = generate_salt()
password_hash = generate_password_hash(password, salt)

pasword_repeat = input('Введите пароль повторно: ')
pasword_repeat_hash = generate_password_hash(pasword_repeat, salt)

print(f'Пароли {("не ", "")[password_hash == pasword_repeat_hash]}совпадают')

print()
print('Отладочная информация:')
print(f'соль: {salt}')
print(f'хешь первого пароля: {password_hash}')
print(f'хешь повтора пароля: {pasword_repeat_hash}')
