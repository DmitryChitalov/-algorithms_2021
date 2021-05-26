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
from uuid import uuid4
import hashlib

url = input('Type your site here: ')
salt = url
cache = {}


def cache_site(site):
    if not cache.get(site):
        odj = hashlib.sha256(salt.encode() + site.encode()).hexdigest()
        cache[site] = odj
        print(cache)
    else:
        print('There is such site in base')


cache_site(url)
cache_site(url)
