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


def my_program():
    password = input("Please enter the password: ")
    salt = 'max_security'
    pwd_hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    file = open('pwd_file.txt', 'w')
    file.write(pwd_hash)
    file.close()
    auth_pwd = input('Enter your password again, please: ')
    auth_pwd_hash = hashlib.sha256(salt.encode() + auth_pwd.encode()).hexdigest()
    file = open('pwd_file.txt', 'r')
    if auth_pwd_hash == file.read():
        print("Correct password.")
    else:
        print("Incorrect password.")
    file.close()


my_program()
