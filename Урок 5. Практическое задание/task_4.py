"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

dicts = dict()
ordered_dicts = OrderedDict(dicts)


def range_list(numb, new_dict):
    for i in range(numb):
        new_dict[i] = i
        return new_dict


def update_ordered_dict(numb, new_ordered_dict):
    for i in range(numb):
        new_ordered_dict.update({i: i})
        return new_ordered_dict


def pop_dict(numb, new_dict):
    for i in range(numb):
        new_dict.pop(i, None)
        return new_dict


def pop_ordered_dict(numb, new_ordered_dict):
    for i in range(numb):
        new_ordered_dict.popitem(last=False)
        return new_ordered_dict


def change_dict(new_dict):
    for k, v in new_dict:
        v += 2
        return new_dict


def change_ordered_dict(new_ordered_dict):
    for k, v in new_ordered_dict:
        v += 2
        return new_ordered_dict


print(f"Время работы функции {range_list.__name__} составило "
      f"{timeit('range_list(100000, dicts)', globals=globals(), number=100000)} сек.")

print(f"Время работы функции {update_ordered_dict.__name__} составило "
      f"{timeit('update_ordered_dict(100000, ordered_dicts)', globals=globals(), number=100000)} сек.")

print(f"Время работы функции {pop_dict.__name__} составило "
      f"{timeit('pop_dict(80000, dicts)', globals=globals(), number=100000)} сек.")

print(f"Время работы функции {pop_ordered_dict.__name__} составило "
      f"{timeit('pop_ordered_dict(80000, ordered_dicts)', globals=globals(), number=100000)} сек.")

print(f"Время работы функции {change_dict.__name__} составило "
      f"{timeit('change_dict(dicts)', globals=globals(), number=100000)} сек.")

print(f"Время работы функции {change_ordered_dict.__name__} составило "
      f"{timeit('change_ordered_dict(ordered_dicts)', globals=globals(), number=100000)} сек.")

"""
Отчет teimeit:
Время работы функции range_list составило 0.1049211 сек.
Время работы функции update_ordered_dict составило 0.1058251 сек.
Время работы функции pop_dict составило 0.12682349999999953 сек.
Время работы функции pop_ordered_dict составило 0.15700826 сек.
Время работы функции change_dict составило 0.141789324 сек.
Время работы функции change_ordered_dict составило 0.06467240000000007 сек.
В целом работа dict и OrderedDict похоже, но dict не много быстрее, но здесь мне кажется, это зависит от
версии интепретатора и мне кажется, что OrderedDict уже устарешие алгоритмы, поэтому они проигрывают 
в производительноти. 

OrderedDict уже не нужен, так как уже устарел и потерял надобность в своем использовании.
"""