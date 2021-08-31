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
from uuid import uuid4


class WebCash:
    def __init__(self):
        self.urls = {}

    def hash_1(self, url):
        salt = uuid4().hex
        hash_u = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        return hash_u

    def cash_1(self, url):
        hash_u = self.hash_1(url)
        self.urls.setdefault(url, hash_u)


url_1 = 'https://gb.ru/education'

url_check = WebCash()

url_check.cash_1(url_1)

print(url_check.urls)
