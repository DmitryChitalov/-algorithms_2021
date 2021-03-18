"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
from hashlib import sha256
from re import findall

table_url = []


def hash_url(url):
    if findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]))+', url):
        salt = url.split('.')
        url_h = sha256(salt[-2].encode() + url.encode()).hexdigest()

        if len(table_url) == 0:
            table_url.append(url_h)
            return f'Хеш добавлен - {url_h}'
        else:
            for u in table_url:
                if u == url_h:
                    return f'{url} - url-адрес уже есть в хеш-таблице!'
                else:
                    table_url.append(url_h)
                    return f'Хеш добавлен - {url_h}'



    else:
        return f'{url} - неверный url адрес!'


print(hash_url('https://www.chipdip.ru/'))
print(hash_url('https://www.arduino.cc/'))
print(hash_url('https://amperka.ru/'))
print(hash_url('https://www.chipdip.ru/'))
print(hash_url('https/amperka.ru/'))