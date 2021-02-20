"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

import hashlib
from uuid import uuid4

hash_table = {}
salt = uuid4().hex


def func1(url):
    hash_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if hash_table.get(url):
        print(f'Адрес в кэше')
    else:
        hash_table[url] = hash_url
        print(f'Адрес добавлен в кэш')

func1("google.com")
func1("google.com")