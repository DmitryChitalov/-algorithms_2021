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

from uuid import uuid4
import hashlib

hash_dict = {}


def url_cash_func(hash_dict_f, url_input_f):
    salt = uuid4().hex
    if url_input_f in hash_dict_f.keys():
        return "Данный url-адрес уже есть в кэше "
    else:
        hash_url = hashlib.sha256(salt.encode() + url_input_f.encode()).hexdigest()
        hash_dict_f[url_input_f] = hash_url
    return hash_dict_f


print(url_cash_func(hash_dict, input("Введите url-фдрес ")))
print(url_cash_func(hash_dict, input("Введите url-фдрес ")))
print(url_cash_func(hash_dict, input("Введите url-фдрес ")))
