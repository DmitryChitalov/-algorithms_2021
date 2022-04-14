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
import json
from uuid import uuid4


def auth():
    username = input('Введите логин')
    salt = uuid4().hex
    password = input('Введите пароль')
    psswrd = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    pass_check = input('Введите пароль еще раз')
    check = hashlib.sha256(salt.encode() + pass_check.encode()).hexdigest()
    if psswrd == check:
        print(psswrd)
        try:
            userdata = {username: psswrd}
            with open('data.json') as file:
                data = json.load(file)
                data['users'].append(userdata)
                with open('data.json', 'w') as f:
                    json.dump(data, f, indent=4)
                    f.close()
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                userdata = {'users': [{username: psswrd}]}
                json.dump(userdata, file, indent=4)
        print('Данные добавлены')
    else:
        print('Пароли не совпадают')


auth()

