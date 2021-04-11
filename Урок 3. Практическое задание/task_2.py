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


from hashlib import pbkdf2_hmac
from binascii import hexlify
from json import dump, load


def hash_gen(passwd, username):
    hash_user = pbkdf2_hmac(hash_name='sha256',
                            password=passwd.encode(),
                            salt=username.encode(),
                            iterations=10000)
    return hash_user


def validation():
    username = input('Введите имя пользователя: ')
    user_passwd = input('Введите пароль: ')
    passwd_gen = hexlify(hash_gen(user_passwd, username))

    with open('hash.json', 'w') as file:
        passwd_gen = passwd_gen.decode('utf-8')
        dump(passwd_gen, file)

    with open('hash.json', 'r') as file:
        passwd_gen = load(file)
        print(f'В базе данных хранится строка: {passwd_gen}')
        user_passwd = input('Введите пароль еще раз для проверки: ')
        passwd_gen = bytes(passwd_gen, encoding='utf-8')
        user_passwd = hexlify(hash_gen(user_passwd, username))

        if user_passwd == passwd_gen:
            return 'Вы ввели правильный пароль'
        else:
            return 'Вы ввели неправильный пароль'


result = validation()
print(result)
