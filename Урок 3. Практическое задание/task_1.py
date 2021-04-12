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

import random
import time


def time_of_function(function):
    def wrapper(*args):
        start_val = time.time()
        function(*args)
        end_val = time.time()
        time_funk = end_val - start_val
        return time_funk
    return wrapper


my_list = []
my_dict = {}


@time_of_function
def list_app(i=1):
    for i in range(i):
        my_list.append(random.choice(range(1000, 10000000000)))
    return my_list


@time_of_function
def dict_app(i=1):
    for i in range(i):
        my_dict[i] = (random.choice(range(1000, 10000000000)))
    return my_dict


print(list_app(1000000))
print(dict_app(1000000))

"""
Время выполнения добавления элементов в словарь больше, чем в список,
из-за расчёта хеша для эллементов. 
"""