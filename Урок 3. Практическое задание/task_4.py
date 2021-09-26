"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

хеш-url : url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

import hashlib
from uuid import uuid4


# Класс MySession отслеживает данные в хеш-таблице и отвечает за получение результата в рамках сессии

class MySession:

    def __init__(self):
        self.salt = uuid4().hex
        self.cache = {}

    def url_cache(self, url):
        url_hex = hashlib.sha256(url.encode() + self.salt.encode()).hexdigest()
        url_verify = self.cache.get(url_hex)
        if url_verify:
            # получаем сохраненный url
            return f'>> найден в кэше - {url} ({url_hex})'
        else:
            # если не нашли, то добавляем в словарь
            self.cache[url_hex] = url
            return f'добавлен в кэш - {url}'


# ----- Проверка результата:
work = MySession()  # создается сессия (имеет свою 'соль')

history_url = ['https://www.rbc.ru/',
               'https://www.yandex.ru/',
               'https://www.mail.ru/',
               'https://www.google.com/',
               'https://www.habr.ru/',
               'https://gb.ru/',
               'https://www.yandex.ru/',  # добавлен повтор сразу
               'https://www.python.org/']

# Добавляем данные:
print('-'*10, '1. Добавляем первый раз данные')
# 1. Добавляем данные в кэш
for url in history_url:
    print(work.url_cache(url))

print('-'*10, 'Содержимое кэша:')
#  Выведем содержимое кеша после добавления
for key, url in work.cache.items():
    print(key, url)

# 2. Повторно пробуем добавить данные в кэш
print('\n\n')
print('-'*10, '2. Добавляем второй раз данные')
# 3. Пробуем еще раз проверить url
for url in history_url:
    print(work.url_cache(url))
print('-'*10, 'Содержимое кэша:')
# 4. Выведем еще раз, чтобы убедиться, что измененй не произошло
for key, url in work.cache.items():
    print(key, url)
