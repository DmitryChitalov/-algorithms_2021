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

SALT = "saltsaltsaltsalt"
user_passw = input("Введите пароль: ")

hash_object = hashlib.sha256(user_passw.encode() + SALT.encode())
print(hash_object.hexdigest())

with open("passw.txt", "w") as password:
    password.write(hash_object.hexdigest())

user_passw = input("Введите пароль: ")

hash_passw_entered = hashlib.sha256(user_passw.encode() + SALT.encode())
with open("passw.txt") as password:
    hash_passw_from_file = password.read()

if hash_passw_entered.hexdigest() == hash_passw_from_file:
    print("Введен верный пароль")
else:
    print("Введен неверный пароль!")
