"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
import hashlib
from uuid import uuid4


class UrlCache:
    def __init__(self):
        self.url_cache = {}

    def check_url(self, url):
        if url in self.url_cache.values():
            return url
        else:
            salt = uuid4().hex
            url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
            self.url_cache[url_hash] = url
            return 'Url добавлен в кэш'


url = UrlCache()

print(url.check_url('google.com'))
print(url.check_url('yandex.ru'))

print(url.check_url('google.com'))

print(url.url_cache)

