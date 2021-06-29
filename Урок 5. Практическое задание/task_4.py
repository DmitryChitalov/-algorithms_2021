"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""


from collections import OrderedDict
from timeit import timeit


my_dict = {}
my_ord_dict = OrderedDict([])


def fill_dict(some_dict):
    for i in range(10000):
        some_dict[i] = i

def get_val(some_dict):
    temp_val = 0
    for i in range(10000):
        temp_val += some_dict[i]


print(timeit('fill_dict(my_ord_dict)', globals=globals(), number=1))    # 0.003580978999999998
print(timeit('fill_dict(my_dict)', globals=globals(), number=1))        # 0.002190554999999997

print(timeit('get_val(my_ord_dict)', globals=globals(), number=1))      # 0.0023833800000000044
print(timeit('get_val(my_dict)', globals=globals(), number=1))          # 0.002334229000000007

# Извлечение значений происходит приблизительно с равной скоростью.
# OrderDict не имеет смысла использовать на Python 3.6, поскольку на этой версии и далее обычный словарь
# способен выполнять те же функции, но при этом удобнее и работает быстрее в некоторых случаях