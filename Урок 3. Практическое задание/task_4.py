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

salt = uuid4().hex
cash_dict = {}


def cash_url(url: str):
    hash_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if hash_url in cash_dict:
        print(f"URL {url} уже закэширован")
    else:
        cash_dict[hash_url] = url
        print(f"URL {url} занесен в кэш")


cash_url("www.google.com")
cash_url("www.google.com")
cash_url("www.google.ru")

for k, v in cash_dict.items():
    print(v, k)
