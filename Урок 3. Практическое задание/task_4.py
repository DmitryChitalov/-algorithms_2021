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
import hashlib


class UrlCache:
    def __init__(self):
        self.url_dict = {}
        self.salt = uuid4().hex

    def __str__(self):
        return str(self.url_dict)

    def add_url(self, new_url):
        self.url_dict[hashlib.sha256(self.salt.encode() + new_url.encode()).hexdigest()] = new_url

    def check_url(self, new_url):
        if not self.url_dict.get(hashlib.sha256(self.salt.encode() + new_url.encode()).hexdigest()):
            self.add_url(new_url)


urls_hash = UrlCache()
urls_hash.check_url('http://www.vk.ru')
urls_hash.check_url('http://www.twitter.com')
urls_hash.check_url('http://www.vk.ru')
urls_hash.check_url('http://www.facebook.com')
urls_hash.check_url('http://www.vk.ru')
urls_hash.check_url('http://www.instagram.com')

print(urls_hash)
