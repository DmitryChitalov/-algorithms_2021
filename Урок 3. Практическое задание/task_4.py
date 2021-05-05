from hashlib import sha256
from uuid import uuid4

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


class Webcash:
    def __init__(self):
        self.dict_url = {}

    def salt(self):
        return uuid4().hex

    def hashing_url(self, url, salt):
        return sha256(url.encode() + salt.encode()).hexdigest()

    def add_url(self, add_url):
        salt = self.salt()
        self.dict_url[add_url] = [self.hashing_url(add_url, salt), salt]


if __name__ == '__main__':
    urls = Webcash()
    while True:
        usr_url = input('Enter URL (or "0" to exit): \n')
        if usr_url == '0':
            print(f'Exit')
            break
        if usr_url in urls.dict_url:
            print(f'URL {usr_url} is already in cache\n')
        else:
            urls.add_url(usr_url)
            print(f'URL {usr_url} added.\n')
