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
from uuid import uuid4
import hashlib

def input_password():
    while True:
        try:
            password = input('Введите пароль: ')
            if len(password) < 3:
                raise Exception
            for elem in password:
                elem = ord(elem.lower())
                if elem not in range(48, 58) and elem not in range(97, 123):
                    raise Exception
            return password
        except:
            print('Пароль должен состоять как минимум из 3х латинских буквы и/или цифр!')

def get_hash(salt, password):
    hash_val = hashlib.sha256(password.encode() + salt.encode()).hexdigest()
    print(f'хеш значение: {hash_val}')
    return hash_val


password = input_password()

salt = uuid4().hex
print(f'соль: {salt}')
hash_val = get_hash(salt, password)

with open('hash.txt', 'w') as f:
    f.write(hash_val)

print('Выполним проверку.')
password = input_password()
hash_val = get_hash(salt, password)

with open('hash.txt') as f:
    if hash_val == f.readline():
        print('Все верно!')
    else:
        print('Вы ввели неверный пароль!')