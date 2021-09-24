"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

хеш-url : url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

from uuid import uuid4
import hashlib

salt = uuid4().hex

class Page():

    def __init__(self, url):
        self.url = url

    def get_cache(self):
        dict_cache = {}
        dict_cache.setdefault(self.url, hashlib.sha256(salt.encode() + self.url.encode()).hexdigest())
        return dict_cache

page_1 = Page('geekbrains.ru')
page_2 = Page('github.com')

print(page_1.get_cache())
print(page_2.get_cache())