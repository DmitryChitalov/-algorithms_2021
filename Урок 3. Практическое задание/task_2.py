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

from hashlib import sha256
import csv

def create_account():
    log = input("Введите логин:")
    password = input("Введите пароль:")
    h_pass = sha256(log.encode() + password.encode()).hexdigest()
    with open("passwords.csv", "a") as f:
        f.write(f"{log},{h_pass}\n")
    return h_pass


def check_password(login):
    checked_pass = input("Введите ваш пароль:")
    with open('passwords.csv', 'r') as p:
        d = csv.reader(p)
        for row in d:
            if row[0] == login:
                if row[1] == sha256(login.encode() + checked_pass.encode()).hexdigest():
                    return "Верный пароль"
                else:
                    return "Введен неверный пароль!"

print(create_account())
print(check_password('123'))


