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


# Подумал, что здесь можно модифицировать задание из первого урока
class HashClass:
    def __init__(self):
        self.hash_list = []
        self.active_user_list = []

    def log_in(self):
        to_continue = None
        while to_continue != 'n':
            login = input('Введите логин: ')
            passwd = input('Введите пароль: ')
            check_hash = sha256(login.encode() + passwd.encode()).hexdigest()
            if check_hash in self.hash_list:
                self.active_user_list.append(login)
                print('Вы вошли в сеть')
                break
            else:
                print('Вы ввели неверный логин или пароль!\nЖелаете попробовать еще раз?')
                to_continue = input('Да - введите любой символ,\nНет - введите "n": ')

    def register(self):
        while True:
            login = input('Введите логин: ')
            passwd = input('Введите пароль: ')
            check_hash = sha256(login.encode() + passwd.encode()).hexdigest()
            if check_hash not in self.hash_list:
                self.hash_list.append(check_hash)
                print('Вы успешно зарегистрировались')
                break
            print('Введеный логин уже занят!\nПопробуйте еще раз')

    def log_out(self):
        login = input('Введите логин, чтобы выйти из сети: ')
        if login in self.active_user_list:
            self.active_user_list.remove(login)
            print('Вы вышли из сети')
        else:
            print('Вы не в сети!')


network = HashClass()

while True:
    user_choice = input('Введите номер функции\n1) Войти в аккаунт\n2) Зарегистрироваться\n'
                        '3) Выйти из аккаунта\n4) Выйти из программы:')
    while user_choice not in ['1', '2', '3', '4']:
        user_choice = input('Нужно ввести номер из списка:\n1) Войти в аккаунт\n2) Зарегистрироваться\n'
                            '3) Выйти из аккаунта:\n4) Выйти из программы: ')
    if user_choice == '1':
        network.log_in()
    elif user_choice == '2':
        network.register()
    elif user_choice == '3':
        network.log_out()
    else:
        break
