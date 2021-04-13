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

cache = dict()


def cache_func(url):
    salt = 'secret'
    url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if url_hash in cache:
        return f'Данный {url} адрес не добавлен, уже находится в таблице'
    else:
        cache[url_hash] = url
        return f'Данный {url} адрес добавлен  в таблице '


print(cache_func('https://gb.ru/lessons/124995'))
print(cache_func('https://gb.ru/lessons/124994'))
print(cache_func('https://gb.ru/lessons/124993'))
print(cache_func('https://gb.ru/lessons/124995'))
