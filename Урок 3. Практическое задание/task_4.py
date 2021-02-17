"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

from binascii import hexlify
from hashlib import pbkdf2_hmac
from uuid import uuid4
urls = {}
url = input("url = ")
while url != "exit":
    if urls.get(url) is None:
        salt = uuid4().hex

        obj = pbkdf2_hmac(hash_name='sha256',
                          password=url.encode(),
                          salt=salt.encode(),
                          iterations=100000)

        result = hexlify(obj)
        urls[url] = result
    url = input("url = ")
