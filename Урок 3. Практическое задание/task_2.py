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
from os import urandom as _urandom

def random_number():
    random = int(int.from_bytes(_urandom(7), 'big')) >> 5
    list = [n for n in range(0, 1000000)]
    return list[random % 100000]

password = input('Введите пароль: ')
salt = str(random_number())
hash_obj = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
print(hash_obj)
with open('password_hash.txt', 'w') as f:
    data = f.write(hash_obj)
while True:
    password_1 = input('Введите пароль повторно: ')
    hash_obj_1 = hashlib.sha256(salt.encode() + password_1.encode()).hexdigest()
    with open('password_hash.txt') as f:
        data = f.read()
    if data == hash_obj_1:
        print('Пароли совпадают')
        break
    else:
        print('Введеные пароли не совпадают')


