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

import hashlib, uuid


def func_url(url):
    if url[:8] == 'https://':
        if kash_url.get(url):
            print(f'Ссылка "{url}" присутствует в кэше.')
        else:
            hash_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
            kash_url[url] = hash_url
    else:
        print(f'Неверный формат ссылки "{url}".')


kash_url = {}
salt = uuid.uuid4().hex
n = 1

func_url('https://ru.wikipedia.org/wiki/')
func_url('https://www.youtube.com/')
func_url('https://ru.wikipedia.org/wiki/')
func_url('https://yandex.ru/')
func_url('test')

for i in kash_url:
    print(f'\n{n}я ссылка - {i}. Кэш ссылки - {kash_url.get(i)}')
    n += 1
