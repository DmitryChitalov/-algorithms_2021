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


def func():
    f = open("my_file.txt", "w+")
    if res == res_2:
        print('Данные верны и внесены в отдельный файл')
        return (f.write(str(res)))
    else:
        return "Ошибка ввода данных!"


login_salt = input('Создайте логин ')
password = input('Созадйте пароль ')
hash_obj = hashlib.sha256(b'password')

res = hashlib.sha256(login_salt.encode() + password.encode()).hexdigest()
print(f'Cоль - {login_salt} + хэш {password}')
print(res)

login_salt_2 = input('Введите логин ')
password_2 = input('Введите пароль ')
hash_obj_2 = hashlib.sha256(b'password')
res_2 = hashlib.sha256(login_salt_2.encode() + password_2.encode()).hexdigest()
print(f'Cоль_2 - {login_salt_2} + хэш_2 {password_2}')
print(res_2)

print(func())
