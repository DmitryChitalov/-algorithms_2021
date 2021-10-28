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


def create_hash(salt, password):
    return hashlib.sha256(salt.encode() + password.encode('utf-8')).hexdigest()


def create_user_password():
    user_password = input('Придумайте пароль: ')
    salt = 'test_salt'
    new_hash = open("hash_db.txt", "w", encoding="utf-8")
    new_hash.write(create_hash(salt, user_password))
    new_hash.close()


def user_check():
    hash_db = open("hash_db.txt", "r", encoding="utf-8")
    salt = 'test_salt'
    read_hash = hash_db.readline()
    print(read_hash)
    check_hash = ''
    while read_hash != check_hash:
        check_password = input('Введите пароль еще раз для проверки: ')
        check_hash = create_hash(salt, check_password)
        print(check_hash)
        if read_hash == check_hash:
            print('Добро пожаловать!')
        else:
            print('Неверный пароль')


create_user_password()
user_check()
