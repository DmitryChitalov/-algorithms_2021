"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""


from uuid import uuid4
from hashlib import sha256


salt = uuid4().hex
url_cash = {}


def base_url(url):
    if not url_cash.get(url):
        url_cash[url] = sha256(salt.encode() + url.encode()).hexdigest()
        return f"Cash:\n" \
               f"{url_cash}"
    else:
        return f"Website {url} available in the cache"


while True:
    usr_url = input("Enter website. To exit, type 'flugergehaimer': ")
    if usr_url == "flugergehaimer":
        print("By")
        break
    else:
        print(base_url(usr_url))
