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

from uuid import uuid4
from hashlib import sha256


def check_and_get_urls(url_cache: dict, url: str, salt):
    site_hash = sha256(salt.encode() + url.encode()).hexdigest()
    if not url_cache.get(site_hash) is None:
        print('Сайт уже добавлен')
        pass
    else:
        url_cache[site_hash] = url
        print('Добавлено в кэш')
        return url_cache


class UrlCache:
    def __init__(self):
        self.url_dict = {}
        self.salt = uuid4().hex

    def __str__(self):
        return str(self.url_dict)

    def check_and_add_url(self, new_url):
        check_and_get_urls(self.url_dict, new_url, self.salt)


my_cache = UrlCache()
my_cache.check_and_add_url('http://www.ya.ru')
my_cache.check_and_add_url('http://www.google.com')
my_cache.check_and_add_url('https://github.com')
my_cache.check_and_add_url('https://gb.ru')
my_cache.check_and_add_url('http://www.ya.ru')

print(my_cache)

