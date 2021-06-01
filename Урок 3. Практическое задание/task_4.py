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
import uuid

cache_dict = {}
salt = uuid.uuid4().hex


def check_url(url_address):
    hash_url = hashlib.sha256(salt.encode() + url_address.encode()).hexdigest()
    if hash_url in cache_dict.keys():
        print(f"Кэш для {url_address} уже существует")
    else:
        cache_dict[hash_url] = "cache"
        print(f"Кэш для {url_address} успешно добавлен")
    return


check_url("https://github.com/")
check_url("https://gb.ru/")
check_url("https://www.codewars.com/")
check_url("https://mail.ru/")
check_url("https://gb.ru/")
check_url("https://habr.com/ru/")
check_url("https://github.com/")
