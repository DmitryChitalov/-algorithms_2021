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


def hash_pwd(pwd):
    pwd_hash = hashlib.sha256(pwd.encode() + 's7gd7g8sf9773nfsdfj4jsdfkklkdcvnllaiu3i4234'.encode()).hexdigest()
    return pwd_hash


file = open('pwdbase.txt', 'w')
pwd = input('Введите пароль: ')
pwd_hash = hash_pwd(pwd)
print('Хеш:', pwd_hash)
file.write(pwd_hash)
file.close()

file = open('pwdbase.txt', 'r')
rpt_pwd = input('Введите пароль повторно: ')
rpt_hash = hash_pwd(rpt_pwd)
pwd_hash = file.read()
file.close()
print('Хеш:', rpt_hash)
if rpt_hash == pwd_hash:
    print('Пароль верный!')
else:
    print('Пароль неверный!')

