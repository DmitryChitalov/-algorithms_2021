"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

url : хеш-url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

import hashlib
import uuid


def url_check(table_cache, url, salt):
    my_hash = hashlib.sha256(url.encode('utf-8') + salt.encode('utf-8'))
    if not table_cache.get(my_hash.hexdigest()):
        table_cache[my_hash.hexdigest()] = url
    return my_hash.hexdigest()


MY_ID = str(uuid.uuid1())
my_table = {}
url_check(my_table, 'mail.ru', MY_ID)
print(my_table)
url_check(my_table, 'ya.ru', MY_ID)
print(my_table)
url_check(my_table, 'mail.ru', MY_ID)
print(my_table)
