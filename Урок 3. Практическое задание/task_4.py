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


def find_url(url):
    salt = uuid4().hex
    hash_url = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
    if url in some_dict.values():
        print('This URL exists')
    else:
        some_dict[hash_url] = url
        print(some_dict)


some_dict = {}
for i in range(5):
    url = input('Enter URL-address: ')
    find_url(url)

