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

    def add_to_hash(self, url):
        hashed_url = sha256(url.encode() + self.salt.encode()).hexdigest()
        if hashed_url not in self.hash_table:
            self.hash_table[hashed_url] = url
            print('Адрес успешно добавлен в кэш:')
        else:
            print('Введенный адрес уже в кэше:')


my_hash = UrlHash('pepper')

user_url = None
while user_url != 'q':
    user_url = input('Введите url-адрес, чтобы добавить его в кэш (если хотите выйти, введите "q"): ')
    if user_url != 'q':
        my_hash.add_to_hash(user_url)
        print(my_hash.hash_table)
