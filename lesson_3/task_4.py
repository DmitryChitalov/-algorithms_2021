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
from hashlib import sha256


def url_check(url):
    salt = 'salt123'
    hash_url = sha256((url + salt).encode('utf-8')).hexdigest()
    try:
        if cache[hash_url]:
            return cache[hash_url]
    except KeyError:
        cache[hash_url] = url
        return 'url добавлен в кэш'


if __name__ == '__main__':
    cache = {}
    test_url = 'https://gb.ru/education'
    print(url_check(test_url))
    print(url_check(test_url))
