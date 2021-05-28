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
from uuid import  uuid4

password = input("Введите пароль: ")
salt = uuid4().hex
res_1 = hashlib.sha256(salt.encode() + password.encode()).hexdigest()

print(res_1)
text_file = open('password.txt', 'w', encoding='utf-8')
text_file.write(res_1)
text_file.close()

password = input("Введите пароль еще раз: ")
res_2 = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
text_file = open('password.txt', 'r')
res_1 = text_file.read()
if res_1 == res_2:
    print('Вы ввели правильный пароль.')
else:
    print('Неверный пароль.')

text_file.close()