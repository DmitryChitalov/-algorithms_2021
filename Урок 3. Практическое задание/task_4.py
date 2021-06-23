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
from uuid import uuid4
from pprint import pprint


class Caching_urls:
    def __init__(self):
        self.hash_table = {}

    def viewing_table(self):
        return self.hash_table

    def clear_table(self):
        return self.hash_table.clear()

    @staticmethod
    def hash_url(url):
        salt = uuid4().hex
        return hashlib.sha256(salt.encode("utf-8") + url.encode("utf-8")).hexdigest()

    def add_table(self, url):
        if self.hash_table.get(url):
            return f"Ваш url: {url}, уже находится в базе!"
        else:
            hash_obj = self.hash_url(url)
            self.hash_table[url] = hash_obj
            return f"Ваш url: {url}, успешно дабавлен в базу!"


if __name__ == '__main__':
    cash_url = Caching_urls()
    print(cash_url.add_table("https://google.com/"))
    print(cash_url.add_table("https://ya.ru/"))
    print(cash_url.add_table("https://gb.ru/"))
    print(cash_url.add_table("https://e1.ru/"))
    print(cash_url.add_table("https://habr.ru/"))
    print(cash_url.add_table("https://mail.ru/"))
    print(cash_url.add_table("https://python-scripts.com/"))
    pprint(cash_url.viewing_table(), width=1)
