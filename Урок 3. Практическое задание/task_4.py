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

cache = dict()
salt = uuid4().hex


def checker(url):
    if url in cache.keys():
        print(f'Адрес {url} уже есть в кэше')
    else:
        url_address = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache[url] = url_address


checker('https://yandex.ru')
checker('https://www.google.com/')
checker('https://yandex.ru')
checker('https://gb.ru')
print(cache)
