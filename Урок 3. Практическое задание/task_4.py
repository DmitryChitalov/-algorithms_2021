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

cache = {}


def url_cache(url, cashe):
    flag = False
    res = ""
    if not len(cashe):
        salt = "key0"
        res = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
        cache[res] = url

    for i in range(len(cashe)):
        salt = "key" + str(i)
        res = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
        if cashe.get(res):
            break
        else:
            flag = True
    if flag:
        cache[res] = url


url_cache("geek.ru", cache)
url_cache("yandex.ru", cache)
url_cache("geek.ru", cache)
url_cache("yandex.ru", cache)
url_cache("mail.ru", cache)
print(cache)
