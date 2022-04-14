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

from uuid import uuid4
import hashlib


def page_caching(url, cache):
    if url in cache.keys():
        return cache.get(url)[0]
    else:
        salt = uuid4().hex
        url_hash = hashlib.sha1(url.encode(encoding='UTF-8') + salt.encode(encoding='UTF-8')).hexdigest()
        cache[url] = url_hash, salt
        return f'Адрес: {url} добавлен в кэш: {url_hash}'


my_cache = {
    'ya.ru': ('e900769e953b2078ddd90ab3d9a13724c7140aa5', 'fce92afa374a4c2897fdf73f5bd4794a'),
    'rambler.ru': ('d648aa8bd7499898a16b42ebcc1f0e6e25db08c6', '5ef607e17b0843888520de93edc02730'),
    'mail.ru': ('aa4c5ad89940ba25f4331a7460f9a0c5e8d341d1', 'd3872e940f1b4237a9506a889e9d0500'),
    'google.com': ('a3c940cd5dba922281ba5e84c7e3fb152b14ef5b', 'dadb9b24edcc436f83900323defeb6d0')
}

print(page_caching('asd', my_cache))
print('_' * 50)
print(page_caching('ya.ru', my_cache))
print('_' * 50)
print(page_caching('qwerty', my_cache))
print('_' * 50)
print(page_caching('asd', my_cache))
print('_' * 50)
print(page_caching('qwerty', my_cache))
print('*' * 50)

for k, v in my_cache.items():
    print(f'{k}: {v[0]}')


# def calc_hash(url):
#     salt = uuid4().hex
#     url_hash = hashlib.sha1(url.encode(encoding='UTF-8') + salt.encode(encoding='UTF-8')).hexdigest()
#     return url, (url_hash, salt)
#
#
# print(calc_hash('google.com'))

'''
Есть ли необходимость хранить в кэше "соль"? Например если потеряется хеш строки адреса, то для вычислении "соленого"
 хеша, необходимо хранить и саму "соль". Если "соль" хранить не надо, то для чего тогда нужен "соленый" хеш?
 '''