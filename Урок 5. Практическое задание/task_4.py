"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

import collections
import timeit


# my_dict = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
# my_ordered_dict = collections.OrderedDict([('first', 1), ('second', 2), ('third', 3), ('fourth', 4)])

def make_dict():
    my_dict = {}
    for i in range(5000):
        my_dict[f'{i}'] = i
    return my_dict


def make_ordered_dict():
    my_ordered_dict = {}
    for i in range(5000):
        my_ordered_dict[f'{i}'] = i
    return my_ordered_dict


def for_dict(my_dict):
    my_dict['hello'] = 55
    my_dict['on'] = 120
    x = my_dict['2']
    return x


def for_ordered_dict(my_ordered_dict):
    my_ordered_dict['hello'] = 55
    my_ordered_dict['on'] = 120
    x = my_ordered_dict['2']
    return x


my_ordered_dict = make_ordered_dict()
my_dict = make_dict()
print('The time of the function "make_dict()" is :',
      timeit.timeit(
          "make_dict()",
          setup='from __main__ import make_dict',
          number=10000))
print('The time of the function "make_ordered_dict()" is :',
      timeit.timeit(
          "make_ordered_dict()",
          setup='from __main__ import make_ordered_dict',
          number=10000))
print('The time of the function "for_dict(my_dict)" is :',
      timeit.timeit(
          "for_dict(my_dict)",
          setup='from __main__ import for_dict,my_dict',
          number=10000))

print('The time of the function "for_ordered_dict(my_ordered_dict)" is :',
      timeit.timeit(
          "for_ordered_dict(my_ordered_dict)",
          setup='from __main__ import for_ordered_dict,my_ordered_dict',
          number=10000))

# В целом у меня быстрее выпольняется выполняется make_dict(), то есть работать с обычними словарями,
# нет смысла использовать OrderedDict в Python 3.6 и более поздних версиях, так как обычные словари уже "помнять"
# порядок и работают быстрее
