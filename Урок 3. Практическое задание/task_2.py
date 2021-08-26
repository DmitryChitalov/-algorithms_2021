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
from hashlib import sha256
from os import path


def pass_hashing(salt, password):
    return sha256(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()


def password_adding():
    user_password = input('Введите пароль:\n')
    pass_hash_add = pass_hashing(login, user_password)
    try:
        with open(path.join(path.dirname(__file__), 'shadow.txt'), 'a+',
                  encoding='utf-8') as fa,\
                open(path.join(path.dirname(__file__), 'shadow.txt'), 'r',
                     encoding='utf-8') as fr:
            if pass_hash_add in fr.read().splitlines():
                print(f'У юзера уже есть пароль с хешем \n{pass_hash_add}')
                return password_adding()
            else:
                fa.write(pass_hash_add + '\n')
                print(f'Пароль с хешем {pass_hash_add} сохранен')
    except IOError:
        print('Что-то пошло не так. Файл не записался.')
    return pass_check()


def pass_check():
    print('проверим пароль')
    password_check = input('Повторите введеный ранее пароль:\n')
    try:
        with open(path.join(path.dirname(__file__), 'shadow.txt'), 'r',
                  encoding='utf-8') as f:
            pass_hash = f.read().splitlines()
    except IOError:
        print('Что-то пошло не так. Ошибка чтения')
    if pass_hashing(login, password_check) in pass_hash:
        print('Как говорится Welcome!')
    else:
        print('Пароль не тот. Попробуй ещё раз')
        return pass_check()


login = input('Введите логин: \n')
password_adding()
