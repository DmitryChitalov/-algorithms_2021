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


class Cache:
    def __init__(self):
        self.cache_dict = {}
        self.__salt = 'hard_salt_123'

    def add_url(self, url):
        if not self.cache_dict.get(url):
            self.cache_dict[url] = pbkdf2_hmac(hash_name='sha256',
                                               password=url.encode('UTF-8'),
                                               salt=self.__salt.encode('UTF-8'),
                                               iterations=10000)
            print('DONE')
        else:
            print('Страница уже закэширована!')


new_cache = Cache()
new_cache.add_url('https://geekbrains.ru/')
new_cache.add_url('https://yandex.ru/')
new_cache.add_url('https://www.instagram.com/')
new_cache.add_url('https://www.instagram.com/')

# просмотр кэша
print()
for item in new_cache.cache_dict:
    print(item)
