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
from uuid import uuid4

salt = uuid4().hex
# print(salt)
cache_storage = {}

def get_page(url):

    if cache_storage.get(url):
        print(f'Страница с адресом {url} есть в кэше')
        print('-' * 20)
    else:
        resust_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_storage[url] = resust_hash
        print(resust_hash)
        print(f'Адрес {url} добавлен в кэш')
        print('-' * 20)


get_page('https://geekbrains.ru/')
get_page('https://yandex.ru/')
get_page('https://vk.com/')
get_page('https://geekbrains.ru/')
get_page('https://yandex.ru/')
get_page('https://vk.com/')

for key, value in cache_storage.items():
    print(key, ":", value)

