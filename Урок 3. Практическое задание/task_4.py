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

from uuid import uuid4
import hashlib

salt = uuid4().hex
cache_url = dict()


def check_url(url):
    hash_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if hash_url in cache_url:
        print(f'Аадрес {url} присутствует в кэше')
    else:
        print(f'Адрес: {url} новый. Добавим в кэш')
        cache_url[hash_url] = url
        print('Текущая кэш таблица:')
        for x in cache_url:
            print(x, cache_url[x])

check_url('https://pythonworld.ru/')
check_url('https://www.google.com/')
check_url('https://pythonworld.ru/')
