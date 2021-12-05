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


def make_hsh(c='Введите пароль: '):
    salt = 'user__1'  # uuid4().hex  # создали соль по логину
    passwd = input(c)
    return hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()  # хеш из пароль+соль в шестнадц ед.


with open("file_2", "w") as fil:
    print(make_hsh(), file=fil)


with open("file_2", "r") as fil:
    for line in fil:
        if make_hsh('Подтвердите пароль: ') in line:
            print("Добро пожаловать!")
        else:
            print("Неверный пароль(")


