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


def cache_web(site, cache_table):
    if cache_table.get(site):
        print(f'Адрес {site} уже кеширован')
    else:
        cache_table[site] = hashlib.sha256(uuid4().hex.encode() + site.encode()).hexdigest()
        print(cache_table)


cache = {}

cache_web("google.com", cache)
cache_web("stackoverflow.com", cache)
cache_web("google.com", cache)
