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

class Cache:
    def __init__(self):
        self.cache = dict()
        self.salt = uuid4().hex

    def add_to_cache(self, url):
        if self.is_contains(url) != None:
            print('Такой url уже хранится в кеше!')
            return

        hash_val = hashlib.sha256(url.encode() + self.salt.encode()).hexdigest()
        self.cache[hash_val] = url

    def is_contains(self, url):
        hash_val = hashlib.sha256(url.encode() + self.salt.encode()).hexdigest()
        return self.cache.get(hash_val)


cache = Cache()
print(f'кеш пуст: {cache.cache}')

cache.add_to_cache('www.py.org')
cache.add_to_cache('www.ne_znau.ru')
print(f'текущие данные в кеше: {cache.cache}')

cache.add_to_cache('www.py.org')