"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

import hashlib
from uuid import uuid4

salt = uuid4().hex
hash_dict = {}


def url_cache(some_url):
    url_hash = hashlib.sha256(salt.encode() + some_url.encode()).hexdigest()
    if url_hash not in hash_dict:
        hash_dict.update({some_url: url_hash})


url_cache('https://gb.ru/')
url_cache('https://vk.com/')
url_cache('https://www.youtube.com/')
url_cache('https://yandex.ru/')
url_cache('https://github.com/')
url_cache('https://github.com/')
url_cache('https://gb.ru/')

print(hash_dict)
