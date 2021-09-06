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


def cache_func(url):
    if url in hash_table.keys():
        txt_url = url[url.find('//')+2:-1].capitalize()
        print(f'Сайт {txt_url} запсан в таблице')
    else:
        hash_table[url] = hashlib.sha256(url.encode()).hexdigest()


file = open("my_web_history.txt", "r")
lines = file.readlines()
file.close()
for line in lines:
    cache_func(line.strip())
