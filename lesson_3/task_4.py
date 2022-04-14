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

from hashlib import sha256
from uuid import uuid4


class UrlCash:

    def __init__(self):
        self.urls = {}
        self.salt = str(uuid4()).encode('utf-8')

    def hash(self, url):
        return sha256(url.encode('utf-8') + self.salt).hexdigest()

    def cash(self, url):
        if self.urls.get(self.hash(url)):
            return
        self.urls[self.hash(url)] = url

    def __str__(self):
        result = ''
        for index, value in self.urls.items():
            result += f'{index}:{value}\n'
        return result


url_cash = UrlCash()
url_cash.cash('test1.com')
url_cash.cash('test2.com')
url_cash.cash('test3.com')
url_cash.cash('test3.com')
url_cash.cash('test3.com')

print(url_cash)
