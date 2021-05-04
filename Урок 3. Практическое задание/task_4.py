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
import re

URLS = {}


def input_url():
    url = input('введите url, для выхода введите exit\n')
    if url == 'exit':
        exit()
    return url


def cash_urls(url):
    schema_match = re.match('^http.?://(.+)', url)
    if schema_match:
        url_ = schema_match.group(1)
    else:
        url_ = url
    hashed_url = hashlib.sha256(str(len(url_)).encode() + url_.encode()).hexdigest()
    if hashed_url not in URLS:
        URLS[hashed_url] = url_
        print(f'cashed new url {url_}')


if __name__ == '__main__':
    while True:
        url = input_url()
        cash_urls(url)
