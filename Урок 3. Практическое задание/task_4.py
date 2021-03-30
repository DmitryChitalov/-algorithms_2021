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
from uuid import uuid4


class Caching:
    def __init__(self):
        self.__cache = {}
        self.__salt = uuid4().hex

    def get_page(self, url):
        if self.__cache.get(url):
            print(f'Данный адрес: {url} присутствует в кэше')
        else:
            res = sha256(self.__salt.encode() + url.encode()).hexdigest()
            self.__cache[url] = res
            print(self.__cache)


cache_url = Caching()
cache_url.get_page('https://geekbrains.ru/')
cache_url.get_page('https://geekbrains.ru/')
