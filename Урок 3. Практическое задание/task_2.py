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


def password_hash(password, salt):
    return hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()


def registration():
    print("Регистрация")
    login = input("Введите логин - ")
    password = input("Введите пароль - ")
    if password == input("Подтвердите пароль - "):
        print("Успешно! ")
        pass_hash = password_hash(password, login)
        with open("password.txt", "a", encoding="utf-8") as passwords_file:
            passwords_file.write(login + ' ' + pass_hash)
    else:
        print("Пароли не совпадают")
        return registration()


def log_in():
    print("Вход")
    login = input("Введите логин - ")
    password = input("Введите пароль - ")
    with open("password.txt", "r", encoding="utf-8") as file:
        for line in file:
            if line.split()[0] == login:
                if password_hash(password, login) == line.split()[1]:
                    print("Вход выполнен")
                    return
                else:
                    return print("Пароль неверный")
        return print("Такого пользователя не существует")


# registration()
log_in()
