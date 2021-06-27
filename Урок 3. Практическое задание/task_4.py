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
import hashlib


class UrlCache:
    def __init__(self):
        self.cache = dict()

    def check_url(self, url):
        if not url in self.cache:
            self.cache[url] = hashlib.sha3_256(uuid4().hex.encode() + url.encode()).hexdigest()
        return self.cache[url]


if __name__ == '__main__':
    mycache = UrlCache()
    mycache.check_url('gb.ru')
    mycache.check_url('facebook.com')
    mycache.check_url('vk.com')
    mycache.check_url('ok.ru')
    mycache.check_url('ok.ru')

    print(mycache.__dict__)
