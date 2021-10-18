"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш
url: хеш-url
Подсказка: задача решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.
Задание творческое. Здесь нет жестких требований к выполнению.
"""
import hashlib
from uuid import uuid4

salt = uuid4().hex
word_storage = {}


def checking_hash(site_page):
    if len(word_storage) == 0:
        hash_sp = hashlib.sha256(salt.encode() + site_page.encode()).hexdigest()
        word_storage[site_page] = hash_sp
        return print({site_page: hash_sp})
    else:
        print('В хеше уже имеется данная страница')


checking_hash('https://geekbrains.ru/')
checking_hash('https://geekbrains.ru/')

