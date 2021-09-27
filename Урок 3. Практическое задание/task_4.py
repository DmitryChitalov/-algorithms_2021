"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

хеш-url : url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


import hashlib
from uuid import uuid4

salt = uuid4().hex
cache_object ={}


def get_page(url):
    if cache_object.get(url):
        print(f'{url} is present in cache')
    else:
        result = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_object[url] = result
        print(cache_object)


get_page('https://github.com')

