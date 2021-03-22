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

url_cash = dict()


def cash_in(url: str):
    if url_cash.get(url):
        print(f"{url} присутствует в кэше")
    else:
        url_cash[url] = hashlib.sha256(url.encode('utf-8') + url.split('.')[-2].encode('utf-8')).hexdigest()


cash_in('https://yandex.ru')
cash_in('https://www.linux.org')
cash_in('https://yandex.ru')

print(url_cash)
