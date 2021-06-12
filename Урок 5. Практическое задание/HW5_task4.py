"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import default_timer
from collections import OrderedDict

a_dict = {}
an_ordered_dict = OrderedDict()
n = 10 ** 4


def time_decorator(my_func):

    def wrapper(*args, **kwargs):
        start = default_timer()
        my_result = my_func(*args, **kwargs)
        print(f'Время выполенения функции {my_func.__name__} составляет {default_timer() - start}.')

        return my_result

    return wrapper


@time_decorator
def make_dict(dict_current, num):
    for i in range(num):
        dict_current[i] = i
    return  dict_current


@time_decorator
def make_ordered_dict(dict_current, num):
    for i in range(num):
        dict_current[i] = i
    return dict_current

@time_decorator
def remake_dict(dict_current, num):
    for i in range(num):
        dict_current.pop(i)
    for j in range(num):
        dict_current[j] = f'fill{j}'
    return dict_current

@time_decorator
def remake_ordered_dict(dict_current, num):
    for i in range(num):
        dict_current.pop(i)
    for j in range(num):
        dict_current[j] = f'fill{j}'
    return dict_current


a_dict = make_dict(a_dict, n)
an_ordered_dict = make_ordered_dict(an_ordered_dict, n)
a_dict = remake_dict(a_dict, n)
an_ordered_dict = remake_ordered_dict(an_ordered_dict, n)


"""
результаты
Время выполенения функции make_dict составляет 0.001079500000000004.
Время выполенения функции make_ordered_dict составляет 0.0015788999999999942.
Время выполенения функции remake_dict составляет 0.0031607999999999983.
Время выполенения функции remake_ordered_dict составляет 0.0049774.

итого работа с упорядоченным словарем незначительно медленнее, чем с обычным

