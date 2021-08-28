"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
import hashlib
import requests

dict_of_url = dict()


def url(address: str):
    salt = b'Hello world'
    hash_url = hashlib.sha256(salt + address.encode()).hexdigest()
    if hash_url in dict_of_url:
        print('Ссылка находится в кэше')
    else:
        dict_of_url[hash_url] = requests.get(address)


url_1 = ' https://pythonworld.ru/osnovy/dekoratory.html'
url_2 = 'https://pavel-karateev.gitbook.io/intermediate-python/sintaksis/args_and_kwargs'
url(url_1)
url(url_2)
url(url_1)
print(dict_of_url)
