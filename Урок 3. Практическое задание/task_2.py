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


class Users:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.password_hash = hashlib.sha256(self.login.encode() + self.password.encode()).hexdigest()
        # Users.check_user(self)

    def check_user(self):
        try:
            with open('users.txt') as users_file:
                for line in users_file:
                    user_dict = eval(line)
                    if self.login == user_dict['login']:
                        if self.password_hash == user_dict['password_hash']:
                            return print('Доступ предоставлен')
                        else:
                            return print('Неверный пароль')
                else:
                    return print(f'Пользователь {self.login} не зарегистрирован')
                # Users.add_user_to_file(self)
        except FileNotFoundError:
            with open('users.txt', 'x'):
                print(f'База данных не найдена или не создана')

    def add_user(self):
        data = {'login': self.login, 'password_hash': self.password_hash}
        try:
            with open('users.txt') as users_file:
                for line in users_file:
                    user_dict = eval(line)
                    if self.login == user_dict['login']:
                        return print(f'Пользователь {self.login} уже зарегистрирован')
                else:
                    with open('users.txt', 'a'):
                        users_file.write(f'{data}\n')
                    print(f'Пользователь {self.login} добавлен в базу')
        except FileNotFoundError:
            with open('users.txt', 'x'):
                print(f'База данных не найдена или не создана')


user_1 = Users('11111', '11111')
user_2 = Users('11111', '22222')

user_1.add_user()
user_1.check_user()
user_2.check_user()
