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


import uuid
import hashlib
my_salt = uuid.uuid4().hex


def password_hash(salt):
    password = input("Введите пароль: ")
    pswd_hash = hashlib.sha256(password.encode() + salt.encode()).hexdigest()
    with open(r"C:\Users\denet\projects\GeekBrains\python\-algorithms_2021\Урок 3. Практическое задание\password.txt", "w") as f:
        f.write(pswd_hash)
    return password_check(salt)


def password_check(salt):
    password_again = input("Введите пароль ещё раз для проверки: ")
    pswd_hash = hashlib.sha256(password_again.encode() + salt.encode()).hexdigest()
    with open(r"C:\Users\denet\projects\GeekBrains\python\-algorithms_2021\Урок 3. Практическое задание\password.txt", "r") as f:
        if pswd_hash != f.readline():
            print("Пароль не верный!")
            return password_check(salt)
    print("Вы ввели правильный пароль")
    return


password_hash(my_salt)
