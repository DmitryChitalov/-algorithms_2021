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


class Cache:
    def __init__(self):
        self.__cache_dict__ = dict()

    def get_value(self, value):
        if not value in self.__cache_dict__:
            __salt__ = uuid4().hex
            __value_str__ = f'{value}{__salt__}'
            __value_obj__ = sha256(__value_str__.encode('utf-8'))
            __value_hex_dig__ = __value_obj__.hexdigest()

            self.__cache_dict__[value] = __value_hex_dig__

        return self.__cache_dict__[value]

    @property
    def cache_data(self):
        __cache_keys__ = self.__cache_dict__.keys()
        return ', '.join([key for key in __cache_keys__])


if __name__ == '__main__':
    url_cache = Cache()
    url_cache.get_value('ya.ru')
    url_cache.get_value('yandex.ru')
    url_cache.get_value('google.ru')
    url_cache.get_value('ya.ru')

    print(f'Значения в кэше: {url_cache.cache_data}')
