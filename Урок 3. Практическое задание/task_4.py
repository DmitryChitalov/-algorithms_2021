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


def caching(url, cach):
    salt = url
    hash_obj = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
    if not cach.get(url):
        cach[url] = hash_obj


cach = dict()
caching('https://pythonworld.ru/tipy-dannyx-v-python', cach)
caching('https://vk.com/im?peers=447085295_393951679_c76', cach)
caching('https://pythonworld.ru/tipy-dannyx-v-python', cach)
print(cach)
