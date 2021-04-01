"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

from uuid import uuid4
import hashlib

salt = uuid4().hex
cache_page = {}


def get_address(url):
    if cache_page.get(url):
        print('Данная страница: ', url, 'присутствует в кэше')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_page[url] = res
        print('Данной страницы: ', url, 'нет в кэше')


get_address('https://instagram.com/paul__antonov?igshid=n4q8p3x7fltp')
get_address('https://instagram.com/paul__antonov?igshid=n4q8p3x7fltp')
get_address('https://vk.com/paulantonov')
get_address('https://vk.com/paulantonov')
