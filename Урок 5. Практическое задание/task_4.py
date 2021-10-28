#!/usr/bin/env python3

from timeit import timeit
from collections import OrderedDict

"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

d = dict()
od = OrderedDict()

number = 100000


def fill(d):
    for i in range(1000):
        d[i] = i


def get(d):
    for i in range(1000):
        d.get(i)


def profile_dict():
    print(f'#{"-" * 30} DICT {"-" * 30}#')
    for i in range(10):
        print(f'fill(dict): {timeit("fill(d)", globals=globals(), number=number)}')
    for i in range(10):
        print(f'get(dict): {timeit("get(d)", globals=globals(), number=number)}')


def profile_ordered_dict():
    print(f'#{"-" * 30} ORDEREDDICT {"-" * 30}#')
    for i in range(10):
        print(f'fill(OrderedDict): {timeit("fill(od)", globals=globals(), number=number)}')
    for i in range(10):
        print(f'get(OrderedDict): {timeit("get(od)", globals=globals(), number=number)}')


def main():
    profile_dict()
    profile_ordered_dict()


if __name__ == '__main__':
    main()

'''
#------------------------------ DICT ------------------------------#
fill(dict): 6.769630201000837
fill(dict): 6.608184030992561
fill(dict): 6.718776472000172
fill(dict): 6.9321143759880215
fill(dict): 6.907620325000607
fill(dict): 6.916411568003241
fill(dict): 6.940511833992787
fill(dict): 7.159243235000758
fill(dict): 6.873298571998021
fill(dict): 6.8899921940028435
get(dict): 7.984801432990935
get(dict): 7.671060905006016
get(dict): 7.58510982900043
get(dict): 7.624888734004344
get(dict): 7.570356301002903
get(dict): 7.483152846994926
get(dict): 7.682853955993778
get(dict): 7.966142420991673
get(dict): 8.084532414999558
get(dict): 7.812382281001192
#------------------------------ ORDEREDDICT ------------------------------#
fill(OrderedDict): 9.688025836003362
fill(OrderedDict): 9.95326742400357
fill(OrderedDict): 9.59180290599761
fill(OrderedDict): 9.584844803001033
fill(OrderedDict): 9.115120382004534
fill(OrderedDict): 9.817884627002059
fill(OrderedDict): 9.881273254999542
fill(OrderedDict): 9.743976698999177
fill(OrderedDict): 9.8162718579988
fill(OrderedDict): 10.014715613986482
get(OrderedDict): 8.645886767000775
get(OrderedDict): 8.123294963996159
get(OrderedDict): 8.227882469989709
get(OrderedDict): 8.464704277997953
get(OrderedDict): 8.242296953001642
get(OrderedDict): 8.187974707005196
get(OrderedDict): 8.377861232991563
get(OrderedDict): 8.5589798130095
get(OrderedDict): 8.379795341999852
get(OrderedDict): 8.485265023991815

Как видно из полученных данных работа с OrderedDict происходит медленнее нежели с dict.
С версии python 3.6 использование OrderedDict не имеет смысла т.к. dict так-же запоминает порядок.
Единственный вариант когда использование OrderedDict оправдано это если вы хотите явно показать что
в коде важен порядок следования элементов
'''
