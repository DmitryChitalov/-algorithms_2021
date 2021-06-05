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


def check_hash(url, dict_cache):
    hash_url = hashlib.sha256('your salt is mine'.encode() + url.encode()).hexdigest()
    if hash_url not in dict_cache.keys():
        dict_cache[hash_url] = url
    return


db_cache = {}
list_test_url = ['https://github.com/', 'https://ru.wikipedia.org/', 'https://translate.google.com/',
                 'https://github.com/', 'https://python-scripts.com/', 'https://ru.wikipedia.org/']
[check_hash(i, db_cache) for i in list_test_url]
print(db_cache)
