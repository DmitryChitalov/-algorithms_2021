"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

хеш-url : url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

import hashlib
from uuid import uuid4

salt = uuid4().hex

class WebCash:
    def __init__(self):
        self.urls = {}

    def hash_1(self, url):
        hash_u = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        if self.urls.get(hash_u):
            print(f"{url} уже существует")
        else:
            self.urls[hash_u] = url

    def cash_1(self):
        for key, value in self.urls.items():
            print(f"{key} : {value}")


url_1 = WebCash()

url_1.hash_1('https://gb.ru/education')

url_1.cash_1()
