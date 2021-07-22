"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
# sqlite, postgres, db_api, orm


from hashlib import sha256
import json

users_dict = {}
with open('users_data.txt', 'w', encoding='utf-8') as f:
   f.write('')


def create_password():
    user_login = input('Введите логин: ')
    user_password = input('Введите пароль: ')
    hash_obj = sha256(user_login.encode() + user_password.encode()).hexdigest()
    users_dict.update({user_login:hash_obj})
    dict_as_string = json.dumps(users_dict)

    with open('users_data.txt', 'r+', encoding='utf-8') as f:
        f.write(dict_as_string)
    with open('users_data.txt', 'r', encoding='utf-8') as f:
        dict_as_str = f.read()
    u_dict = json.loads(dict_as_str)

    print(f'В файле хранится строка: {u_dict[user_login]}')
    check = input('Введите пароль ещё раз: ')
    if hash_obj == sha256(user_login.encode() + check.encode()).hexdigest():
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели не правильный пароль!')


create_password()