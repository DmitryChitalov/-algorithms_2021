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
from uuid import uuid4
from pymongo import MongoClient

login = input('Введите логин:')
passwd = input('Введите пароль:')
salt = uuid4().hex
hash_passwd = hashlib.sha256(passwd.encode()).hexdigest() + salt
json_passwd = {'login': login, 'passwd': hash_passwd, 'salt': salt}
print(f'В БД хранится такой пароль: {json_passwd["passwd"]}')

client = MongoClient('localhost', 27017)
db = client['hash']
hash = db.hash
hash.insert_one(json_passwd)                    # вставка в БД

new_passwd = input('введите пароль еще раз:')
new_hash_passwd = hashlib.sha256(passwd.encode()).hexdigest()

for user in hash.find({'login': f'{login}'}):  # поиск в БД
    if user['passwd'] == (new_hash_passwd + user['salt']):
        print('Вы ввели правильный пароль!')
    else:
        print('Вы ввели пароль не верно(')
