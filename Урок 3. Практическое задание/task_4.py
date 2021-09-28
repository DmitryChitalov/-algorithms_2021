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

from random import randint as ran
import hashlib


class Url:

    def __init__(self):
        self.set_x = set()
        self.salt = ran(1, 1000000)
        self.dict_x = dict()

    def func_add(self, x):
        self.set_x.add(self.func_hash(x))

    def func_hash(self, x):
        return hashlib.sha256(x.encode() + str(self.salt).encode()).hexdigest()

    def func_verifications(self, x):
        if self.func_hash(x) not in self.set_x:
            self.func_add(x)
            self.dict_x[self.func_hash(x)] = x
        else:
            print('Уже есть данный url.')


if __name__ == '__main__':
    obj = Url()
    obj.func_verifications(r'https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html')
    obj.func_verifications(r'https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html')
    print(obj.dict_x)
