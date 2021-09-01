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


def check_user(user):
    with open('db.txt') as f:
        user_list = {line.strip('\n').split(':').pop(0): line.strip('\n').split(':').pop(1) for line in f}
        if user_list.get(user) is None:
            return user
        else:
            user_password = input('Вы уже есть в базе, введите пароль: ')
            if user_list.get(user) == hashlib.sha256(user.encode() + user_password.encode()).hexdigest():
                print('Успешная авторизация')
            else:
                print('Пароль введен неверно')


def add_bd_user(user_login, hash_password):
    with open('db.txt', 'a') as f:
        f.write(f'\n{user_login}:{hash_password}')
        print(f'Операция завершилась успешно. В базе данных хранится строка: {hash_password}')

    if hashlib.sha256(user_login.encode() + input('Введите пароль повторно: ').encode()).hexdigest() == hash_password:
        print('Вы ввели правильный пароль')
    else:
        print('Пароли не совпадают')


def reg_user():
    user_login = check_user(input('Введите логин: '))
    if user_login is not None:
        user_password = input('Введите пароль: ')
        hash_password = hashlib.sha256(user_login.encode() + user_password.encode()).hexdigest()
        add_bd_user(user_login, hash_password)


reg_user()

