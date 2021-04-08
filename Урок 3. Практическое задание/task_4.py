"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
from hashlib import sha256
from uuid import uuid4

salt = uuid4().hex
cache = {}


def my_cache(string):
    hash_string = sha256(salt.encode() + string.encode()).hexdigest()
    if hash_string not in cache.values():
        cache[string] = hash_string
        print(f'url {string} добавлен в базу')
    else:
        print(f'url {string} уже в базе')


my_cache("ya.ru")  # url ya.ru добавлен в базу
my_cache("ya.ru")  # url ya.ru уже в базе
my_cache("google.ru")  # url google.ru добавлен в базу