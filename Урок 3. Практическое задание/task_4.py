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

class UrlCash:
    def __init__(self):
        self.__url_dict = {}
        self.__salt = 'Url_salt'

    def add_url(self, url):
        hash_url = sha256(url.encode() + self.__salt.encode()).hexdigest()
        if hash_url in self.__url_dict.values():
            print('Url уже есть в кеше')
        else:
            self.__url_dict[url] = hash_url

    def show_url_cash(self):
        for key, value in self.__url_dict.items():
            print(f'{key}: {value}')


a = UrlCash()
a.add_url('https://finance.yahoo.com/')
a.add_url('https://travel.ru/')
a.add_url('https://travel.ru/')
a.add_url('https://nalog.ru/')
a.add_url('https://mail.ru/')

a.show_url_cash()