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


def make_cache(url: str):
    salted_url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if url_cache.get(url):
        print(f' "Этот адрес {url} уже есть в кэше')
    else:
        url_cache[url] = salted_url_hash
        print(f'Сохраняем адрес {url}  в кэш')


make_cache('https://google.com/')
make_cache('https://www.yandex.ru/')
make_cache('https://gb.ru/')
make_cache('https://google.com/')
make_cache('https://vk.com/')
make_cache('https://www.bash.im/')
make_cache('https://www.ya.ru/')
make_cache('https://vk.com/')


print(f'В кэше сохранены: {url_cache}')