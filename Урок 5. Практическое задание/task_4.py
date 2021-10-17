"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""


import collections

NEW_DICT = {}
NEW_DICT_ord = collections.OrderedDict()
n = 1000000


def timer(func):
    import time
    def wrapper(*arg):
        start = time.time()
        func(*arg)
        end = time.time()
        print(f'время выполнения - {end - start} \n')

    return wrapper


@timer
def test1(NEW_DICT):
    NEW_DICT = {a: a for a in range(n)}
    print('заполнение обычного словаря')


@timer
def test2(NEW_DICT_ord):
    NEW_DICT_ord = {a: a for a in range(n)}
    print('заполнение OrderedDict словаря')


NEW_DICT1 = {str(a): a for a in range(n)}


@timer
def test3(NEW_DICT1):
    print(NEW_DICT1['1'])
    print('получение элемента обычного словаря')


NEW_DICT_ord1 = {str(a): a for a in range(n)}


@timer
def test4(NEW_DICT1):
    print(NEW_DICT_ord1['1'])
    print('получение элемента OrderedDict словаря')


test1(NEW_DICT)
test2(NEW_DICT_ord)
test3(NEW_DICT1)
test4(NEW_DICT_ord1)
'''
OrderedDict словарь работает быстрее
'''
