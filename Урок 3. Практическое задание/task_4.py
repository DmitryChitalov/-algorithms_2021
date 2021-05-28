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

cached_url = {}
salt = uuid4().hex

def cache_check(link):
    if cached_url.get(link):
        print(f'Даная страница находится в кэше.')
    else:
        hash_obj = hashlib.sha256(salt.encode() + link.encode()).hexdigest()
        cached_url[link] = hash_obj

print(cached_url)

cache_check('https://gb.ru/lessons/132193')
cache_check('https://gb.ru/lessons/132193')