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


def get_hash(url, salt):
    """Генерируется соленый hash"""
    return hashlib.sha256(url.encode() + salt.encode()).hexdigest()


cache_data = {}
SALT = 'AnY SeCrEt SaLt'

while True:
    url = input('Enter URL (For exit type Q): ')
    if url.lower() == 'q':
        break
    url_hash = get_hash(url, SALT)

    if cache_data.get(url_hash):
        print(f'URL {cache_data[url_hash]} already added to cache.')
    else:
        cache_data[url_hash] = url
        print(f'URL {cache_data[url_hash]} was not find in cache. It will be add to cache now.')
