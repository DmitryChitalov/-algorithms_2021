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

import hashlib as hs
import uuid as uu

cache = {}
salt = uu.uuid4().hex

def cache_check(url, salt):
    if url not in cache.keys():
        url_hash = hs.sha256(url.encode() + salt.encode()).hexdigest()
        cache.update({url: url_hash})
        print('Данный url добавлен в cache')
    else:
        print('Данный url уже существует в cache')

cache_check('https://pythonworld.ru/', salt)
print(cache)
cache_check('https://pythonworld.ru/', salt)
cache_check('https://www.youtube.com/', salt)
print(cache)
