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
import uuid


def func_url_check(url, bd={}, salt=uuid.uuid4().hex):
    if url in bd.keys():
        print(f'{url} есть в базе данных')
    else:
        hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        bd.update({url: hash})
        print(f'{url} добавлен в базу данных')


func_url_check('https://yandex.ru/')
func_url_check('https://google.com/')
func_url_check('https://www.drive2.ru/')
func_url_check('https://www.drive2.ru/')
