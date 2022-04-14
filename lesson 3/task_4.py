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

import hashlib

salt = 'my salt'
url_dict = dict()
def cash_url(url):
    has_url = hashlib.sha256(salt.encode('utf-8') + url.encode('utf-8')).hexdigest()
    if url not in url_dict:
        url_dict[url] = has_url

url_1 = 'https://gb.ru/lessons/150238'
url_2 = 'https://gb.ru/lessons/150238/homework'
url_3 = 'https://github.com/DmitryChitalov/-algorithms_2021'
url_4 = 'https://gb.ru/lessons/150238/homework'

cash_url(url_1)
cash_url(url_2)
cash_url(url_3)
cash_url(url_4)
print(url_dict)