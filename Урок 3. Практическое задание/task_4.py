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
import re
import hashlib
dict_url = {}


def cash_url(url):
    patern = re.compile(r'([a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,9})')
    if dict_url.get(url) is None:
        salt = patern.search(url).group(1)
        hash_url = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
        dict_url[url] = {hash_url}
    else:
        print(f'Адрес: {url} уже находится в кэше')


cash_url('https://zen.yandex.ru/media/')
cash_url('https://gb.ru/lessons/158162')
cash_url('https://zen.yandex.ru/media/picture')
cash_url('https://zen.yandex.ru/media/')
print(dict_url)

