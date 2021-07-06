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
from hashlib import sha256
import uuid

salt = uuid.uuid4().hex
url_hash = {}

def get_hash_url(url):
    if url_hash.get(url):
        print(f'Адрес {url} уже есть в кэше')
    else:
        hash_obj = sha256(salt.encode() + url.encode()).hexdigest()
        url_hash[url] = hash_obj
        print(url_hash)

get_hash_url('https://github.com')
get_hash_url('https://github.com')
