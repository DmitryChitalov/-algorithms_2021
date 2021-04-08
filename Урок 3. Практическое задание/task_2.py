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
from peewee import *
import datetime
from uuid import uuid4
from hashlib import pbkdf2_hmac
from binascii import hexlify

db = SqliteDatabase('my_database.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    login = CharField(unique=True)
    password_hash = CharField(unique=True)
    salt = CharField(unique=False)


def password_hash(password,salt):

    obj = pbkdf2_hmac(hash_name='sha256',
                      password=password.encode(),
                      salt=salt.encode(),
                      iterations=100000)
    return hexlify(obj)

db.connect()
salt = uuid4().hex
db.create_tables([User])
login = (input('Введите login: '))
password = (input('Введите пароль: '))


user, created = User.get_or_create(login=login,password_hash=password_hash(password,salt),salt=salt)


print(f'В базе данных хранится строка: {user.password_hash}')

check_password = (input('Введите пароль еще раз для проверки: '))
if password_hash(check_password,user.salt) == user.password_hash:
    print('Вы ввели правильный пароль')
else:
    print('Вы ввели не правильный пароль')
