"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""

import uuid
import hashlib
import redis


# openserver redis
r = redis.StrictRedis(
    host='127.0.0.1',
    port=6379,
    password=''
)


def hash_password(password):
    return hashlib.sha256(password.encode()+salt.encode()).hexdigest()


def check_password(login):
    old_pass = hash_password(input('Введите пароль еще раз для проверки: '))
    password = r.get(login).decode('UTF-8')
    if password == old_pass:
        return 'Вы ввели верный пароль'
    else:
        return 'Пароль неверный'


salt = uuid.uuid4().hex
login = input('Введите логин: ')
new_pass = input('Введите пароль: ')
hashed_password = hash_password(new_pass)
print(hashed_password)
r.set(login, hashed_password)
print(check_password(login))


