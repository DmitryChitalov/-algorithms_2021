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


def passwd_verification():

    salt = uuid4().hex
    #print(salt)

    password = input('Введите пароль: ')
    resust_hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    print(resust_hash)

    password_verification = input('Введите пароль еще раз для проверки: ')
    result_verification = hashlib.sha256(salt.encode() + password_verification.encode()).hexdigest()
    print(result_verification)

    if resust_hash == result_verification:
        print('Вы ввели правильный пароль')
        f = open('text.txt', 'w')
        f.write(result_verification + '\n')
        f.close()
    else:
        print('Пароли не совпадают попробуйте еще раз')
        return passwd_verification()

passwd_verification()
