"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
from random import randrange
from collections import OrderedDict

def gen_dict(num_el):
    return {c: c * 3 for c in range(num_el)}

def gen_ordered_dict(num_el):
    return OrderedDict({c: c * 3 for c in range(num_el)})

def dict_key(dict):
    for i in range(len(dict)):
        if i == 5678:
            k = dict[i]
    return 0

def dict_value(dict):
    for i in dict.values():
        if i == 17034:
            k = i
    return 0

num = 10000

print(timeit('gen_dict(num)', globals = globals(), number = 1000))
print(timeit('gen_ordered_dict(num)', globals = globals(), number = 1000))
# 0.786497923
# 2.090535697
# создание обычного словаря отработало быстрее

dict = gen_dict(num)
o_dict = gen_ordered_dict(num)

print(timeit('dict_key(dict)', globals = globals(), number = 1000))
print(timeit('dict_key(o_dict)', globals = globals(), number = 1000))
# 0.3192115430000002
# 0.31607607500000023
# Поиск по индексу отработал примерно одинаково

print(timeit('dict_value(dict)', globals = globals(), number = 1000))
print(timeit('dict_value(o_dict)', globals = globals(), number = 1000))
# 0.23860143600000017
# 0.428546259
# Поиск по значению отработал на обычном словаре быстрее

# Особого сымсла использовать Ordered_dict в настоящем времени не вижу, если только не придётся поддерживать код на старом питоне

