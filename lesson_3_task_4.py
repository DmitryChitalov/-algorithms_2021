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


def url_cache(func):
    def g(n, cache={}):
        r = cache.get(n)
        if r is None:
            r = func(n)
            cache[n] = r
        print(cache)
        return r, cache

    return g


@url_cache
def url_hash(link):
    salt = uuid4().hex
    res = hashlib.sha256(salt.encode() + link.encode()).hexdigest()
    return res


url_hash('https://www.google.ru/')
url_hash('https://gb.ru/')
url_hash('https://habr.com/ru/')
