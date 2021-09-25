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
from pprint import pprint


class CacheURL:
    def __init__(self):
        self.cache = dict()

    def throw_url(self, url) -> tuple:
        is_cached = False
        tmp = hash(url)
        if not tmp in self.cache:
            self.cache[tmp] = url
            is_cached = True
        return (self.cache[tmp], 'added to cache' if is_cached else 'already in cache')

    def print_cache(self):
        pprint(self.cache)


if __name__ == '__main__':
    request = CacheURL()
    print('Site {} {}'.format(*request.throw_url('address1')))
    print('Site {} {}'.format(*request.throw_url('address2')))
    print('Site {} {}'.format(*request.throw_url('address1')))
    print('Site {} {}'.format(*request.throw_url('address2')))
    request.print_cache()

'''
Site address1 added to cache
Site address2 added to cache
Site address1 already in cache
Site address2 already in cache
{-3721402707588848217: 'address1', 1960924240048146215: 'address2'}
'''
