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

from uuid import uuid4
import hashlib

salt = uuid4().hex

password = input('Введите пароль: \n>>>')


def hash_pswd(salt, password):
    slt_pswd = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    print(f'Созданный хеш: {slt_pswd}')
    return slt_pswd


hash_val = hash_pswd(salt, password)

with open('password.txt', 'w') as f:
    f.write(hash_val)

print('Выполним проверку.')
password = input('Введите пароль ещё раз для проверки: \n>>>')
hash_val = hash_pswd(salt, password)

with open('password.txt') as f:
    if hash_val == f.readline():
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели неверный пароль!')
