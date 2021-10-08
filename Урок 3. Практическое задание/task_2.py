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

salt = uuid4().hex


def get_hash(password):
    res = hashlib.sha256(salt.encode() + password.encode('utf-8')).hexdigest()
    return res


def check_password():
    password = input('Введите пароль:')
    res = get_hash(password)
    print(f'В базе данных хранится строка: {res}')

    path = '.\\'
    with open(f'{path}pass.txt', 'w', encoding='utf-8') as f:
        f.write(f'{res}')

    password = input('Введите пароль еще раз для проверки:')
    res = get_hash(password)

    with open(f'{path}pass.txt', 'r', encoding='utf-8') as f:
        if res == f.readline():
            print('Вы ввели правильный пароль')
        else:
            print('Пароли не совпадают')


if __name__ == '__main__':
    check_password()
