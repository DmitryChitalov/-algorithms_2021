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
import uuid


class CachePages:
    def __init__(self):
        self.salt = uuid.uuid4().hex
        self.cache_obj = {}

    def get_page(self, url):
        if self.cache_obj.get(url):
            print(f'Этот адрес: {url} присутствует в кэше')
        else:
            res = hashlib.sha256(self.salt.encode() + url.encode()).hexdigest()
            self.cache_obj[url] = res
            print(self.cache_obj)


cache_pages = CachePages()
cache_pages.get_page('https://gb.ru/')
cache_pages.get_page('https://gb.ru/')
cache_pages.get_page('https://gb.ru/')
cache_pages.get_page('https://gb.ru/courses')
cache_pages.get_page('https://gb.ru/courses')
cache_pages.get_page('https://gb.ru/courses')
