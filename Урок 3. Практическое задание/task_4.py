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

def func_hash(user_site):
    fig_calc = 0
    while fig_calc != 2:
        salt = user_site[11:]
        hash_code = hashlib.sha256(salt.encode() + user_site.encode()).hexdigest()
        url_for_check = dict_s.get(hash_code)
        if url_for_check is None:
            dict_s[hash_code] = user_site
            print(f'Сайт {user_site} добавлен')
        else:
            print(f'Сайт уже добавлен {url_for_check}')
        fig_calc += 1

dict_s = {}
user_site = 'https://www.mail.ru'
func_hash(user_site)