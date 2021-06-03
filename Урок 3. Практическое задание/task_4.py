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
from uuid import uuid4

url_cache = {}
salt = uuid4().hex


def make_url_cache(url: str):
    salted_url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if url_cache.get(url):
        print(f'The address is already in the cache {url}')
    else:
        url_cache[url] = salted_url_hash
        print(f'Save to cache: \n{url} ')


make_url_cache('https://geekbrains.ru/')
make_url_cache('https://www.vk.com/')
make_url_cache('https://auto.ru/')
make_url_cache('https://www.rambler.ru/')
make_url_cache('https://www.ya.ru/')

print(f'Save in cashe: \n{url_cache}')
