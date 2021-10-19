"""Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей.

Самый просто вариант хранения хешей - просто в оперативной памяти (в переменных)

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка:
555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу!
Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД
и сохраняйте хеши там."""

from hashlib import sha256
from uuid import uuid4
import json
import os


class HashStorage:
    """Класс - хранилище хешей паролей (с 'солью')"""

    def __init__(self, storage=dict(), storage_file='hashes.json'):
        # хранилище хешей - dict(хеш_пароля: соль), путь к хранилищу
        self.storage = storage
        self.storage_file = storage_file
        # текущие - пароль, хеш пароля, соль, хеш "соленого" пароля
        self.pwd = ''
        self.hash_pwd = ''
        self.salt = ''
        self.salted_hash = ''

    def is_hash_in_storage(self):
        """Проверка наличия хеша введенного пароля в хранилище"""
        if self.hash_pwd in self.storage:
            # достаем для имеющегося в хранилище хеша пароля соль
            self.salt = self.storage[self.hash_pwd]
            return True
        return False  # если хеша пароля в хранилище нет

    def write_hash(self, salt='auto'):
        """Расчет хеша (с 'солью'), сохранение в хранилище"""
        # если соль не дана в параметрах, то генерим ее
        self.salt = uuid4().hex if salt == 'auto' else salt
        # сохраняем "соль" для пароля в хранилище
        self.storage[self.hash_pwd] = self.salt
        # сохраняем хеш для "соленого" пароля
        self.salted_hash = sha256(self.salt.encode() +
                                  self.pwd.encode()).hexdigest()

    def get_pwd_hash(self):
        """Вычисление хеша пароля (без 'соли')"""
        self.hash_pwd = sha256(self.pwd.encode()).hexdigest()

    def get_salted_hash(self):
        """Вычисление хеша 'соленого' пароля"""
        self.salted_hash = sha256(self.salt.encode() +
                                  self.pwd.encode()).hexdigest()

    def read_storage(self):
        """Чтение хранилища хешей из файла"""
        if not os.path.exists(self.storage_file):
            self.storage = dict()
            return
        with open(self.storage_file, 'r', encoding='utf-8') as storage:
            self.storage = json.load(storage)

    def write_storage(self):
        """Запись хранилища хешей в файл"""
        with open(self.storage_file, 'w', encoding='utf-8') as storage:
            json.dump(self.storage, storage)


if __name__ == '__main__':
    hashes = HashStorage()  # Создаем экземпляр хранилища с пар-ми по-умолчанию

    # основной цикл скрипта
    while True:
        # получаем пароль от пользователя
        hashes.pwd = input('\nВведите пароль (0 - для выхода из скрипта): ')
        if hashes.pwd == '0':
            print('Выход из программы!')
            exit(0)

        hashes.read_storage()  # считываем из файла хранилище хешей

        hashes.get_pwd_hash()  # получаем хеш пароля (без соли)
        if hashes.is_hash_in_storage():  # если хеш пароля есть в хранилище
            hashes.get_salted_hash()  # получаем хеш "соленого" пароля
            print('Пароль есть в хранилище!\nХеш "соленого" пароля:',
                  hashes.salted_hash)

            # Тестовая печать хранилища
            # print('\nХранилище хешей паролей:',
            #       *hashes.storage.items(), sep='\n')

            continue  # запрашиваем следующий пароль в осн. цикле скрипта

        # хеша введенного пароля нет в хранилище
        hashes.write_hash()     # генерим "соль", хеш и сохраняем в хранилище
        hashes.write_storage()  # сохраняем хранилище в файл
        print('Пароля в хранилище нет - сохраняем в хранилище!\n'
              'Хеш "соленого" пароля:', hashes.salted_hash)

        # Тестовая печать хранилища
        # print('\nХранилище хешей паролей:',
        #       *hashes.storage.items(), sep='\n')

        # запрашиваем следующий пароль в осн. цикле скрипта
