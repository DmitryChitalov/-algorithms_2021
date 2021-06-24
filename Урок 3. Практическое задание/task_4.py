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

CACHE_URL = {}
SALT = uuid4().hex


def add_hash_url(my_url):
    if CACHE_URL.get(my_url):
        return print('В кэше уже существует данная страница!')
    url_hash = hashlib.sha256(SALT.encode() + my_url.encode()).hexdigest()
    CACHE_URL[my_url] = url_hash
    return


add_hash_url('https://gb.ru/')
add_hash_url('http://pythonlearn.ru/')
add_hash_url('https://codecamp.ru/')
add_hash_url('https://codecamp.ru/')

for i in CACHE_URL:
    print(f'Страница - "{i}", её хеш - {CACHE_URL.get(i)}')
