"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict


def items(test):
    return test.items()


def copy(test):
    return test.copy()


def values(test):
    return test.values()


test_dict = {'Key_' + str(i - 999): i for i in range(1, 9999)}
test_ordered_dict = OrderedDict(test_dict)

dict_1 = copy(test_dict)
dict_2 = copy(test_dict)
ord_dict_1 = copy(test_ordered_dict)
ord_dict_2 = copy(test_ordered_dict)

print(f"values(dict): {timeit('values(test_dict)', globals=globals(), number=10000)} ")
print(f"values(ord_dict): {timeit('values(test_ordered_dict)', globals=globals(), number=10000)}")
print(f"items(dict): {timeit('items(test_dict)', globals=globals(), number=10000)} ")
print(f"items(ord_dict): {timeit('items(test_ordered_dict)', globals=globals(), number=10000)}")
print(f"copy(dict): {timeit('copy(test_dict)', globals=globals(), number=10000)} ")
print(f"copy(ord_dict): {timeit('copy(test_ordered_dict)', globals=globals(), number=10000)}")


"""
В новых версиях Python нет необходимости в OrderedDict, т.к. начиная с 3.6 словари и так упорядочные. А copy
выполняется еще и медленее
"""