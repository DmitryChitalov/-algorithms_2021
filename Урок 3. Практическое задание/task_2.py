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
import json
import hashlib

def get_hash(str, salt):
    return hashlib.sha256(str.encode('utf-8') + salt.encode('utf-8')).hexdigest()

def check_login (login, users_dict):
    if login in users_dict:
        return users_dict[login]
    else:
        return None

def add_to_dict(login, pass_hash, users_dict):
    users_dict.update({login: pass_hash})
    return users_dict

def add_to_file(user_dict):
    with open('task_2.json', 'w') as f:
        json.dump(user_dict, f)
    return True


def load_from_file():
    try:
        with open('task_2.json', 'r') as f:
            users_dict = json.load(f)
            return users_dict
    except FileNotFoundError:
        print("Файла с данными еще не существует")
        users_dict  = dict()
        return users_dict

users_dict = load_from_file()
login = input("Введите логин: ")
pass_hash = check_login(login, users_dict)
if pass_hash is None:
    password = input("Это новый пользователь. Введите пароль: ")
    pass_hash = get_hash(password, login)
    repeat_pass = input("Введите пароль повтоно: ")
    repeat_pass_hash = get_hash(repeat_pass, login)
    if pass_hash == repeat_pass_hash:
        print('Пароли совпали. Добавляем запись в базу')
        print('Хеш пароля в базе:', pass_hash)
        users_dict = add_to_dict(login, pass_hash, users_dict)

    else:
        print('Пароли не совпали. Пользователь не может быть добавлен в базу. Попробуйте еще раз')
        print('Хеш пароля в базе:', pass_hash)
        print('Хеш введенного пароля:', repeat_pass_hash)
else:
    repeat_pass = input("Логин уже существует. Введите пароль: ")

    repeat_pass_hash = get_hash(repeat_pass, login)
    if pass_hash == repeat_pass_hash:
        print('Пароли совпали. Вы молодец!')
        print('Хеш пароля в базе:', pass_hash)
    else:
        print('Пароли не совпали. Вспоминайте пароль и попробуйте еще раз')
        print('Хеш пароля в базе:', pass_hash)
        print('Хеш введенного пароля:', repeat_pass_hash)

add_to_file(users_dict)