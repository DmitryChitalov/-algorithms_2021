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

my_salt = str(hash('my_salt')).encode('utf-8')
data_name = 'pass.data'
new_pass = input('Введите пароль >')
obj = pbkdf2_hmac('sha256', new_pass.encode('utf-8'), my_salt, 100000)
try:
    with open('data_name', 'wb') as file_w:
        file_w.write(hexlify(obj))
    sec_pass = input('Подтвердите пароль >')
    obj = pbkdf2_hmac('sha256', sec_pass.encode('utf-8'), my_salt, 100000)
    with open('data_name', 'rb+') as file_r:
        check_pass = file_r.read()
        if check_pass == hexlify(obj):
            print('Пароли совпадают')
        else:
            print('Пароли не совпадают')
except IOError:
    print('Проблемы работы с файлами')
