"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


def dict_insert(new_dict):
    for value in range(10000):
        new_dict[value] = value
    return new_dict


def dict_search(some_dict):
    return some_dict.get(99)


def dict_pop(my_dict):
    some_dict = dict_insert(my_dict)
    for i in range(1, 50):
        some_dict.pop(i)
    return some_dict


simple_dict = {}
ord_dict = OrderedDict()
simple_dict = dict_insert(simple_dict)
ord_dict = dict_insert(ord_dict)

print(timeit('dict_insert(simple_dict)', globals=globals(), number=10000))  # 6.107180100000001
print(timeit('dict_insert(ord_dict)', globals=globals(), number=10000))  # 8.6580963

print(timeit('dict_search(simple_dict)', globals=globals(), number=100000))  # 0.010118999999999545
print(timeit('dict_search(ord_dict)', globals=globals(), number=100000))  # 0.011166899999999202

print(timeit('dict_pop(simple_dict)', globals=globals(), number=10000))  # 6.3426343
print(timeit('dict_pop(ord_dict)', globals=globals(), number=10000))  # 9.092448399999999

"""
По итогам замеров времени работы операций с обычным словарем и OrderedDict
вывод следующий - время работы сопоставимо, а в некоторых случаях обычный словарь быстрее. 
Смысла использовать OrderedDict в последних версиях Python нет.
"""
