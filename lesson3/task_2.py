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
from uuid import uuid4

password_list = ["a48d49b7f6794d3621bd5d2cade26ac31432e4abf8aa07fe04f37e89b3d9fa18", "6658b13cc075d0eff26a3bbb5263483e81a25e63649cd8f3af643d4acec8b835"]




def create_pass(username):
    flag = False
    user_pass = input("Введите пароль: ")
    print(f"Пароль для пользователя {username} - {user_pass}")
    hash_obj_1 = hashlib.sha256(username.encode() + user_pass.encode()).hexdigest()
    print(f"Хеш пароля пользователя {username} - {hash_obj_1}")

    check_user_pass = input("Введите пароль еще раз: ")
    for l in password_list:
        if hashlib.sha256(username.encode() + check_user_pass.encode()).hexdigest() == l:
            print("Correct")
            flag = True
            break

    if flag == False:
        print("Incorrect password")

create_pass('Nikitarius')