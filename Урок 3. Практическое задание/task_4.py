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
url_dict = {}

def check_url(url):
    hash_url = hashlib.sha3_256(salt.encode() + url.encode()).hexdigest()
    if hash_url in url_dict:
        print(f'{url} in cash')
    else:
        url_dict.update({hash_url: url})
        print(f'{url} Not in cash. Add.')

check_url('http://google.com')
check_url('http://www.yandex.ru')
check_url('http://gb.ru')
check_url('http://google.com')
check_url('http://gb.ru')
