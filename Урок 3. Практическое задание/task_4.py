"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

url : хеш-url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
from hashlib import sha256
from uuid import uuid4


class UrlControl:
    def __init__(self):
        self.table_url = {}
        self.salt = uuid4().hex

    def add_url(self, url):
        if sha256(url.encode() + self.salt.encode()).hexdigest() in self.table_url.values():
            print(f'URL {url} уже есть в кэше')
        else:
            self.table_url[url] = sha256(url.encode() + self.salt.encode()).hexdigest()

    def __str__(self):
        str_hash = ""
        len_hash = max(map(len, self.table_url.keys()))
        for ind in self.table_url.keys():
            str_hash += f'|{ind}{" " * (len_hash - len(ind) + 1)}|\t{self.table_url[ind]}\n'
        return str_hash


hash_table = UrlControl()
hash_table.add_url('https://google.com/')
hash_table.add_url('https://geekbrains.ru/')
hash_table.add_url('https://www.jetbrains.com/')
hash_table.add_url('https://www.jetbrains.com/')
print(hash_table)
