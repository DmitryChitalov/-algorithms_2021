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

import hashlib, uuid


salt = uuid.uuid4().hex
passwd = 'password'
res_pass_hash = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
with open('hash_task2.txt', 'w') as f:
    f.write(res_pass_hash)
with open('hash_task2.txt', 'r') as f:
        open_file = f.read()

'''
while True:
    inp_pass = input('Введите пароль: ')
    if open_file == hashlib.sha256(salt.encode() + inp_pass.encode()).hexdigest():
        print('Welcome!')
        break
    else:
        print('Invalid password. Try again.\n')
        continue
'''

def func_inp_pass(open_file):
    inp_pass = input('Введите пароль: ')
    if open_file == hashlib.sha256(salt.encode() + inp_pass.encode()).hexdigest():
        return 'Welcome!'
    else:
        print('Invalid password. Try again.\n')
        return func_inp_pass(open_file)

print(func_inp_pass(open_file))
