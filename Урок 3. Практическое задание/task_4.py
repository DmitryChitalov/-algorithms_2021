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


salt = uuid4().hex
cache_list = []


def check_cache(url_address):
    if hashlib.sha256(salt.encode() + url_address.encode()).hexdigest() not in cache_list:
        cache_list.append(hashlib.sha256(salt.encode() + url_address.encode()).hexdigest())


check_cache('https://google.com/')
check_cache('https://geekbrains.ru/')
check_cache('https://google.com/')

print(cache_list)


