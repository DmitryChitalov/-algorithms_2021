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


class HashClass(filename):
    def __init__(self):
        self.filename = filename
    
    def write_in_file(data_line):
        with open(self.filename, 'a') as f:
            f.write('data_line')

    def read_from_file():
        with open(self.filename, 'r') as f:
            linelist = []
            for i in f:
            linelist.append(i)
        return linelist

    def get_hash(self):
        login = input('Введите логин: ')
        passwd = input('Введите пароль: ')
        hash_obj = sha256(login.encode() + passwd.encode()).hexdigest()
        return login, hash_obj


    def register(self):

        login, registration_hash = self.get_hash()

        dataline = "" + login + ":" + registration_hash

        linelist = read_from_file()

        for i in linelist:
            if dataline == i:
                print('Вы уже были зарегистрированы')
                registered = True
        if not registered:
            write_in_file(dataline)
            print('Вы зарегистрированы')


    def log_in(self):

        login, check_hash = self.get_hash()
        dataline = "" + login + ":" + check_hash

        linelist = read_from_file()
        logged = False

        for i in linelist:
            if dataline == i:
            logged = True

        if logged:
            print('Вы вошли!')
        else:
            print("Вы ввели неверный пароль или еще не регистрировались")

