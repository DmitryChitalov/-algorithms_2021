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
from uuid import uuid4
import hashlib


url_hash_dct = dict()
salt = uuid4().hex


def url_check(url):
    salt_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if salt_hash not in url_hash_dct:
        url_hash_dct[salt_hash] = url
        print('url внесён в кэш', url_hash_dct)
    else:
        print('url был внесён в кэш ранее')


p = 'https://mail.ru/'
url_check(p)
url_check(p)
