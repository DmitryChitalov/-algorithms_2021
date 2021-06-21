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


def time_decorator(func):
    def time_of_function(*args, **kwargs):
        start_time = time.time()
        return_value = func(*args, **kwargs)
        end_time = time.time()
        print(f'Время выполнения функции = {end_time - start_time}')
        return return_value
    return time_of_function


@time_decorator
def list_comprehension():  # O(1), но если n неизвестен, то O(n)
    lst = [i for i in range(1000000)]
    return lst


@time_decorator
def dict_list_comprehension():  # O(1), но если n неизвестен, то O(n)
    dictionary = {i: i for i in range(1000000)}
    return dictionary


# @time_decorator - решил закрепить рекурсию, но засечь общее время для всего алгоритма через декоратор никак не вышло
def list_recur(lst, count=1):  # O(1), но если n неизвестен, то O(2^n)
    if count == 995:
        return lst.append(random.randint(0, 100))
    else:
        lst.append(random.randint(0, 100))
        count += 1
        return list_recur(lst, count)


# @time_decorator - решил закрепить рекурсию, но засечь общее время для всего алгоритма через декоратор никак не вышло
def dict_recur(dictionary, count=1):  # O(1), но если n неизвестен, то O(2^n)
    if count == 995:
        return dictionary.update({chr(count): random.randint(0, 100)})
    else:
        dictionary.update({chr(count): random.randint(0, 100)})
        count += 1
        return dict_recur(dictionary, count)


@time_decorator
def delete_list(lst):        # O(n), но если не известно заранее количество итираций, то O(n^2)
    for i in range(1000):    # O(1)
        lst.pop(i)           # O(n)


@time_decorator
def delete_list_2(lst):    # O(1)
    for i in range(1000):
        lst.pop()


@time_decorator
def change_list(lst):  # O(n)
    for i in range(8000):
        lst[i] = lst[i] + 1


@time_decorator
def delete_dict(dictionary):  # O(1)
    for i in range(1000):
        dictionary.pop(i)


@time_decorator
def change_dict(dictionary):  # O(1)
    for i in range(1000, 8001):
        dictionary[i] = 'smth new'


my_list = []
my_dict = {}

start_list_recur = time.time()
list_recur(my_list)
end_list_recur = time.time()
print(f'Время выполнения функции рекурсии = {end_list_recur - start_list_recur}')


start_dict_recur = time.time()
dict_recur(my_dict)
end_dict_recur = time.time()
print(f'Время выполнения функции рекурсии = {end_dict_recur - start_dict_recur}')
#
my_list = list_comprehension()
my_dict = dict_list_comprehension()

delete_list(my_list)
delete_list_2(my_list)
change_list(my_list)

delete_dict(my_dict)
change_dict(my_dict)

"""
a) Среди рекурсий наилучшую скорость записи данных показали словари, т.к. словарь
является хэш-таблицей. Однако, среди comprehension выражений наибольшую скорость записи показали списки по неизвестной 
мне причине. 
b) Удаление и изменение элементов из словаря так же происходит быстрее, т.к. все операции по изменению или удалению 
данных из словаря имеют константную ассимптотическую сложность О(1)
"""


