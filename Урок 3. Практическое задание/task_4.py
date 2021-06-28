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

from uuid import uuid4
import hashlib

salt = uuid4().hex
website_in_hash = dict()

def website(url):
    if not website_in_hash.get(url):
        website_in_hash[url] = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        print(f"Страница {url} успешно добавлена")
    else:
        print(f"В кеше страница {url} уже присутствует")

website('https://gb.ru/')
website('https://www.google.com/')
website('https://gb.ru/')


