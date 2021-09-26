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


def check_password():
    salt = 'Я люблю солить хеши <3'
    first_password = hashlib.sha256(salt.encode() + input('Введите пароль: ').encode('utf-8'))
    print(first_password.hexdigest())
    second_password = hashlib.sha256(salt.encode() + input('Введите пароль повторно: ').encode('utf-8'))
    if first_password.hexdigest() == second_password.hexdigest():
        print('Вы ввели правильный пароль.')
    else:
        print('Вы ввели неправильный пароль.')


def check_password_upgrade():
    salt = 'Я люблю солить хеши <3'
    with open('password.txt', 'w', encoding='utf-8') as file:
        phash = hashlib.sha256(salt.encode() + input('Введите пароль: ').encode('utf-8'))
        print(phash.hexdigest())
        file.write(phash.hexdigest())
    second_password = hashlib.sha256(salt.encode() + input('Введите пароль повторно: ').encode('utf-8')).hexdigest()
    with open('password.txt', 'r', encoding='utf-8') as file:
        if file.readline() == second_password:
            print('Вы ввели правильный пароль.')
        else:
            print('Вы ввели неправильный пароль.')


if __name__ == '__main__':
    check_password()
    check_password_upgrade()
