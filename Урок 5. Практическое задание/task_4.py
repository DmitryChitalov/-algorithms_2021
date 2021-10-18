"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict

num = 100000
my_dict = dict()
for i in range(num):
    my_dict[num] = num
my_o_dict = OrderedDict()
for i in range(num):
    my_dict[num] = num


def new_dict(num):
    my_dict_1 = dict()
    for i in range(num):
        my_dict_1[num] = num


def new_o_dict(num):
    my_dict_1 = OrderedDict()
    for i in range(num):
        my_dict_1[num] = num


def get_dict(my_dict):
    for i in range(len(my_dict)):
        item = my_dict.get(i)

def get_o_dict(my_o_dict_1):
    for i in range(len(my_o_dict_1)):
        item = my_o_dict_1.get(i)


print(f"new_dict({num}): ",
      timeit(f"new_dict({num})", globals=globals(), number=1000))
print(f"new_o_dict({num}): ",
      timeit(f"new_o_dict({num})", globals=globals(), number=1000))


print(f"get_dict(my_dict1): ",
      timeit(f"get_dict(my_dict)", globals=globals(), number=1000))
print(f"get_o_dict(my_o_dict1): ",
      timeit(f"get_o_dict(my_o_dict)", globals=globals(), number=1000))


"""
new_dict(100000):  3.3567807000000003
new_o_dict(100000):  4.4613515
Заполнение обычного словаря происходит быстрее, чем OrderedDict.
get_dict(my_dict1):  0.00024170000000012237
get_o_dict(my_o_dict1):  0.00016139999999964516
Получение элемента происходит практически с одинаковой скоростью.
Вывод: применение OrderedDict в Python 3.6 и более поздних версиях не имеет смысла.
"""
