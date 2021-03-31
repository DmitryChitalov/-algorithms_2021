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
from hashlib import pbkdf2_hmac
from binascii import hexlify

def registration():
    print("Регистрация")
    username = input("Введите логин: ")

    with open('credentials.txt', 'r') as f:
        for line in f:
            lst_line = line.split()
            if lst_line[0] == username:
                print("Вы уже зарегистрированы")
                exit()
    f.close()

    passwd = input("Введите пароль: ")
    salt = username.encode("utf-8")
    pass_hash = hexlify(pbkdf2_hmac('sha256', passwd.encode("utf-8"), salt, 1000))

    with open('credentials.txt', 'a') as f:
        f.write(username + ' ' + pass_hash.decode("utf-8") + '\n')
    f.close()
    print("Пароль сохранен в виде хэша ", pass_hash.decode("utf-8"))

def auth():
    print("Авторизация")
    username = input("Введите логин: ")
    passwd = input("Введите пароль: ")
    salt = username.encode("utf-8")
    pass_hash = hexlify(pbkdf2_hmac('sha256', passwd.encode("utf-8"), salt, 1000))

    with open('credentials.txt', 'r') as f:
        user_exists = 0
        for line in f:
            lst_line = line.split()
            if lst_line[0] == username:
                user_exists = 1
                if lst_line[1] == pass_hash.decode("utf-8"):
                    print("Аутентификация прошла успешно")
                    print("Пароль хранится в виде хэша ", lst_line[1])
                    print("Введенный пароль имеет хэш ", pass_hash.decode("utf-8"))

                else:
                    print("Пароли не совпадают")
                    print("Пароль хранится в виде хэша ", lst_line[1])
                    print("Введенный пароль имеет хэш ", pass_hash.decode("utf-8"))
    f.close()

    if user_exists == 0:
        print("Пользователя с таким логином не существует")

exit_programm = 0

while exit_programm == 0:
    action = int(input("Если желаете зарегистироваться введите 0. Если желаете войти в систему введите 1. Для выхода введите 2: "))
    if action == 0:
        registration()
    elif action == 1:
        auth()
    elif action == 2:
        exit_programm = 1