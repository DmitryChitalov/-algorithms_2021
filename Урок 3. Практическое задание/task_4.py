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

urls = {}  # словарь с адресами
salt = 'salt'


def url_cash(uri):
    result = urls.get(hashlib.sha256(salt.encode() + uri.encode()).hexdigest())
    if result is None:
        urls[hashlib.sha256(salt.encode() + uri.encode()).hexdigest()] = uri
        result = uri
    return result


url_cash('https://gb.ru/lessons/145450')
url_cash('https://gb.ru/lessons/145448')
url_cash('https://gb.ru/lessons/145449')
url_cash('https://gb.ru/lessons/145449')
url_cash('https://gb.ru/lessons/145445')
url_cash('https://gb.ru/lessons/145445')
url_cash('https://gb.ru/lessons/145433')
for k, v in urls.items():
    print(k, ':', v)
