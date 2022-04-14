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

salt = uuid4().hex


def pass_hash():
    passw = input('Введите пароль: ')
    gen_hash = hashlib.sha256(salt.encode() + passw.encode('utf-8')).hexdigest()
    return passw, gen_hash


def pass_save():
    hash_to_save = pass_hash()
    hash_log = open("hash_log.txt", "w", encoding="utf-8")
    hash_log.write(hash_to_save[1])
    hash_log.close()


def password_validator():
    pass_save()
    try_count = 3
    while try_count != 0:
        passw, hash_check = pass_hash()
        read = open("hash_log.txt", "r", encoding="utf-8")
        if read.readline() == hash_check:
            print('Вы ввели правильный пароль!')
            read.close()
            break
        else:
            try_count -= 1
            if try_count == 0:
                print('Пароли не сопадают. Попытки закончились')
            else:
                print(f'Попробуйте еще раз. Осталось {try_count} попыток')


password_validator()
