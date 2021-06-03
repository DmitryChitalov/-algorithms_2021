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


def memorize(func):
    def wrapped(u, memory):
        new_hash = func(u, memory)
        n = memory.get(new_hash)
        if n is None:
            memory[new_hash] = u
            print("Added new web-page")
            return
        print("This page has already added in dictionary")
    return wrapped


@memorize
def set_url(new_url, memo_dict):
    salt = uuid4().hex
    hash_obj = hashlib.sha256(salt.encode() + new_url.encode('utf-8'))
    return hash_obj.hexdigest()


url_dict = {}
set_url('https://www.google.com/', url_dict)
set_url('https://ya.ru/', url_dict)
set_url('https://ya.ru/', url_dict)
print(url_dict)
