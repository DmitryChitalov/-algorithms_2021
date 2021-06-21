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


import json
from hashlib import sha256


class Authentication:
    def __init__(self):
        self.data = {}
        self.total_list = self.get_data_json()
        self.ind_total_list = 0    # индекс элемента, в котором был найден user_name

    def get_data_json(self):
        """Возвращает данные из json файла"""
        with open('passwords.json') as f_json:
            return json.load(f_json)

    def check_user_name(self, user_name):
        """Проверка на наличие имени пользователя в файле, так же присваивает переменной self.ind_total_list
        индекс словаря, в котором было найдено имя"""
        for i, user_info in enumerate(self.total_list):
            if user_info.get(user_name):
                self.ind_total_list = i
                return True

    def match(self, text):
        """Проверка на наличие кириллицы в вводимом тексте"""
        alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        return alphabet.isdisjoint(text.lower())  # возвращает True, если в множестве не найдены элементы объекта

    def check_in(self):
        """Алгоритм для регистрации пользователей с проверкой на корректность вводимых символов и на повторение
        имени пользователя"""
        print('Добро пожаловать на нашу форму регистрации. Следуйте инструкциям')
        while True:
            try:
                user_name = input('Придумайте имя пользователя. Имя не должно содержать кириллицы').lower()
                password = input('Придумайте пароль. Пароль не должен содержать кириллицы')
                if not self.match(user_name) or not self.match(password):
                    raise ValueError
                elif self.check_user_name(user_name):
                    raise RuntimeError
                else:
                    break
            except ValueError:
                print('Имя пользователя и/или пароль не должны содержать кириллицу')
            except RuntimeError:
                print('Данное имя пользователя уже используется')
        password = self.get_hash(user_name, password)
        self.data[user_name] = password
        self.total_list.append(self.data)
        with open('passwords.json', 'w') as f_json:
            json.dump(self.total_list, f_json)
        return 'Регистрация прошла успешно'

    def log_in(self):
        """Алгоритм для авторизации пользователей с проверкой на наличие имени пользователя в базе"""
        print('Добро пожаловать на наш ресурс.')
        user_name = input('Укажите имя пользователя').lower()
        password = input('Укажите пароль')
        password = self.get_hash(user_name, password)
        if self.check_user_name(user_name):
            if password == self.total_list[self.ind_total_list][user_name]:
                return 'Авторизация прошла успешно!'
            else:
                return 'Вы ввели неверный пароль'
        return 'Пользователь с таким именем не существует.'

    def get_hash(self, user_name, password):
        """Алгоритм для хеширования "соленого" пароля"""
        hash_obj = sha256(user_name.encode() + password.encode()).hexdigest()
        return hash_obj


with open('passwords.json') as f_json:
    print(json.load(f_json))

a = Authentication()
print(a.check_in())
print(a.log_in())


