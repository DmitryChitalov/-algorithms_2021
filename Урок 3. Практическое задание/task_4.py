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


class CashUrl():
    def __init__(self):
        self.repository = {}

    def __str__(self):
        return '\n'.join(self.repository.keys())

    @staticmethod
    def _hash_url_(string):
        salt = 'salt'
        return hashlib.sha256(string.encode() + salt.encode()).hexdigest()

    def new_url(self, url):
        hash_url = self._hash_url_(url)
        if hash_url not in self.repository:
            self.repository[hash_url] = url


if __name__ == '__main__':
    my_url = CashUrl()
    my_url.new_url('https://gb.ru/lessons/145450')
    my_url.new_url('https://gb.ru/lessons/145450')
    my_url.new_url('https://gb.ru/lessons/145451')
    print(my_url)

