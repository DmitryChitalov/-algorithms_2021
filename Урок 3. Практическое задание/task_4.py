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

from hashlib import sha1
from uuid import uuid4


class Browser():
    def __init__(self):
        self.seen = {}
        self.salt = uuid4().hex

    def browse(self, url):
        if url not in self.seen:
            self.seen[url] = sha1(url.encode() + self.salt.encode()).hexdigest()

browser = Browser()

for url in ['mail.ru', 'yandex.ru', 'google.com', 'mail.ru', 'vk.com', 'google.com']:
    browser.browse(url)

print(browser.seen)
