"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
import hashlib
from time import sleep
from uuid import uuid4


class UrlCache:
    cache_dict = {}
    salt = uuid4().hex

    def __init__(self, url):
        self.url = url
        UrlCache.add_to_cache(self)

    def add_to_cache(self):
        if UrlCache.cache_dict.get(self.url):
            return print(f"{self.url} is already in the cache")
        else:
            print(f"Add {self.url} to cache")
            sleep(1)  # Для наглядности
            url_hash = hashlib.sha256(UrlCache.salt.encode() + self.url.encode()).hexdigest()
            UrlCache.cache_dict[self.url] = url_hash

    @staticmethod
    def get_cache():
        return UrlCache.cache_dict


UrlCache('https://www.ya.ru')
UrlCache('https://www.ya.ru')
UrlCache('https://www.google.com')
for key, value in UrlCache.get_cache().items():
    print(f"{key}: {value}")
