"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

simple_dict = dict()
not_simple_dict = OrderedDict()


def fill_1(dic):
    for i in range(100):
        dic[i] = f'{str(i)}a'
    return dic


# заполнение
print('заполнение')
print(timeit('fill_1(simple_dict)', globals=globals(), number=10000))  # 0.604726485        +
print(timeit('fill_1(not_simple_dict)', globals=globals(), number=10000))  # 0.6115800929999999

# получение элемента по ключу
print('# получение элемента по ключу')
print(timeit('simple_dict[99]', globals=globals(), number=100000))  # 0.008372079000000143
print(timeit('not_simple_dict[99]', globals=globals(), number=100000))  # 0.006928703000000036    +

# получение элемента get
print('получение элемента get')
print(timeit('simple_dict.get(99)', globals=globals(), number=10000))  # 0.0011756399999998113          +
print(timeit('not_simple_dict.get(99)', globals=globals(), number=10000))  # 0.0011888969999998

# вставка
print('вставка')
print(timeit('simple_dict[50]=2', globals=globals(), number=10000))  # 0.001535405999999906    +
print(timeit('not_simple_dict[50]=2', globals=globals(), number=10000))  # 0.0014000729999998907

# popitem
print('popitem')
print(timeit('simple_dict.popitem()', globals=globals(), number=90))  # 1.5945000000128218e-05   +
print(timeit('not_simple_dict.popitem()', globals=globals(), number=90))  # 2.264400000018263e-05

'''Вывод: при работе с хеш-таблицами лутше использовать dict и его функции.'''
