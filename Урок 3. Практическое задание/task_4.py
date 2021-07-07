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


class UrlCache:
    def __init__(self):
        self.cache = {}

    def hash_url(self, url_addr):
        url_hash = hashlib.sha256(url_addr.encode() +
                                  'js2df79290hs3d2fl2fl6s4d24f0fdn45ngf3jdn3j2'.encode()).hexdigest()
        return url_hash

    def check_url(self, url_addr):
        url_hash = self.hash_url(url_addr)
        if url_hash in self.cache.keys():
            return True
        else:
            return False

    def add_url(self, url_addr):
        url_hash = self.hash_url(url_addr)
        if not self.check_url(url_addr):
            self.cache.update({url_hash: url_addr})
            return print('URL добавлен')

    def rm_url(self, url_addr):
        if self.check_url(url_addr):
            del self.cache[self.hash_url(url_addr)]
            return print('URL удален')

    def show(self):
        for item in self.cache.items():
            print('Hash: ' + item[0] + ', URL: ' + item[1])


urlcache = UrlCache()
urlcache.add_url('https://gb.ru')
urlcache.show()
urlcache.rm_url('https://gb.ru')
urlcache.show()
urlcache.rm_url('https://gb.ru')
urlcache.show()
urlcache.add_url('https://pythonworld.ru')
urlcache.add_url('https://ya.ru/')
urlcache.add_url('https://google.com/')
urlcache.show()