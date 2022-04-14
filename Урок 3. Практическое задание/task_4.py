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


def caching(url):
    if url in cache:
        print(f'Сайт "{url}" есть в кэше')
    else:
        cache[url] = hashing(url)


def hashing(url):
    salt = url.split('.')
    res = hashlib.sha256(salt[-1].encode() + url.encode()).hexdigest()
    return res


caching('youtube.com')
caching('google.com')
caching('yandex.ru')
caching('youtube.ru')
caching('google.com')
caching('yandex.ru')
caching('https://gb.ru/lessons/165909')
caching('https://gb.ru/lessons/165900')
caching('https://gb.ru/lessons/165909')
