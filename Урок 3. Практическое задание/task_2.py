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
from os import path


def password_hashing(salt, password):
    return hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()


def password_add():
    my_password = input("Введите пароль: ")
    password_hash_add = password_hashing(my_salt, my_password)
    try:
        with open(path.join(path.dirname(__file__), 'password.txt'), 'a+', encoding='utf-8') as fa, open(path.join(path.dirname(__file__), 'password.txt'), 'r', encoding='utf-8') as fr:
            if password_hash_add in fr.read().splitlines():
                print(f"У данного пользователя пароль с хешем \n {password_hash_add} уже есть в базе.\n"
                      f"Попробуйте другой набор символов.")
                return password_add()
            else:
                fa.write(password_hash_add + "\n")
    except IOError:
        print("Файл не записан")

    print(f"Пароль с хешем {password_hash_add} сохранен")
    return password_check()


def password_check():
    print("Проверка пароля.")
    password_again = input("Повторите пароль: ")
    try:
        with open(path.join(path.dirname(__file__), 'password.txt'), 'r', encoding='utf-8') as f:
            password_hash = f.read().splitlines()
    except IOError:
        print("Ошибка чтения.")

    if password_hashing(my_salt, password_again) in password_hash:
        print("Добро пожаловать!.")
    else:
        print("Пароль не совпадает.")
        return password_check()


my_salt = input("Введите логин: ")  # uuid.uuid4().hex
password_add()
