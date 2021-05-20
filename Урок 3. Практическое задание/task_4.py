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
import json
from uuid import uuid4
with open('cache.json', 'w', encoding='UTF-8') as file:
    cache_dict = {}
    json.dump(cache_dict, file)

def check_url_in_cache(url):
    with open('cache.json', 'r', encoding='UTF-8') as file:
        cache_dict = json.load(file)

    if cache_dict.get(url):
        print(f'Страница {url} уже сохранена в кэш ранее!')
    else:
        phrase = 'new url'
        salt = uuid4().hex
        hash_obj = hashlib.sha256(phrase.encode('UTF-8') + salt.encode('UTF-8') + url.encode('UTF-8'))
        cache_dict[url] = hash_obj.hexdigest()

        with open('cache.json', 'w', encoding='UTF-8') as file:
            json.dump(cache_dict, file)
        print(f'Страница {url} добавлена в кэш.')


if __name__ == '__main__':
    check_url_in_cache('https://www.google.com')
    check_url_in_cache('https://www.youtube.com')
    check_url_in_cache('https://www.google.com')

