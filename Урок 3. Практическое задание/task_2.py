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
from uuid import uuid4


def create_hash(pass_hash, salt1, first=True):
    pass_hash = hashlib.sha256(salt1.encode() + pass_hash.encode()).hexdigest()
    if first:
        print(f"Пароль задан, хеш пароля : {pass_hash}")
        write_password(pass_hash)
    else:
        return pass_hash


def write_password(pass_temp2):
    with open('pass_hash.txt', 'w') as f:
        f.write(pass_temp2)
    print("Хеш пароля успешно записан в файл.")


def open_password():
    with open('pass_hash.txt', 'r') as f:
        open_password_temp = f.read()
    return open_password_temp


print("Добро пожаловать в систему юзер.")
password = input("Введите пароль: ")
salt = uuid4().hex
create_hash(password, salt)

print("Введите пароль еще раз для проверки.")
second_password = input("Подтвердите пароль: ")
second_password = create_hash(second_password, salt, first=False)

if open_password() == second_password:
    print("Вы ввели правильный пароль. Добро пожаловать.")
else:
    print("Введённые пароли не совпадают. Пройдите процедуру заново.")
