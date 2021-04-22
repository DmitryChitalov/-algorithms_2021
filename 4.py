"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

my_dict = {str(i): i for i in range(1000)}
o_d_ex = OrderedDict(my_dict)


def get_d():
    my_dict.get('100')


def get_o_d():
    o_d_ex.get('100')


def pop_i_d():
    my_dict.popitem()


def pop_i_o_d():
    o_d_ex.popitem()


def u_d():
    my_dict.update({'100': 0})


def u_o_d():
    o_d_ex.update({'100': 0})


print('get')
print(timeit('get_d()', number=1000000, globals=globals()))
print(timeit('get_o_d()', number=1000000, globals=globals()))

print('popitem')
print(timeit('pop_i_d()', number=1000, globals=globals()))
print(timeit('pop_i_o_d()', number=1000, globals=globals()))

print('update')
print(timeit('u_d()', number=1000, globals=globals()))
print(timeit('u_o_d()', number=1000, globals=globals()))

'''
Вывод : не в одном из тестов 'OrderDict' не был быстрее , следовательно его использование нецелесообразно 
'''