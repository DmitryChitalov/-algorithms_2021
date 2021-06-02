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
from uuid import uuid4


def check_password():
    access = False
    pwd = input('Введите пароль: ')
    with open('salt', 'r', encoding='utf-8') as g:
        salt_list = g.read().splitlines()
    with open('passwords', 'r', encoding='utf-8') as g:
        pwd_list = g.read().splitlines()
    if not pwd_list:
        return add_password(pwd)
    for el in salt_list:
        if hashlib.sha3_256(el.encode() + pwd.encode()).hexdigest() in pwd_list:
            access = True
    if access:
        return 'ACCESS GRANTED'
    if not access:
        return add_password(pwd)


def add_password(pwd):
    salt = uuid4().hex
    user_passwd = hashlib.sha3_256(salt.encode() + pwd.encode()).hexdigest()
    with open('passwords', 'a', encoding='utf-8') as g:
        g.write(user_passwd + '\n')
    with open('salt', 'a', encoding='utf-8') as g:
        g.write(salt + '\n')
    print(f'Add password {pwd} to database')
    check_password()


check_password()
