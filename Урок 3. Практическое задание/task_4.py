"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

url : хеш-url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

import hashlib
from uuid import uuid4


salt = uuid4().hex
dict_cash_urls = {}


def get_url(url):
    if dict_cash_urls.get(url):
        print(f'{url} присутствует в кэше')
    else:
        url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        dict_cash_urls[url] = url_hash
        print(f'{url} добавлен в кэш')


get_url('https://gb.ru')
get_url('https://www.youtube.com')
get_url('https://gb.ru')
