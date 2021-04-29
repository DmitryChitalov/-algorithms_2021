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

from hashlib import sha256


class CacheUrl:

    def __init__(self):
        self.cache = set()

    def url_add(self, url):
        cache_len = len(self.cache)
        self.cache.add(sha256('salt'.encode() + url.encode()).hexdigest())
        print('Ваш url добавлен в кэш') if len(self.cache) > cache_len else print('Ваш url уже присутствует в кэше')


cache = CacheUrl()

print(*cache.cache)

cache.url_add('https://gb.ru/')
cache.url_add('https://gb.ru/')
cache.url_add('https://www.youtube.com/')

print(*cache.cache)
