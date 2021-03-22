"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

from hashlib import sha256


class Cash:
    def __init__(self):
        self.bd_url = {}
        self.__salt = 'NaCl'

    def add_url(self, url):
        url_h = sha256(self.__salt.encode() + url.encode()).hexdigest()
        if url_h not in self.bd_url.values():
            self.bd_url[url] = url_h
            print(f'{url} добавлен в кеш')
        else:
            print(f'{url} - уже в кеше')

    def show_cash(self):
        print('Содержимое кеша:')
        for item in self.bd_url:
            print(item)


new_cash = Cash()
new_cash.add_url('https://geekbrains.ru/')
new_cash.add_url('https://yandex.ru/')
new_cash.add_url('https://www.instagram.com/')
new_cash.add_url('https://www.instagram.com/')

new_cash.show_cash()
