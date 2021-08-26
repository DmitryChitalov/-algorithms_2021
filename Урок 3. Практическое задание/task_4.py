"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

from hashlib import sha256
web_cache_hash = {}


class MyWebCache:

    def __init__(self):
        self.salt = 'my_salt'

    def chk_cache(self, url):
        """
        :param url: web page address to check
        calc_hash: hash computation
        """
        calc_hash = sha256(self.salt.encode() + url.encode()).hexdigest()
        if calc_hash not in web_cache_hash.keys():
            web_cache_hash[calc_hash] = url
            print(f'{url} - добавлен в кэш.')
        else:
            print(f'{url} - уже присутствует в кэше.')


cache = MyWebCache()

cache.chk_cache('https://habr.com/ru/post/196560/')
cache.chk_cache('http://www.gp.com/Roku/HLS/X264_Settings.htm#no-8x8dct')
cache.chk_cache('http://www.gp.com/Roku/HLS/X264_Settings.htm#no-8x8dct')
print(web_cache_hash)
