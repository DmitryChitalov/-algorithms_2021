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
import hashlib


def hash_password(pswd_str):
    return hashlib.sha256(pswd_str.encode('utf-8') + salt.encode('utf-8')).hexdigest()


def check_password():
    with open("password.txt") as f:
        first_password = f.read()
    second_password = hash_password(input('Введите пароль еще раз: '))

    if first_password == second_password:
        res = 'Вы ввели верный пароль'
    else:
        res = 'Пароль неверный'
    return res


salt = 'NaCl'

f_inp_password = hash_password(input('Введите пароль: '))

with open("password.txt", "w") as password:
    password.write(f_inp_password)

print(check_password())
