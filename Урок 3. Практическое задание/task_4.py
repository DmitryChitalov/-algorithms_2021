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
import uuid
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class HashedLinks:
    def __init__(self):
        self._salt = uuid.uuid4( ).bytes
        self.database = {}
        self._validator = URLValidator( )

    def check_link(self, link):
        hashed_link = sha256(self._salt + link.encode('utf-8')).hexdigest( )
        if hashed_link in self.database:
            return self.database[hashed_link]
        else:
            self.add_link(link)

    def add_link(self, link):
        try:
            self._validator(link)
        except ValidationError:
            print('Введена некорректная ссылка.')
        else:
            print(f'В базу была добавлена новая ссылка {link}.')
            hashed_link = sha256(self._salt + link.encode('utf-8')).hexdigest( )
            self.database[hashed_link] = link

    @property
    def view_cash(self):
        return self.database


My_links_cash1 = HashedLinks( )
My_links_cash1.add_link('https://vk.com/feed')
print(My_links_cash1.view_cash)
My_links_cash1.check_link('mail.ru')
print(My_links_cash1.view_cash)
print(My_links_cash1.check_link('https://vk.com/feed'))
