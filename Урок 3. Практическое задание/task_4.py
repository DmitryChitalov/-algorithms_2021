"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

import requests
import uuid
import hashlib

# Для реализация хеш-таблицы используем словарь
cache = dict()

salt = uuid.uuid4().hex  #  получаем соль, которую будем использовать в сеансе

def write_to_cache(url, text):
    print("Записываем в кэш")
    key = hashlib.sha256(salt.encode() + url.encode()).hexdigest() + ':' + salt
    cache[key] = text

def check_in_cache(url):
    print("Проверяем наличие в кэше")
    key = hashlib.sha256(salt.encode() + url.encode()).hexdigest() + ':' + salt
    return key in cache

def get_article_from_server(url):
    print("Получаем статью с сервера")
    response = requests.get(url)
    return response.text

def get_article(url):
    if not check_in_cache(url):
        write_to_cache(url, get_article_from_server(url))
        print("Записали статью в кэш")
    else:
        print("Получаем статью из кэша")


get_article("https://proglib.io/p/keshirovanie-v-python-algoritm-lru-2020-11-17")
get_article("https://proglib.io/p/keshirovanie-v-python-algoritm-lru-2020-11-17")