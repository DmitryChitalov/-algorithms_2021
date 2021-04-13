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

hash_history = set()


def hash_create(url):
    salt = str(url)[::-1]
    url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if url_hash in hash_history:
        return 'Данная страница была захеширована ранее'
    else:
        hash_history.add(url_hash)
        return 'Данная страница захеширована'


print(hash_create("https://gb.ru/education"))
print(hash_create("https://gb.ru/education"))

