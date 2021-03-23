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

#  С субд пока не разобрался, на работе завал. Сделал, как умею, с файлом. Коряво, но работает.
import hashlib


class User:

    def __init__(self):
        self.username = input('Input name')
        self.password = input('Input password')
        self.password_hash = hashlib.sha256(self.username.encode() + self.password.encode()).hexdigest()
        User.check_user(self)

    def check_user(self):
        try:
            with open("users.txt") as f_obj:
                for line in f_obj:
                    user_dict = eval(line)
                    if self.username == user_dict['username']:
                        if self.password_hash == user_dict['password']:
                            return print("Access Granted")
                        else:
                            return print("Bad password")
                User.add_user_to_file(self)
        except FileNotFoundError:
            with open("users.txt", "x"):
                pass
            User.add_user_to_file(self)

    def add_user_to_file(self):
        print(f"Add {self.username} user to database")
        data = {'username': self.username, 'password': self.password_hash}
        with open("users.txt", "a") as f_obj:
            f_obj.write(f'{data}\n')
        User.__init__(self)


User()
