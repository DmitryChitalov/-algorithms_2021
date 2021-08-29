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
import json


def exist_or_not(url):
    """
    Функия выводит адрес сайте если он есть в кэше,
    если нет, то заносит хеш и адрес сайта в базу
    """
    salt = url[:int(len(url) / 2)]
    url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    try:
        with open('urls.json') as file:
            urls = json.load(file)
            if urls.get(url_hash):
                print(url)
            else:
                urls[url_hash] = url
                with open('urls.json', 'w') as file_w:
                    json.dump(urls, file_w)
    except FileNotFoundError:
        with open('urls.json', 'w') as file_w:
            json.dump({url_hash: url}, file_w)


exist_or_not('google.com')
