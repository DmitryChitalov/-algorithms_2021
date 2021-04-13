"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

from uuid import uuid4
import hashlib

def generate_salt():
    return uuid4().hex


def generate_hash(data, salt=generate_salt()):
    return hashlib.sha256(salt.encode() + data.encode()).hexdigest()


class UrlCacher:
    def __init__(self):
        self.cache = {}
        self.salt = generate_salt()

    def get(self, url):
        hash = generate_hash(url, self.salt)
        return self.cache[hash]

    def add(self, url):
        hash = generate_hash(url, self.salt)
        if not hash in self.cache:
            self.cache[hash] = url
        return hash

    def print(self):
        print(self.cache)


URL_CACHER = UrlCacher()

URL_CACHER.add('http://google.com')
URL_CACHER.add('http://ya.ru')
URL_CACHER.add('http://ya.ru')

URL_CACHER.print()
