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
from urllib.parse import urlparse

hash_dict = {}


def encode(salt, url):
    return hashlib.sha256(salt.encode() + url.encode()).hexdigest()


class Url:

    def __init__(self, url):
        self.salt = 'url_hash'
        self.url = url
        self.encoded_url = encode(self.salt, url)
        self.parsed_data = urlparse(url)
        if self.encoded_url in hash_dict.keys():
            print(f'URL hash exists in the table! \nParsed data for this URL: \n'
                  f'{hash_dict[self.encoded_url]}')
        else:
            hash_dict[self.encoded_url] = self.parsed_data
            print('New data successfully saved...')


my_url = Url('https://gb.ru/lessons/141727/homework')
my_url2 = Url('https://gb.ru/lessons/141727')
my_url3 = Url('https://gb.ru/lessons/141727')
