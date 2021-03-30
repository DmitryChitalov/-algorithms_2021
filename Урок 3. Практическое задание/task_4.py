"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

import hashlib
from uuid import uuid4

repository = {}
salt = uuid4().hex


def url_save(url):
    salted_minced_meat = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if repository.get(url):
        print(f'Адрес уже есть в кэше {url}')
    else:
        repository[url] = salted_minced_meat
        print(f'Сохраняем в кэш: {url} ')


url_save('https://geekbrains.ru/')
url_save('https://www.youtube.com/')
url_save('https://geekbrains.ru/')
url_save('https://www.google.ru/')

print(f'Уже в кэше {repository}')
