"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
from hashlib import sha256 as sha256
from uuid import uuid4 as uuid4

salt = uuid4().hex
url_list = {}


def add_url(url):

    print(f'{url_list.update({sha256(salt.encode() + url.encode()).hexdigest(): url})} '
          f'{url} has been added in list!'[5:]) if check(url) is False else print(f'{url} has already been added!')


def check(url):

    return False if not url_list.get(sha256(salt.encode() + url.encode()).hexdigest()) else True


add_url('https://geekbrains.ru/')
add_url('https://geekbrains.ru/')
add_url('https://vk.com/')
add_url('https://vk.com/')
add_url('https://vk.com/')
