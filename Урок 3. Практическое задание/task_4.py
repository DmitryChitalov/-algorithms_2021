""" Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш
url : хеш-url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и хеш-таблиц. Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации

Задание творческое. Здесь нет жестких требований к выполнению."""

from hashlib import sha256
from uuid import uuid4
import json
import os


class UrlHashStorage:
    """Класс - хранилище url и их хешей (с 'солью')"""

    def __init__(self, storage=dict(), storage_file='url_hashes.json'):
        # хранилище url и хешей - dict(url: хеш url), путь к хранилищу
        self.storage = storage
        self.storage_file = storage_file
        # текущие - url и хеш "соленого" пароля
        self.url = ''
        self.salted_hash = ''

    def is_url_in_storage(self):
        """Проверка наличия url в хранилище"""
        if self.url in self.storage:
            # достаем для имеющегося в хранилище url - его хеш
            self.salted_hash = self.storage[self.url]
            return True
        return False  # если хеша пароля в хранилище нет

    def write_hash(self, salt='reverse'):
        """Расчет хеша (с 'солью'), сохранение в хранилище"""
        # если соль не дана в параметрах, то используем развернутый url
        if salt == 'reverse':
            salt = self.url[::-1]
        # сохраняем хеш для "соленого" url
        self.salted_hash = sha256(salt.encode() + self.url.encode()).hexdigest()
        # сохраняем хеш для url в хранилище
        self.storage[self.url] = self.salted_hash

    # def get_salted_hash(self):
    #     """Вычисление хеша 'соленого' пароля"""
    #     self.salted_hash = sha256(self.salt.encode() +
    #                               self.pwd.encode()).hexdigest()

    def read_storage(self):
        """Чтение хранилища url и хешей из файла"""
        if not os.path.exists(self.storage_file):
            self.storage = dict()
            return
        with open(self.storage_file, 'r', encoding='utf-8') as storage:
            self.storage = json.load(storage)

    def write_storage(self):
        """Запись хранилища url и хешей в файл"""
        with open(self.storage_file, 'w', encoding='utf-8') as storage:
            json.dump(self.storage, storage)


if __name__ == '__main__':
    url_storage = UrlHashStorage()  # Создаем экземпляр хранилища

    # основной цикл скрипта
    while True:
        # получаем url от пользователя
        url_storage.url = input('\nВведите url (0 - для выхода из скрипта): ')
        if url_storage.url == '0':
            print('Выход из программы!')
            exit(0)

        url_storage.read_storage()  # считываем из файла хранилища

        # если url есть в хранилище - печатаем
        if url_storage.is_url_in_storage():
            print(f'url {url_storage.url} есть в хранилище!\nХеш "соленого" '
                  f'url: {url_storage.salted_hash}')

            # Тестовая печать хранилища
            # print('\nХранилище url и их хешей:',
            #       *url_storage.storage.items(), sep='\n')

            continue  # запрашиваем следующий url в осн. цикле скрипта

        # введенного url нет в хранилище
        url_storage.write_hash()  # генерим "соленый" хеш и сохр. в хранилище
        url_storage.write_storage()  # сохраняем хранилище в файл
        print(f'url {url_storage.url} в хранилище нет - сохраняем!\n'
              f'Хеш "соленого" url: {url_storage.salted_hash}')

        # Тестовая печать хранилища
        # print('\nХранилище url и их хешей:',
        #       *url_storage.storage.items(), sep='\n')

        # запрашиваем следующий url в осн. цикле скрипта
