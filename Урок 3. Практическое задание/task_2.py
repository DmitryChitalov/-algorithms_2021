"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""
from uuid import uuid4
import hashlib

salt = uuid4().hex

flag = False
while flag is not True:
    passwd = input('Enter your password: ')
    salt = uuid4().hex
    with open('file_for_task2.txt', 'w+', encoding='utf-8') as f:
        f.write(hashlib.sha256(salt.encode() + passwd.encode()).hexdigest())
        passwd_check = input('Enter your password one more time: ')
        check_res = hashlib.sha256(salt.encode() + passwd_check.encode()).hexdigest()
        f.seek(0) # курсор в начало файла
        if check_res == f.read():
            print('Your password is correct')
            flag = True
            break
        else:
            print('The passwords are not equal! Try again')



