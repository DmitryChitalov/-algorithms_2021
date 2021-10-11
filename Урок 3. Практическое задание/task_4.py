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

cache = {}


def url_hash(url):
    if not (url in cache.keys()):
        cache[url] = hashlib.sha256('salt'.encode() + url.encode()).hexdigest()
    return cache[url]


print(cache)
url_hash('http://youtube.com')
print(cache)
url_hash('http://gmail.com')
print(cache)
url_hash('http://youtube.com')
print(cache)
