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

from uuid import uuid4
import hashlib


class My_hash_url:
    def __init__(self):
        self.dict_hash = {}
        self.__salt = uuid4().hex

    def pull_hash(self, url):
        url_hash = hashlib.sha3_256(self.__salt.encode() + url.encode()).hexdigest()
        if url not in self.dict_hash:
            self.dict_hash[url] = url_hash
            print('Url добавлен в хеш')
        else:
            print('Данный url уже присутствует.')


obj = My_hash_url()
obj.pull_hash('https://gb.ru/')
obj.pull_hash('https://gb.ru/')
obj.pull_hash('https://www.google.ru/')
print(obj.dict_hash)










