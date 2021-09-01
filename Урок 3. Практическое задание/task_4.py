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


def check(url):
    salt = 'salt'
    url_hash = sha256((url + salt).encode('utf-8')).hexdigest()
    try:
        if cache[url_hash]:
            return cache[url_hash]
    except KeyError:
        cache[url_hash] = url
        return 'URL added'


cache = {}
t_url = 'https://gb.ru/education'
print(check(t_url))
print(check(t_url))

print(cache)
