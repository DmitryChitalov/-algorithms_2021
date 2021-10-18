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
cache_dict = {}
def url_hash(url):
    if url in cache_dict.keys():
        print(cache_dict.get(url))
        print('Есть в кэше')
    else:
        salt = uuid4().hex
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        print(res)
        cache_dict[url] = res


url_hash('https://www.google.com/')
url_hash('https://www.google.com/')

