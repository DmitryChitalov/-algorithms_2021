"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

url : хеш-url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
import hashlib
from uuid import uuid4

url = 'https://yandex.ru/search/?from=chromesearch&clid=2242348&text=%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%' \
      'D0%B4%D1%87%D0%B8%D0%BA&lr=38'


class Hashurl:
    dict_hash = {}

    def __init__(self, url):
        salt = uuid4().hex
        hash_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        if url in self.dict_hash:
            print(f'Такой url уже есть в списке: {self.dict_hash[url]}')
        else:
            self.dict_hash[url] = hash_url
            print('url записан.')


q = Hashurl(url)  # url записан.
print(q.dict_hash)

a = Hashurl(url)  # Такой url уже есть в списке: 97dc8df1619ff83fc850ea13538743986ba9977128bf7d36dcca1eae51281e36
url = 'https://yandex.ru/search/?esearch&clid=2242348&text=%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%' \
      'D0%B4%D1%87%D0%B8%D0%BA&lr=38'
a = Hashurl(url)
print(q.dict_hash)