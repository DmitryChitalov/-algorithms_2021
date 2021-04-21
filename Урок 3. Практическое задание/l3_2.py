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

from hashlib import sha256 as sha256
from uuid import uuid4 as uuid4

password = input('Enter your password please: ')
salt = uuid4().hex
res = sha256(salt.encode() + password.encode()).hexdigest()
print(res)

with open('pass_db.txt', 'w') as password_in_db:
    password_in_db.write(res)

password = input('Enter your password again: ')
res = sha256(salt.encode() + password.encode()).hexdigest()

with open('pass_db.txt', 'r') as password_in_db:
    res_2 = password_in_db.read()

print('Password is correct!') if res == res_2 else print('Password is incorrect!')
