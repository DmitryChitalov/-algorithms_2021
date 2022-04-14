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
import uuid
import hashlib


cache = {}
salt = uuid.uuid4().hex


def check_page(url):
    if cache.get(url):
        print(f'Адрес {url} есть в кэше')
    else:
        cache.update({url: hashlib.sha256(salt.encode() + url.encode()).hexdigest()})
        print(f'Адрес {url} добавлен в кэш')
        print(cache)

check_page('https://gb.ru')
check_page('https://gb.ru')
check_page('https://vk.com')
check_page('https://vk.com')
check_page('https://cat-houses.ru')