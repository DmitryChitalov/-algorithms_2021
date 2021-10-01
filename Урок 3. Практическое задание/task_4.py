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


cache = {}

salt = uuid4().hex


def get_page(url):
    if cache.get(url):
        print(f'Получение страницы из кэша... {url} {cache[url]}')
        return cache[url]
    else:
        res = hashlib.sha256(salt.encode() + url.encode('utf-8')).hexdigest()
        print(f'Получение страницы с сервера... {url} {res}')
        cache[url] = res
        return res


if __name__ == '__main__':
    get_page("https://www.kinopoisk.ru/film/758178/")
    get_page("https://www.kinopoisk.ru/film/758178/")
    get_page("https://www.kinopoisk.ru/series/949000/")
    get_page("https://www.kinopoisk.ru/series/949000/")
    get_page("https://www.kinopoisk.ru/series/949000/")
