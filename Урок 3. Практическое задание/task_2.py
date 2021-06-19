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
import hashlib
from uuid import uuid4

salt = uuid4().hex
passwd = 'Ilublugysei'


def generate_passwd(passwd):
    res = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
    return res


with open('text.txt', 'w', encoding='UTF-8')as f_objct:
    f_objct.write(generate_passwd(passwd))

check_passwd = input('Введите пароль повторно: ')

with open('text.txt', 'r', encoding='UTF-8')as f_objct:
    hash_passwd = f_objct.readline()
if generate_passwd(passwd) == hash_passwd:
    print('Вы ввели верный пароль')
else:
    print('Пароль не верный: ')