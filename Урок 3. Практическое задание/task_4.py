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

SALT = uuid4().hex
url_dict = {}


def url_dict_add(url):
    hash_url = hashlib.sha256(SALT.encode() + url.encode()).hexdigest()
    if not url_dict.get(hash_url):
        url_dict[hash_url] = url


url_dict_add('https://gb.ru/')
url_dict_add('https://gb.ru/')
url_dict_add('https://github.com/')
url_dict_add('https://mail.google.com/')

print(url_dict)
