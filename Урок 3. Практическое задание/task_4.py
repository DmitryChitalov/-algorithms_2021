"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

url : хеш-url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

import hashlib

url_cash = {}


def url_hash(url):
    salt = url.replace('.', '')
    get_hash = hashlib.sha256(salt.encode() + url.encode('utf-8')).hexdigest()
    if url_cash.get(get_hash):
        print(url_cash[get_hash])
    else:
        url_cash[get_hash] = url


url_hash('google.ru')
print(url_cash)
url_hash('yandex.ru')
print(url_cash)
url_hash('google.ru')
print(url_cash)
