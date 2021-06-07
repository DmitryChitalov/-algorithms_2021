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
import requests
import hashlib
from uuid import uuid4

URL = 'https://www.avito.ru'
URL1 = 'https://www.google.com'

def get_url(url):
    try:
        response = requests.get(url)
        return response.status_code
    except ConnectionError:
        return requests.exceptions.ConnectionError

salt = uuid4().hex
cash_url = {}

def get_page(url):
    if cash_url.get(url):
        return f'Адрес присутствует в кэше'
    else:
        if get_url(url) == 200:
            data = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
            cash_url[url] = data
            return cash_url
        else:
            return f'Адрес недоступен'

print(get_page(URL))
print(get_page(URL1))

print(get_page(URL))
print(get_page(URL1))
