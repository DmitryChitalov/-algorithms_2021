"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


from hashlib import sha256
from uuid import uuid4

salt = uuid4().hex
urls = {}


def my_urls(url):
    if urls.get(url):
        print(f'Адрес: {url} уже в кэше.')
    else:
        res = sha256(salt.encode() + url.encode()).hexdigest()
        urls[url] = res


my_urls('https://gb.ru/lessons/150346/homework')
my_urls('https://gb.ru/lessons/150346/homework')
print(urls)
my_urls('https://gb.ru')
print(urls)
my_urls('https://gb.ru')
