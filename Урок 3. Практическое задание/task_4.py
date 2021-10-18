"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

import hashlib
from uuid import uuid4

obj_cash = {}


def url_get(url_page):
    if obj_cash.get(url_page):
        print("Этот адрес ", url_page, " уже есть в кеше", sep='')
    else:
        result = hashlib.sha256(uuid4().hex.encode() + url_page.encode()).hexdigest()
        print('Имя страницы: ', url_page, '\n', 'Хеш URL: ', result, sep='')
        obj_cash[url_page] = result    # присвоим в переменную, хотя и негде не сохраним :)


url_get('https://yandex.ru')
