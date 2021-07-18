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


class Cash:
    def __init__(self):
        self.url = {}

    def check_cash(self,url):
        salt = uuid4().hex
        url_hash = hashlib.sha256(salt.encode() +  url.encode()).hexdigest()
        self.url.setdefault(url,url_hash)
        return f'Запись Hash по ключу {url}'
url = 'https://gb.ru/lessons/150346'

urls = Cash()
print(urls.check_cash(url))

print(urls.url)
