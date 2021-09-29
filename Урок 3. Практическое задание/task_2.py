import hashlib
from uuid import uuid4

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

def password_validator():
    passw = input('Введите пароль: ')
    salt = uuid4().hex
    hash_log = open("hash_log.txt", "w", encoding="utf-8")
    hash_log.write(hashlib.sha256(salt.encode() + passw.encode('utf-8')).hexdigest())
    hash_log.close()
    try_count = 3
    while try_count != 0:
        passw_2 = input('Введите пароль: ')
        res_2 = hashlib.sha256(salt.encode() + passw_2.encode('utf-8')).hexdigest()
        read = open("hash_log.txt", "r", encoding="utf-8")
        if read.readline() == res_2:
            print('Вы ввели правильный пароль!')
            read.close()
            break
        else:
            try_count -= 1
            if try_count == 0:
                print('Пароли не сопадают. Попытки закончились')
            else:
                print(f'Попробуйте еще раз. Осталось {try_count} попыток')


password_validator()
