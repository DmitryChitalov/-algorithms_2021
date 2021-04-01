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

import hashlib
import pickle


def hash_password(password, salt):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)


def check_password(hash_pass, user_password, salt):
    hash_user_pass = hashlib.pbkdf2_hmac('sha256', user_password.encode(), salt.encode(), 100000)
    return hash_pass == hash_user_pass.hex()


with open('data.txt', 'rb') as f:
    data = pickle.load(f)

login = input('Введите имя: ')
new_pass = input('Введите пароль: ')
hashed_password = hash_password(new_pass, login).hex()

double_pass = input('Введите пароль еще раз для проверки: ')
if check_password(hashed_password, double_pass, login):
    print('Пароли совпадают')
    data[login] = hashed_password         # Сохранение кеша пароля в словаре
    print(f'Строка для сохранения в базе данных: {hashed_password}')
    with open('data.txt', 'wb') as f:  # Сохранение словаря в файле
        pickle.dump(data, f)
else:
    print('Пароли не совпадают')