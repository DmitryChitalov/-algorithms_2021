"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым из них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

import collections
from timeit import timeit

def collection_dict():
    return collections.OrderedDict([(el, el*2) for el in range(100)])

def classical_dict():
    return {el: el*2 for el in range(100)}

def get_dict(dct, key):
    return dct[key]

print('ЗАПОЛНЕНИЕ СЛОВАРЯ')
print('collection_dict => ', timeit(f'collection_dict()', globals=globals(), number=10000))
print('classical_dict  => ', timeit(f'classical_dict()', globals=globals(), number=10000))
print('ПОЛУЧЕНИЕ ЭЛЕМЕНТА СЛОВАРЯ')
print('get_collection_dict => ', timeit(f'get_dict(collection_dict(), 10)', globals=globals(), number=10000))
print('get_classical_dict  => ', timeit(f'get_dict(classical_dict(), 10)', globals=globals(), number=10000))

'''
    Проведенные измерения времени заполнения словаря и получения элемента словаря показывают что обычный словарь
в 4 раза быстрее осуществляет данные операции чем OrderedDict.
    ЗАПОЛНЕНИЕ СЛОВАРЯ
    collection_dict =>  0.4274766
    classical_dict  =>  0.16615379999999996
    ПОЛУЧЕНИЕ ЭЛЕМЕНТА СЛОВАРЯ
    get_collection_dict =>  0.4149348999999999
    get_classical_dict  =>  0.1330213
    Так как с версии Python 3.6 обычные словари обладают свойством запоминания последовательности заполнения его
элементами, то использование коллекции OrderedDict не имеет никакого смысла...  
'''