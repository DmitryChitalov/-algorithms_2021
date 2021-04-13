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
cache = {}


def check_page(url):
    if cache.get(url):
        print(f'Адрес {url} уже присутствует в кэше')
    else:
        cache.update({url: hashlib.sha256(salt.encode() + url.encode()).hexdigest()})
        print(f'Адрес {url} добавлен в кэш')


check_page('https://gb.ru')
check_page('https://gb.ru')
check_page('https://mail.ru')
check_page('https://mail.ru')
check_page('https://mail.ru')

