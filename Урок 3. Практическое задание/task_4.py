"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

from hashlib import pbkdf2_hmac


class CacheUrl:
    def __init__(self):
        self.cache_dict = {}
        self.__salt = 'salty_salt'

    def add_url(self, url):
        if not self.cache_dict.get(url):
            self.cache_dict[url] = pbkdf2_hmac(hash_name='sha256',
                                               password=url.encode('UTF-8'),
                                               salt=self.__salt.encode('UTF-8'),
                                               iterations=100000)
            print(f'{url} занесен в кэш')
        else:
            print(f'{url} уже есть в кэше')
    def __str__(self): # вывод всего кэша
        dict_print = 'Весь словарь: \n'
        for  k, v in self.cache_dict.items():
            dict_print += str(k) + ' : ' + str(v.hex()) + '\n'
        return dict_print




my_cache = CacheUrl()
my_cache.add_url('https://google.com')
my_cache.add_url('https://yandex.ru')
my_cache.add_url('https://geekbrains.ru')
my_cache.add_url('https://geekbrains.ru')


print(my_cache)
