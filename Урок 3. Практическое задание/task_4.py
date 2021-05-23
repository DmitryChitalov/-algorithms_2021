"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

import hashlib


class UrlCache:
    def __init__(self):
        self.url_cache = {}
        self.salt = 'salt'

    def cache_add(self, url):
        if not self.url_cache.get(url):
            self.url_cache[url] = hashlib.sha256(self.salt.encode('utf-8') + url.encode('utf-8')).hexdigest()
        else:
            print('Страница уже в кеше')


cache = UrlCache()
cache.cache_add('https://www.google.com')
cache.cache_add('https://www.google.com')
cache.cache_add('https://www.yandex.ru')
print(cache.url_cache)
