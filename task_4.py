"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

хеш-url : url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


import hashlib


class Pages:

    def __init__(self):
        self.cache = {}
        self.salt = 'Я люблю солить <3'

    def create_hash(self, url):
        return hashlib.sha256(self.salt.encode() + url.encode()).hexdigest()

    def add_in_cache(self, url):
        print('Добавлено в кэш.')
        self.cache[self.create_hash(url)] = url

    def find_in_cache(self, url):
        if self.cache.get(self.create_hash(url)):
            print(self.cache[self.create_hash(url)])
        else:
            self.add_in_cache(url)


if __name__ == '__main__':
    a = Pages()
    a.find_in_cache('https://www.spotify.com/us/')
    a.find_in_cache('https://www.spotify.com/us/')
    a.find_in_cache('https://vk.com/')
    print(a.cache)
