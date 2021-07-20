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


class MainCache:
    def __init__(self):
        self.url_for_cache = {}
        self.salt = 'saltsalt'

    def add_cache(self, url):
        if not self.url_for_cache.get(url):
            self.url_for_cache[url] = hashlib.sha256(self.salt.encode('utf-8') + url.encode('utf-8')).hexdigest()
        else:
            print(f'данная страница "{url}" уже добавлена в кеш ')


cache = MainCache()
cache.add_cache('https://www.yandex.ru')
cache.add_cache('https://www.google.com')
cache.add_cache('https://www.google.com')
print(cache.url_for_cache)