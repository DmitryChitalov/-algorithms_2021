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


class WebCache:
    def __init__(self):
        self.web_cache_hash = {}
        self.salt = 'any_salt'

    def add_to_cache(self, url):
        self.web_cache_hash[url] = sha256(f'{url}{self.salt}'.encode())

    def check_url(self, url):
        if not self.web_cache_hash.get(url):
            self.add_to_cache(url)
        else:
            print('in web cache')


cache = WebCache()

cache.check_url('https://www.codewars.com/dashboard')
print(cache.web_cache_hash)
cache.check_url('https://www.codewars.com/dashboard')
