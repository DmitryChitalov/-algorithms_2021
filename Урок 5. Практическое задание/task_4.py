"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from random import choice
from timeit import default_timer
import string

d = dict()
od = OrderedDict()

dict_elements, len_word = 10, 6
NUMBER = 1000000

# формируем ключи и значения для последующей работы по образцу 'wkcydl':6
values = [k for k in range(dict_elements)]
keys = [''.join(choice(string.ascii_lowercase) for x in range(len_word)) for v in values]


def measure(cnt):
    def time_it(func):
        def wrapper():
            start = default_timer()
            for i in range(cnt):
                func()
            runtime = default_timer() - start
            print(f'{func.__name__:<15s} {runtime:10.5f}')

        return wrapper

    return time_it

@measure(NUMBER)
def fill_dict():
    for idx in range(len(keys)):
        d[keys[idx]] = values[idx]
    # return dict(zip(keys, values)) # этот вариант не берем ибо это приведение типов


@measure(NUMBER)
def get_dict():
    while d:
        d.popitem()


@measure(NUMBER)
def fill_ordereddict():
    for idx in range(len(keys)):
        od[keys[idx]] = values[idx]


@measure(NUMBER)
def get_ordereddict():
    while od:
        od.popitem()


if __name__ == '__main__':
    fill_dict()
    get_dict()
    fill_ordereddict()
    get_ordereddict()

'''
fill_dict          3.23162
get_dict           0.22422
fill_ordereddict    3.67950
get_ordereddict    0.22341

вывод:
1. скорость одинаковая
2. лаконичности не прибавилось
3. применять следует только для целей обратной совместимости с версией притона до 3.6

'''
