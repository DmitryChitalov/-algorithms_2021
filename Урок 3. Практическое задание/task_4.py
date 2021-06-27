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

salt = uuid4().hex
cache_sites = {}

def cache_url(url):
    if not cache_sites.get(url):
        cache_sites[url] = hashlib.sha256(salt.encode() + url.encode()).hexdigest()


cache_url('https://yandex.ru')
cache_url('https://championat.com.')


print(cache_sites)
