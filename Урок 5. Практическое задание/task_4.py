"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit
from random import randint

RAND_FROM = 1
RAND_TO = 10
DICT_NUM = 1000

def dict_fill(user_dict):
    user_dict = {i: randint(RAND_FROM, RAND_TO) for i in range(DICT_NUM)}
    return user_dict


def dict_get(user_dict):
    return user_dict.get(DICT_NUM - 1)


def dict_pop(user_dict):
    user_dict = {i: randint(RAND_FROM, RAND_TO) for i in range(DICT_NUM)}
    for i in range(DICT_NUM - 1):
        user_dict.pop(i)
    return user_dict


my_dict = {}
ord_dict = OrderedDict()
my_dict = dict_fill(my_dict)
ord_dict = dict_fill(ord_dict)

print(f"dict_fill(my_dict): {timeit('dict_fill(my_dict)', globals=globals(), number=1000)}")
print(f"dict_fill(ord_dict): {timeit('dict_fill(ord_dict)', globals=globals(), number=1000)}")

print(f"dict_get(my_dict): {timeit('dict_get(my_dict)', globals=globals(), number=100000)}")
print(f"dict_get(ord_dict): {timeit('dict_get(ord_dict)', globals=globals(), number=100000)}")

print(f"dict_pop(my_dict): {timeit('dict_pop(my_dict)', globals=globals(), number=1000)}")
print(f"dict_pop(ord_dict): {timeit('dict_pop(ord_dict)', globals=globals(), number=1000)}")

# разница во времени выполнения в пределах статистической погрешности
# смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях нет