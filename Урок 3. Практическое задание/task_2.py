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


def passwd(lst_pass):
    salt = uuid4().hex.encode()
    for i in range(len(lst_pass)):
        lst_pass[i] = hashlib.sha256(salt + lst_pass[i].encode()).hexdigest()

    while True:
        with open('Save.txt', 'a', encoding='utf-8') as f:
            f.write(f'{lst_pass[0]};\n')

        with open('Save.txt', 'r') as f:
            value_hash = f.readlines()[-1][:len(f.readlines())-2]
            print(f'В базе данных хранится строка: {value_hash}')
            if value_hash == lst_pass[1]:
                return 'Вы ввели правильный пароль'
            else:
                raise ValueError('Вы ввели неправильный пароль')


print(passwd([input('Введите пароль: '), input('Введите пароль еще раз для проверки: ')]))


# import hashlib
# from uuid import uuid4
#
#
# def passwd():
#     salt = uuid4().hex.encode()
#     while True:
#         hash_passwd = input('Введите пароль: ')
#         hash_obj_in_bd = hashlib.sha256(salt + hash_passwd.encode()).hexdigest()
#         with open('Save.txt', 'a', encoding='utf-8') as f:
#             f.write(f'{hash_obj_in_bd};\n')
#
#         with open('Save.txt', 'r') as f:
#             value_hash = f.readlines()[-1][:len(f.readlines())-2]
#             print(f'В базе данных хранится строка: {value_hash}')
#             check_passwd = input('Введите пароль еще раз для проверки: ')
#             check_passwd_in_bd = hashlib.sha256(salt + check_passwd.encode()).hexdigest()
#             if value_hash == check_passwd_in_bd:
#                 return 'Вы ввели правильный пароль'
#             else:
#                 raise ValueError('Вы ввели неправильный пароль')
#
#
# print(passwd())