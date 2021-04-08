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

from hashlib import sha256
from uuid import uuid4


#  Проверяем наличие значения в файле
def f_check_in_file(value):
    try:
        with open('pwd.hidden', 'r') as f:
            for line in f.readlines():
                if line == value + '\n':
                    return True
    except:
        return False
    return False


#  Записываем значение в файл, если его там еще нет
def f_save_to_file(value):
    if not f_check_in_file(value):
        with open('pwd.hidden', 'a') as f:
            f.write(value + '\n')


#  Надо обеспечить неизменность значения соли между попытками ввода пароля.
#  Соль сохраняем в файле эмулируя необходимость ее сохранения где-то для учетной записи.

salt = uuid4().hex

pwd = input('Введите пароль: ')
saved_to_db = salt + ':' + sha256(salt.encode() + pwd.encode('utf-8')).hexdigest()
print(f'Создали хеш-значение для пароля: {saved_to_db}')
f_save_to_file(saved_to_db)

pwd = input('Введите пароль еще раз для проверки: ')
value_to_check = salt + ':' + sha256(salt.encode() + pwd.encode('utf-8')).hexdigest()
print(f'Проверочное хеш-значение для пароля: {value_to_check}')
if f_check_in_file(value_to_check):
    print('Вы ввели правильный пароль!')
else:
    print('Введенный пароль не совпадает!')
