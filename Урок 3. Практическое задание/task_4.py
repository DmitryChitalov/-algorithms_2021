"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

from uuid import uuid4
import hashlib

salt = uuid4().hex
web_hash = {}


def url_website(url):
    if not web_hash.get(url):
        web_hash[url] = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        print(f"Страница {url} успешно добавлена. Хеш : {web_hash[url]}")
    else:
        print(f"Такая страница в кеше уже присутствует {url}")


url_website('https://ru.tradingview.com/')
url_website('https://wpcalc.com/')
url_website('https://www.citilink.ru/')
url_website('https://wpcalc.com/')