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
        self.data = set()

    def add(self, url):
        self.data.add(self.hash_url(url))

    def get_all(self):
        return self.data

    @staticmethod
    def hash_url(url):
        salt = 'any_salt'
        return hashlib.sha256(salt.encode() + url.encode()).hexdigest()


cache = UrlCache()
cache.add('https://google.ru')
cache.add('https://ya.ru')
cache.add('https://google.ru')
cache.add('https://yandex.ru')
cache.add('https://yandex.ru')
cache.add('https://yandex.ru')
cache.add('https://goog.ru')
cache.add('https://gle.ru')
cache.add('https://ggle.ru')
cache.add('https://goge.ru')
cache.add('https://goole.ru')
cache.add('https://google.ru')
cache.add('https://ggle.ru')
cache.add('https://ya.ru')
cache.add('https://yandex.ru')
cache.add('https://google.ru')
cache.add('https://goo.ru')
cache.add('https://goge.ru')
cache.add('https://googe.ru')
cache.add('https://goo.ru')


print(cache.get_all())
