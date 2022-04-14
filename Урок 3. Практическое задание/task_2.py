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
import os
import hashlib
from uuid import uuid4


def account_pas(res_1=None, salt=None):
    if res_1== None:
        password_1 = input('Please enter the password: ')
        salt = uuid4().hex
        res_1 = hashlib.sha256(password_1.encode() + salt.encode()).hexdigest()
        print(res_1)
    password_2 = input('Please confirm password: ')
    res_2 = hashlib.sha256(password_2.encode() + salt.encode()).hexdigest()
    print(res_2)
    if res_1 == res_2:
        print('you entered the correct password')
        if os.path.isfile('hash'):
            with open('hash', 'a') as f:
                f.write(res_2 + '\n')
        else:
            with open('hash', 'w') as f:
                f.write(res_2 + '\n')
        return
    else:
        print('you entered the wrong password, please try again')
        return account_pas(res_1, salt)


if __name__ == '__main__':
    account_pas()