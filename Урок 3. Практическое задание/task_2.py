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
from hashlib import sha256
from os import path


# Считаем хеш из логина и пароля
def get_hash(log, pas):
    return sha256(pas.encode('utf-8') + log.encode('utf-8')).hexdigest()


# записываем хеш в файл
def write_data(log, pas):
    pass_hash = get_hash(log, pas)
    try:
        with open(path.join(path.dirname(__file__), 'hash.txt'), 'w', encoding='utf-8') as file:
            file.write(pass_hash)
    except IOError:
        print("Ошибка записи файла.")

    print(f'В базе данных хранится строка:\n{pass_hash}')


# получаем хеш из файла и сравниваем с хешем из повторно введённого пароля
def read_data(log, pas):
    try:
        with open(path.join(path.dirname(__file__), 'hash.txt'), 'r', encoding='utf-8') as file:
            pass_hash = file.read()
    except IOError:
        print("Ошибка чтения файла.")

    if get_hash(log, pas) == pass_hash:
        print('Вы ввели правильный пароль.')
    else:
        print('Вы ввели неправильный пароль.')


if __name__ == '__main__':

    login = input('Введите логин:\n')
    password = input('Введите пароль:\n')
    write_data(login, password)

    repeat_password = input('Ввелите пароль ещё раз:\n')
    read_data(login, repeat_password)
