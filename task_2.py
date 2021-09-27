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


def create_hash(some_str):
    salt = 'Я люблю солить хеши <3'
    return hashlib.sha256(salt.encode() + some_str.encode('utf-8')).hexdigest()


def check_password():
    first_password = create_hash(input('Введите пароль: '))
    print(first_password)
    second_password = create_hash(input('Введите пароль повторно: '))
    if first_password == second_password:
        print('Вы ввели правильный пароль.')
    else:
        print('Вы ввели неправильный пароль.')


def check_password_upgrade():
    salt = 'Я люблю солить хеши <3'
    with open('password.txt', 'w', encoding='utf-8') as file:
        phash = create_hash(input('Введите пароль: '))
        print(phash)
        file.write(phash)
    second_password = create_hash(input('Введите пароль повторно: '))
    with open('password.txt', 'r', encoding='utf-8') as file:
        if file.readline() == second_password:
            print('Вы ввели правильный пароль.')
        else:
            print('Вы ввели неправильный пароль.')


if __name__ == '__main__':
    check_password()
    check_password_upgrade()
