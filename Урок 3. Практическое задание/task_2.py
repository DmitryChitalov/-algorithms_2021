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
# sqlite, postgres, db_api, orm


from hashlib import sha256


def hash_password(password):
    return sha256(password.encode('utf-8') + login.encode('utf-8')).hexdigest()


def check_password():
    with open("password.txt") as f:
        true_password = f.read()
    input_password_check = hash_password(input('Введите пароль еще раз: '))

    if true_password == input_password_check:
        result = 'Вы ввели правильный пароль'
    else:
        result = 'Вы ввели неправильный пароль'
    return result


login = input('Введите логин: ').lower()
input_password = hash_password(input('Введите пароль: '))
print(f'Создан хэш пароля: {input_password}')
with open("password.txt", "w") as p:
    p.write(input_password)
print(check_password())
