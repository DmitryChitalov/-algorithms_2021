"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
from hashlib import sha256


class UrlHash:
    def __init__(self, salt):
        self.hash_table = {}
        self.salt = salt

    def hash_add(self, user_url):
        hash_url = sha256(user_url.encode() + self.salt.encode()).hexdigest()
        if hash_url not in self.hash_table:
            self.hash_table[hash_url] = user_url
            print('Адрес добавлен в кэш: ')
        else:
            print('Введенный адрес находится в кэше: ')


my_hash = UrlHash('salt')

user_url = None
while user_url != 'q':
    user_url = input('Введите url-адрес, чтобы добавить его в кэш (Для выхода введите "q"): ')
    my_hash.hash_add(user_url)
    print(my_hash.hash_table)
