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
import hashlib

m = 'vk.com'
cache = {}


def page_caching(site):
    salt = '9f7ca7161a8e45908faaef224089d445'
    hash_site = hashlib.sha256(site.encode()+salt.encode()).hexdigest()
    if cache.get(hash_site):
        return cache[hash_site]
    else:
        cache[hash_site] = cache.get(hash_site, site)
        return site


print(page_caching(m))
print(page_caching(m))
