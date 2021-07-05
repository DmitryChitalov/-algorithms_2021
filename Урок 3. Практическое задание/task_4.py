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
cached_url = {}


def get_page(url):
    if cached_url.get(url):
        print(f'Сайт {url} уже в кэше')
    else:
        cash = sha256(salt.encode() + url.encode()).hexdigest()
        cached_url[url] = cash
        print(f'Сайт {url} добавлен в кэш')


get_page('vk.com')
get_page('google.сom')
get_page('mail.ru')
get_page('mail.ru')
print(cached_url)
