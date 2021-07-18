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


# ничего не сказано о Memcached, о условиях использования, поэтому сделал вывод, что требуется только проверка хэша.
# Понятно, что фунция полноценного кэширования, написанная заново, будет иной


def cache_checker(url, my_cash):
    if url in my_cash.keys():
        print(my_cash[url])
    else:
        req = requests.get(url)
        salt = uuid4().hex
        cash[url] = [hashlib.sha256(req.content + salt.encode()), salt]


if __name__ == '__main__':
    import requests
    from uuid import uuid4
    import hashlib

    cash = {}
    links = ['https://gb.ru/', 'https://www.udemy.com', 'https://javarush.ru/']
    for i in links:
        print(cache_checker(i, cash))

    links_2 = ['https://payeer.com', 'https://www.udemy.com', 'https://www1.oanda.com/']
    for i in links_2:
        print(cache_checker(i, cash))
