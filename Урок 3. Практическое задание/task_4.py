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


class AddressCache:
    def __init__(self, set_cache):
        self.cache = set_cache

    def add_cache(self, el):
        if el not in tuple(self.cache.keys()):
            salt = uuid4().hex
            res = hashlib.sha256(el.encode() + salt.encode()).hexdigest()
            self.cache[el] = [res, salt]
            return 'URL has been cache'
        else:
            return 'Such url already exists'

    def pop_out(self, el):
        if el in self.cache.keys():
            self.cache.pop(el)
        else:
            return 'There is not such URL'

    def get_cache(self, el):
        return self.cache[el]

    def check_cache(self):
        return self.cache


if __name__ == '__main__':
    start = AddressCache({})
    print(start.add_cache('https://ru.wikipedia.org'))
    print(start.check_cache())
    print(start.add_cache('https://translate.google.com/translate'))
    print(start.check_cache())
    print(start.get_cache('https://translate.google.com/translate'))