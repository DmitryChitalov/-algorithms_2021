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
url_list = ['https://music.yandex.ru','https://www.youtube.com','https://geekbrains.ru','https://habr.com',
            'https://askdev.ru'] # -> Просто список заранее заготовленных url адресов

bd = {'hash':[]} # -> условная БД, которая хранит значения хэшей


def hash_url(web_url,bd):
    salt = '1000' # -> Соль.
    hash_url = hashlib.sha256(web_url.encode(encoding="utf-8")+salt.encode()).hexdigest()
    if hash_url in bd['hash']:
        print('Страница была добавлена ранее')
        return bd
    bd['hash'].append(hash_url)
    print(f'Страница {web_url} добавлена в базу данных')
    return bd

for i in url_list:
    hash_url(i,bd)

for i in url_list:
    hash_url(i,bd)

