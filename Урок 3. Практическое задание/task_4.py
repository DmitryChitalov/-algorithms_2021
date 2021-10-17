"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

url : хеш-url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
import hashlib

cash = dict()
SALT = 'salt'.encode('UTF-8')


def fill_url_cash(url):
    hash_obj = hashlib.sha256(str(url).encode('UTF-8') + SALT)
    hash_url = hash_obj.hexdigest()
    return cash.setdefault(url, hash_url)


def check_url_cash(url):
    hash_obj = hashlib.sha256(str(url).encode('UTF-8') + SALT)
    hash_url = hash_obj.hexdigest()
    if url not in cash:
        return cash.setdefault(url, hash_url)


print(fill_url_cash('geekbrains.ru'))
print(fill_url_cash('yandex.ru'))
print(fill_url_cash('mail.ru'))
print(fill_url_cash('google.com'))
print(fill_url_cash('kinopoisk.ru'))
print(cash)
print(check_url_cash('geekbrains.ru'))
print(check_url_cash('rambler.ru'))
print(cash)

