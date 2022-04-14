from collections import OrderedDict
from timeit import timeit

new_dict = {}  # обычный словарь
new_ordered_dict = OrderedDict()  # OrderedDict
n = 10000


def dict_func_2(n):
    for i in range(n):
        new_dict[i] = i

def dict_func_3(n):
    for i in range(n):
        new_dict.pop(i)

def dict_func_4(n):
    for i in range(n):
        new_dict[i] = "1"






def ordered_dict_func_2(n):
    for i in range(n):
        new_ordered_dict[i] = i

def ordered_dict_func_3(n):
    for i in range(n):
        new_ordered_dict.pop(i)

def ordered_dict_func_4(n):
    for i in range(n):
        new_ordered_dict[i] = "1"



print(timeit("dict_func_2", globals=globals(),number=1000))
print(timeit("ordered_dict_func_2", globals=globals(),number=1000))
print(timeit("dict_func_3", globals=globals(),number=1000))
print(timeit("ordered_dict_func_3", globals=globals(),number=1000))
print(timeit("dict_func_4", globals=globals(),number=1000))
print(timeit("ordered_dict_func_4", globals=globals(),number=1000))


""" Результаты измерений:
---- Добавление элементов ----
1.9700000000004436e-05
1.9499999999998685e-05
---- Удаление элементов ----
1.9500000000005624e-05
1.9499999999998685e-05
---- Замена элементов ----
1.8199999999999467e-05
1.8299999999998873e-05

Исходя из замеров они работают практически идентично. Но ordereddict работает немного быстрее на диапазоне 10000
Смысла использовать OrderedDict в версии python 3.6 и выше нет
"""