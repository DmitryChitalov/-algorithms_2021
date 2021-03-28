"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""


import os
import hashlib


def fetch_url(url):
    if cached_pages.get(url) is None:
        print("Will cache url")
        page_hash = hashlib.sha256(url.encode("utf-8") + salt).hexdigest()
        cached_pages[url] = page_hash
    else:
        print(f"Page {url} is in the cache ({cached_pages[url]})")


salt = os.urandom(32)
cached_pages = {}

fetch_url("www.google.com")
fetch_url("www.google.com")
fetch_url("www.google.com")
fetch_url("www.facebook.com")
fetch_url("www.mail.com")
fetch_url("www.facebook.com")
