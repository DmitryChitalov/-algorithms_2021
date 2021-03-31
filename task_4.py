"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
import uuid
import hashlib


cash = {'https://mail.ru/': '030208b9ce194621c68bff9f9d2b7b94b07ba182611ff2ebfb5ed22cd6e0ab00'}


def check(url):
    salt = uuid.uuid4().hex
    total = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if cash.get(url):
        print('дданый адрес находится в кэше ', url)
    else:
        cash [url] = total
        print('данный адрес был добавлен в кэш', url)

check('https://mail.ru/')
check('https://yandex.ru/')
print(cash)