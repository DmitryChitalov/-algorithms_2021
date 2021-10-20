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

import hashlib

user_login = input("Введите логин ")    # логин будет солью (т.к. он неповторимый)
user_password = input("Введите пароль ")


def hash_password(password, login):
    with open('example.txt', encoding='utf-8') as file_read:    # открываем для чтения
        result = hashlib.sha256(login.encode() + password.encode()).hexdigest()
        if result in file_read.read():
            print("В базе данных уже есть хеш данного пароля: ", result)
        else:
            print("Информация о данном пароле отсутствует")
            user_password_2 = input("Чтобы добавить пароль в БД, ведите его повторно ")
            if password == user_password_2:
                print("Пароли совпадают. Сохранён хеш: ", result)
                with open('example.txt', 'a', encoding='utf-8') as file_write:    # открываем для записи
                    file_write.write(result + '\n')
            else:
                print("Введёный пароли не совпадают")


hash_password(user_password, user_login)
"""можно было и логин в отдельную БД закинуть"""
