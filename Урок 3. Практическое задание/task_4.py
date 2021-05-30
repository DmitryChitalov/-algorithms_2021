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
from __future__ import annotations
import re
from uuid import uuid4
import hashlib


class Url:
    def __init__(self, name: str) -> None:
        self._name = self.get_url_text(name)
        self.salt = uuid4().hex

    @staticmethod
    def get_url_text(url: str) -> str:
        pattern = re.compile(r'http(s:|:)//(www.|ww2.|)([0-9a-z.A-Z-]*\.\w{2,3})')
        return pattern.match(url).group()

    @property
    def name(self) -> str:
        return self._name

    def __hash__(self) -> int:
        return hash(self.salt.encode('utf-8') + self.name.encode('utf-8'))

    def __eq__(self, other: Url) -> bool:
        if isinstance(other, Url) and other.__hash__() == self.__hash__():
            return True
        return False


class UrlCash:
    def __init__(self) -> None:
        self.cash_dict = {}

    def to_cash(self, url: Url) -> str:
        if isinstance(url, Url) and not self.cash_dict.get(url.name):
            self.cash_dict[url.name] = url.__hash__()
            return f'Страница {url.name} добавлена в кэш'
        return f'Страница {url.name} уже в кэше'


if __name__ == '__main__':
    url1 = Url('https://medium.com/nuances-of-programming/')
    url2 = Url('http://cursedcreatures.f-rpg.me/viewtopic.php?id=4690&p=7')
    url3 = Url('https://gb.ru/lessons/141727')

    url_cash = UrlCash()
    url_list = (url1, url2, url3)

    for i in range(2):
        for url in url_list:
            print(url_cash.to_cash(url))
