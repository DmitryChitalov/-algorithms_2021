#!/usr/bin/env python3

from uuid import uuid4
from hashlib import sha256

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


class Cache:
    __cache = dict()

    @classmethod
    def show(cls) -> str:
        print(cls.__cache)

    @classmethod
    def __str__(cls) -> str:
        return str(cls.__cache)

    @classmethod
    def get(cls, url) -> str:
        result = cls.__cache.get(url)
        if result is None:
            result = sha256(f'{url}{uuid4().hex}'.encode('utf-8')).hexdigest()
            cls.__cache[url] = result
        return result


def main():
    print(Cache())
    Cache.get(r'https://www.youtube.com')
    Cache.get(r'https://vk.com')
    Cache.get(r'https://news.google.com')
    Cache.get(r'https://vk.com')
    print(Cache())


if __name__ == '__main__':
    main()
