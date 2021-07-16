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

from uuid import uuid4
from hashlib import sha256


class URLCache:
    """
    Класс для работы с кешем. Храним данные в словаре url: hash.
    """
    def __init__(self):
        self.__cache = dict()

    def get_value(self, value):
        if not self.__cache.get(value):
            __salt = uuid4().hex
            __value = value + __salt
            __value_hash = sha256(__value.encode('utf-8'))
            __value_hexdig = __value_hash.hexdigest()

            self.__cache[value] = __value_hexdig

        return self.__cache[value]

    def get_cache(self):
        return self.__cache

    def clear_cash(self):
        self.__cache.clear()


url_cache = URLCache()

urls = ["https://yandex.ru", "https://google.ru", "https://mail.ru", "https://stackoverflow.com",
        "https://github.com", "https://mail.google.com/", "https://mail.ru", "https://google.ru"]

for u in urls:
    url_cache.get_value(u)

print([f"{k}: {v};" for k, v in url_cache.get_cache().items()])

url_cache.clear_cash()









