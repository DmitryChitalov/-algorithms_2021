"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

import hashlib

t_cash = {}


class My_Cashe:
    def __init__(self):
        self.salt = 'druska'

    def get_hash(self, url):
        hash_obj = hashlib.sha256(url.encode() + self.salt.encode()).hexdigest()
        r = t_cash.get(hash_obj)
        if not r:
            t_cash[hash_obj] = url
            print('Добавлено в хеш-таблицу')
        else:
            print('Найдено в хеш-таблице')


cash = My_Cashe()
cash.get_hash('https://www.kika.lt/katalogas/katems/draskykles-ir-stovai/?&page=2')
cash.get_hash('https://www.kika.lt/katalogas/katems/draskykles-ir-stovai/?&page=2')
