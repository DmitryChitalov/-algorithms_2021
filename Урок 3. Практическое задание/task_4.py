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


def to_cache(url: str):
    url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if url_cache.get(url):
        print(f'Этот адрес {url} уже есть в кэше')
    else:
        url_cache[url] = url_hash
        print(f'Адрес {url}  был сохранен в кэш')


to_cache("https://www.litres.ru/")
to_cache("https://google.com/")
to_cache("https://vk.com/")
to_cache("https://www.instagram.com/")
to_cache("https://www.litres.ru/")
to_cache("https://google.com/")
to_cache("https://vk.com/")
to_cache("https://www.instagram.com/")

print(f'В кэше сохранены: {url_cache}')
