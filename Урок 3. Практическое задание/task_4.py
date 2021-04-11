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


list_of_url = ['https://vk.com/yanok0yanok', 'https://www.google.ru/', 'https://www.kinopoisk.ru/',
            'https://translate.yandex.ru/']

data_base = {'hash': []}


def hash_function(web_url, db):

    salt = '1000'

    hash_url = hashlib.sha256(web_url.encode(encoding="utf-8")+salt.encode()).hexdigest()

    if hash_url in db['hash']:

        print("*" * 70)

        print(f'Данная ссылка: {web_url} уже присутствует в кэше')

        return db

    data_base['hash'].append(hash_url)

    print("*" * 70)

    print(f'Ссылка {web_url} добавлена')

    return db


for i in list_of_url:

    hash_function(i, data_base)

for i in list_of_url:

    hash_function(i, data_base)
