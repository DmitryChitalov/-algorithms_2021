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
import hashlib
import pickle


def hash_url(url):
    """
    Получение хеша адреса сайта
    :param url: адресс сайта
    :return: хеш адреса сайта
    """
    sal = 'qwerty'
    return hashlib.sha1(url.encode() + sal.encode()).hexdigest()


def get_article_from_server(url):
    print('Получение статьи с сервера ...')
    response = requests.get(url)
    return response.text


def get_article(url):
    """
    Проверка наличия кеша на адрес url

    :param url: адрес сайта
    :return: страница сайта
    """
    print('Получение статьи ...')
    hashed_url = hash_url(url)
    if hashed_url not in cache:
        cache[hashed_url] = get_article_from_server(url)
        with open('cache.pickle', 'wb') as f:  # Сохранение словаря в файле
            pickle.dump(cache, f)
    else:
        print('Получение из кэша...')
    return cache[hashed_url]


with open('cache.pickle', 'rb') as f:
    cache = pickle.load(f)
url = input('Введите URL сайта: ')
get_article('http://' + url)
get_article('http://' + url)
