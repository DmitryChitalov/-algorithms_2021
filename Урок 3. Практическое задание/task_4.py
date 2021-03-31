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

url_lists = {}
salt = uuid4().hex


def save_url(url):
    salted_minced_meat = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if url_lists.get(url):
        print(f'Адрес уже есть в кэше {url}')
    else:
        url_lists[url] = salted_minced_meat
        print(f'Сохраняем в кэш: {url} ')


save_url('https://geekbrains.ru/')
save_url('https://ru.wikipedia.org/wiki/')


print(f'Уже в кэше {url_lists}')