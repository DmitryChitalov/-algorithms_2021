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


def hash_pass(password):
    return hashlib.sha256(password.encode() + salt.encode()).hexdigest()

salt = 'username_login_password_salt'
user_password_input = input('Create password: ')
hash_password = hash_pass(user_password_input)   # пароль создан
print(hash_password)
# На этом этапе для пароля, введенного пользователем создан хеш и выведен на экран (это правильный пароль!!!)
# Записываем в файл правильный пароль:
with open('passwords_file.txt', 'w') as password:
    password.write(hash_password)
# Просим пользователя ввести пароль повторно
user_password_input = input('Enter password: ')
hash_password = hash_pass(user_password_input)
# Читаем пароль из файла
with open('passwords_file.txt') as password:
    hash_password_from_file = password.read()

print(hash_password)
# Сравнениваем хеш созданного пароля (32 строка) с введенным сейчас

if hash_password == hash_password_from_file:
    print("Верный пароль")
else:
    print("Неверный пароль")