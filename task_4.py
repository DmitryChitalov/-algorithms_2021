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
import hashlib
from uuid import uuid4

cash_dict = {}
salt = uuid4().hex


def cashing_web(url):
    url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if url in cash_dict:
        print(f"url-адрес {url} уже есть в кэше")
    else:
        cash_dict.update({url: url_hash})
        print(f'url-адрес {url} хэш {url_hash} сохранен')


list_url = ['https://cbr.ru/', 'https://www.google.ru/', 'https://www.google.ru/',
            'https://yandex.ru/', 'https://www.facebook.com/', 'https://cbr.ru/',
            'https://www.google.ru/', 'https://www.google.ru/', 'https://yandex.ru/']
for i in list_url:
    cashing_web(i)

print(cash_dict)
