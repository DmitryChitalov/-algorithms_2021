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
from hashlib import sha256

salt = uuid4().hex
hash_table = dict()


def check_cash(url):
    if url in hash_table.keys():
        print('url был внесён в кэш ранее')
    else:
        hash_url = (sha256((url.encode()) + salt.encode())).hexdigest()
        hash_table[url] = hash_url


check_cash('https://mail.ru/')
check_cash('https://mail.ru/')
check_cash('https://gb.ru/')
