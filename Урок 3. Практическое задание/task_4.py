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


class CachChecker:
    def __init__(self):
        self.salt = 'salt_forever'
        self.cache = {}

    def url_salt_hasher(self, url):
        return hashlib.sha256(self.salt.encode() + url.encode()).hexdigest()

    def cache_check(self, url):
        if self.url_salt_hasher(url) in self.cache.keys():
            return 'URL is already exist'
        else:
            self.cache[self.url_salt_hasher(url)] = url
            return 'URL has been cached'


CC_object = CachChecker()
while True:
    user_url = input('Input url or x to exit: ')
    if user_url.lower() == 'x':
        print(CC_object.cache)
        break
    print(CC_object.cache_check(user_url))