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

salt = uuid4().hex

def check_password():
    user_password = input('Введите пароль: ')
    user_password_sha256 = hashlib.sha256(salt.encode('utf-8') + user_password.encode('utf-8'))
    has_password = user_password_sha256.hexdigest()
    print(has_password)
    check_user_password = input('Введите пароль повторно: ')
    check_user_password_sha256 = hashlib.sha256(salt.encode('utf-8') + check_user_password.encode('utf-8'))
    check_has_password = check_user_password_sha256.hexdigest()
    print(check_has_password)
    if check_has_password == has_password:
        print('Регистрация пройдена')
    else:
        print(f'ОШИБКА! ПАРОЛЬ ВВЕДЕН НЕ ВЕРНО! Надо повторить')
        return check_password()
check_password()

