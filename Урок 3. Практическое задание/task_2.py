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


def registration():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    with open("authentication.txt", "r+", encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            line_login = line[:line.find(":")]
            if login == line_login:
                print('Данный логин уже занят')
                return False
        f.write(f'{login}:{hashlib.sha3_256(login.encode() + password.encode()).hexdigest()}\n')
        print(f'Созданный хеш: {hashlib.sha3_256(login.encode() + password.encode()).hexdigest()}')
        return True


def authentication():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    with open("authentication.txt", "r", encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            line_login = line[:line.find(":")]
            hash_line = line[line.find(":") + 1:-1]
            if login == line_login:
                if hash_line == hashlib.sha3_256(login.encode() + password.encode()).hexdigest():
                    print("Добро пожаловать")
                    return True
        print("Введенные пара логин и пароль неверные")
        return False


print("Регистрация нового аккаунта:")
registration()
print("Аутентификация:")
authentication()
