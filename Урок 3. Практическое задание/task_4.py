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

bd_url = {}


def url_hash(url):
    salt = "salt"
    url_h = sha256(salt.encode() + url.encode()).hexdigest()
    if url_h not in bd_url.values():
        bd_url[url_h] = url_h
        return f'Хеш добавлен - {url_h}'
    else:
        return f'{url} - url-адрес уже есть в хеш-таблице!'


print(url_hash("https://github.com/"))
print(url_hash("https://dev.mysql.com/"))
print(url_hash("https://github.com/"))
