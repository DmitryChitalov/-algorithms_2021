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

my_cache = dict()


def cache_n_hash(some_url, some_cache):
    if some_url in some_cache:
        return some_cache[some_url]
    else:
        salt = uuid4().hex
        some_cache[some_url] = [(hashlib.sha256((some_url + salt).encode())).hexdigest(), salt]


cache_n_hash('https://gb.ru/courses', my_cache)
cache_n_hash('https://gb.ru/courses', my_cache)
cache_n_hash('https://gb.ru/lessons/150238', my_cache)