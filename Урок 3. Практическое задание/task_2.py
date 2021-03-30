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


def hash_gen(passwd, nick):
    hash_user = pbkdf2_hmac(hash_name='sha256',
                            password=passwd.encode(),
                            salt=nick.encode(),
                            iterations=10000)
    return hash_user


def validation():
    user_nickname = input('Введите свой никнейм: ')
    user_passwd = input('Введите пароль: ')
    passwd_gen = hexlify(hash_gen(user_passwd, user_nickname))

    with open('hash.json', 'w') as file:
        passwd_gen = passwd_gen.decode('utf-8')  # превращаем байты в строку для json
        dump(passwd_gen, file)

    with open('hash.json', 'r') as file:
        passwd_gen = load(file)
        print(f'В базе данных хранится: {passwd_gen}')
        user_passwd = input('Введите пароль ещё раз чтоб проверить: ')
        passwd_gen = bytes(passwd_gen, encoding='utf-8')
        user_passwd = hexlify(hash_gen(user_passwd, user_nickname))

        if user_passwd == passwd_gen:
            return 'Пароли совпадают.\nВалидация пройдена.'
        else:
            return 'Пароли не совпадают!\nПерепройдите валидацию!'


result = validation()
print(result)
