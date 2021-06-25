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

cash = set()

def url_hash(url):
    if hashlib.sha256(url.encode() + url.encode()).hexdigest() in cash:
        print(f'{url} => находится в кэш! В кэш не добавлен!')
    else:
        print(f'{url} => отсутствует в кэш! В кэш добавлен!')
        cash.add(hashlib.sha256(url.encode() + url.encode()).hexdigest())



url_hash('https://github.com/')
url_hash('https://github.com/')
url_hash('https://github.com/')
url_hash('https://gb.ru/lessons/145595/homework')
url_hash('https://gb.ru/lessons/145595/homework')
