"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш
"""
import hashlib
from uuid import uuid4

url_cache = {}
salt = uuid4().hex


def make_url_cache(url: str):
    salted_url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if url_cache.get(url):
        print(f'Адрес уже есть в кэше {url}')
    else:
        url_cache[url] = salted_url_hash
        print(f'Сохраняем в кэш: {url} ')


make_url_cache('https://geekbrains.ru/')
make_url_cache('https://www.vk.com/')
make_url_cache('https://geekbrains.ru/')
make_url_cache('https://www.yandex.ru/')
make_url_cache('https://www.ya.ru/')
make_url_cache('https://www.https://habr.com/')

print(f'В кэше сохранены: {url_cache}')
