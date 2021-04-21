"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""
from random import randint
from timeit import Timer


def fill_dict():
    dict_obj = {}
    long = randint(3, 30)
    for i in range(long):
        dict_obj[i] = randint(-200, 200)
    return dict_obj


def fill_list():
    list_obj = []
    long = randint(3, 30)
    for i in range(long):
        list_obj.append(randint(-200, 200))
    return list_obj


t_dict = Timer("fill_dict()", "from __main__ import fill_dict")
print("Filling dict - ", t_dict.timeit(number=1000000), "seconds")

t_list = Timer("fill_list()", "from __main__ import fill_list")
print("Filling list - ", t_list.timeit(number=1000000), "seconds")
"""
Большой разницы не выявлено
Filling dict -  9.637264 seconds
Filling list -  9.761187600000001 seconds
"""


def dict_clear():
    some_dict = {'hello': 'bye', 'good morning': 'good evening'}
    some_dict.clear()


def list_clear():
    some_list = ['hello', 'bye']
    some_list.clear()


def dict_copy():
    some_dict = {'hello': 'bye', 'good morning': 'good evening'}
    some_dict.copy()


def list_copy():
    some_list = ['hello', 'bye']
    some_list.copy()


t1 = Timer("dict_clear()", "from __main__ import dict_clear")
print("dict clear", t1.timeit(number=100000), "seconds")

t2 = Timer("list_clear()", "from __main__ import list_clear")
print("list clear", t2.timeit(number=100000), "seconds")

t3 = Timer("dict_copy()", "from __main__ import dict_copy")
print("dict copy", t3.timeit(number=100000), "seconds")

t4 = Timer("list_copy()", "from __main__ import list_copy")
print("list copy", t4.timeit(number=100000), "seconds")
"""
Со словарем операции выполняются дольше
dict clear 0.01358380000000281 seconds
list clear 0.009437299999998316 seconds
dict copy 0.01894360000000006 seconds
list copy 0.01219989999999882 seconds
"""