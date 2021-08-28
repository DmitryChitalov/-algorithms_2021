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


def add_password():
    password = input('Введите пароль: ')
    salt = uuid4().hex
    pass_hash = hashlib.sha3_256(salt.encode() + password.encode())
    print(type(pass_hash))
    pass_hash = pass_hash.hexdigest()
    with open('passwords.txt', 'w', encoding='utf-8') as f:
        f.write(pass_hash)
    res = input('Введите пароль еще раз: ')
    with open('passwords.txt', encoding='utf-8') as f:
        pass_hash = f.readline()
    new_res = hashlib.sha3_256(salt.encode() + res.encode()).hexdigest()

    print(new_res == pass_hash)


add_password()
