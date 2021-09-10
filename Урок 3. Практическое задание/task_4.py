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

from uuid import uuid4
import hashlib


def hash(salt, url):
    return hashlib.sha256(salt.encode() + url.encode()).hexdigest()


cache = {}
salt = uuid4().hex
url = 1
while url != '0':
    url = input('Введите URL: ')
    if url == '0':
        break
    hash_url = hash(salt, url)
    if cache.get(hash_url):
        print(f'"{cache.get(hash_url)}" есть в кэше')
    else:
        cache[hash_url] = url
        print(f'"{cache[hash_url]}" внесён в кэш.')

