"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

import random
import time

LENGTH = 100000


def time_spent_decorator(func):

    def internal():
        start_time = time.time()
        res = func()
        print(time.time() - start_time)
        return res

    return internal


@time_spent_decorator
def fill_list() -> list:
    l = list()
    for i in range(LENGTH):
        x = random.randint(0, 100)
        l.append(x)
    return l


@time_spent_decorator
def fill_dict() -> dict:
    d = dict()
    for i in range(LENGTH):
        x = random.randint(0, 100)
        d[x] = x
    return d


@time_spent_decorator
def operations_list():
    l = fill_list()
    while len(l) != 0:
        l.pop()


@time_spent_decorator
def operations_dict():
    d = fill_dict()
    keys = list(d.keys())
    for key in keys:
        d.pop(key)


operations_dict()
print('operations_dict')
operations_list()
print('operations_list')