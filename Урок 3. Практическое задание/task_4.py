"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
from uuid import uuid4
from hashlib import sha256


class WebCache:

    def __init__(self):
        self.url_cache = {}
        self.salt = uuid4().hex

    # генерируем хеш
    def __get_hash(self, url):
        return sha256(url.encode('utf-8') + self.salt.encode('utf-8')).hexdigest()

    # проверяем наличие url в кеше
    def is_cached(self, url):
        return self.__get_hash(url) in self.url_cache

    # добавляем url
    def add_url(self, url):
        if self.is_cached(url):
            print(f'Страница {url} уже существует')
        else:
            self.url_cache[self.__get_hash(url)] = url
            print(f'Страница {url} успешно добавлена в кэш')

    # выводим на экран хеши для кэшированных страниц
    def show_cache(self):
        for key, value in self.url_cache.items():
            print(f'{value} - {key}')


if __name__ == '__main__':

    url_cache = WebCache()

    url_cache.add_url('gb.ru')
    url_cache.add_url('gb.ru')
    url_cache.add_url('yandex.ru')
    url_cache.add_url('github.com')
    url_cache.add_url('github.com')

    url_cache.show_cache()
