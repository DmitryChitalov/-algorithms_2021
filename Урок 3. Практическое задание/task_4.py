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


def site(url):
    salt = 'https://'
    print(salt)
    if dict_of_site.get(url):
        print("такой сайт уже есть")
    else:
        hash_for_dict = hashlib.sha256(salt.encode()+url.encode()).hexdigest()
        dict_of_site[url] = hash_for_dict
        print(dict_of_site)


dict_of_site = {}

site('https://stackoverflow.com/questions/48613002/sha-256-hashing-in-python')
site('https://stackoverflow.com/questions/48613002/sha-256-hashing-in-python')
site('https://docs-python.ru/standart-library/modul-hashlib-python/')
site('https://python-scripts.com/sqlite')
site('https://python-scripts.com/sqlite')
