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


class Cache:
    def __init__(self):
        self.memory = {}
        pass

    def get_hash(self, url):
        hash_obj = sha256(url.encode() + url.encode()).hexdigest()
        return hash_obj

    def cache_url(self, url):
        if self.memory.get(url):
            return f'Адрес {url} уже находится в кэше'
        else:
            hash_obj = self.get_hash(url)
            self.memory[url] = hash_obj
            return f'Адрес {url} внесен в кэш: {hash_obj}'


a = Cache()
print(a.cache_url('https://mysite.ru/'))
print(a.cache_url('https://mysite.ru/'))
print(a.cache_url('https://mysite_1.ru/'))
print(a.cache_url('https://mysite_1.ru/'))
