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

import uuid


class HashURL:
    def __init__(self):
        self.url_dict = {}
        self.salt = uuid.uuid4().hex

    def add_url(self, new_url):
        self.url_dict[hash(self.salt + new_url)] = new_url

    def check_url(self, new_url):
        if not self.url_dict.get(hash(self.salt + new_url)):
            self.add_url(new_url)

    def __str__(self):
        return str(self.url_dict)


my_hash = HashURL()
my_hash.check_url('http://www.gazeta.ru')
my_hash.check_url('http://www.lenta.ru')
my_hash.check_url('http://www.gazeta.ru')
my_hash.check_url('http://www.pythonworld.ru')
my_hash.check_url('http://www.yandex.ru')
my_hash.check_url('http://www.python.org')
my_hash.check_url('http://www.gb.ru')
my_hash.check_url('http://www.yandex.ru')
print(my_hash)
