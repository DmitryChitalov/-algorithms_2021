"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict


def my_func_coll_dict_1(n=1000):
    for i in range(n):
        od1[str(i)] = i


def my_func_stock_dict_1(n=1000):
    for i in range(n):
        stock_DICT[str(i)] = i


def my_func_coll_dict_2(n=1000):
    for i in range(n):
        tmp_var = od1[str(i)]


def my_func_stock_dict_2(n=1000):
    for i in range(n):
        tmp_var = stock_DICT[str(i)]


od1 = OrderedDict()
stock_DICT = dict()

print(f'Сравнение заполнения OrderedDict и dict\n'
      f'OrderedDict: {timeit("my_func_coll_dict_1", globals=globals(), number=10000000)}'
      f' vs ' 
      f'dict: {timeit("my_func_stock_dict_1", globals=globals(), number=10000000)}\n')

print(f'Сравнение deq_obj.popleft() и list_obj.pop(0)\n'
      f'popleft(): {timeit("my_func_coll_dict_2", globals=globals(), number=10000000)}'
      f' vs ' 
      f'pop(0): {timeit("my_func_stock_dict_2", globals=globals(), number=10000000)}\n')

"""
Аналитика:
Сравнение заполнения OrderedDict и dict
OrderedDict: 0.7498311999999999 vs dict: 1.0080711999999998

Сравнение deq_obj.popleft() и list_obj.pop(0)
popleft(): 0.9657938000000001 vs pop(0): 0.6746434999999997

OrderedDict показал себя несколько быстрее чем обычный словарь. 
Если замеры верные, то использовать его стоит, когда есть необходимость экономить ресурсы.
"""