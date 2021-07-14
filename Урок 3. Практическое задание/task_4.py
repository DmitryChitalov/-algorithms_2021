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
from uuid import uuid4


class HashUrls:
    def __init__(self):
        self.hashes = {}

    def in_cache(self, url):
        if self.hashes.get(url, None) is not None:
            return True
        else:
            return False

    def add_cache(self, url):
        if not self.in_cache(url):
            self.hashes[url] = sha256(url.encode() + str(uuid4()).encode()).hexdigest()
            print(f'Страница {url} добавлена в кеш.')
            return True
        else:
            print(f'Страница {url} уже в кеше.')
            return False

    def __str__(self):
        return 'В кеше содержатся следующие страницы:\n' + '\n'.join(self.hashes.keys())


hs = HashUrls()
hs.add_cache('https://mail.ru')
hs.add_cache('https://mail.ru')
hs.add_cache('https://mail.ru')
hs.add_cache('https://google.com')
hs.add_cache('https://gosuslugi.ru')
print(hs)
