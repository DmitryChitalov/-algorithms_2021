"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

хеш-url : url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
import hashlib
from uuid import uuid4

salt = uuid4().hex
cache_url = {}


def cache_page(url):
    if cache_url.get(url):
        print(f'Адрес: {url} есть в кэше')
    else:
        cache_url[url] = hashlib.sha256(salt.encode() +
                                        url.encode()).hexdigest()
        print(cache_url)


cache_page('https://yandex.ru')
cache_page('https://yandex.ru')
cache_page('https://yahoo.ru')
