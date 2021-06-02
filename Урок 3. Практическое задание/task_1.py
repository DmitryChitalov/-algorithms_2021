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
from time import time_ns

my_list = []
my_dict = {}
my_dict2 = {}


def time_func(func):
    def the_wrapper(*args):
        t1 = time_ns()
        func(*args)
        t2 = time_ns()
        delta = t2 - t1
        print(f'Время выполнения функции: {func.__name__} - {delta}')
    return the_wrapper


@time_func
def list_gen(n):
    for i in range(n):
        my_list.append(i)
    return my_list


@time_func
def dict_gen(data):
    keys = range(len(data))
    for i in keys:
        for el in data:
            my_dict[i] = el
    return my_dict


@time_func
def dict2_gen(data):
    keys = range(len(data))
    el = 0
    for i in keys:
        my_dict2[i] = data[el]
        el += 1
    return my_dict2


@time_func
def search_dict(any_dict, arg):
    return any_dict.get(arg, 0)


@time_func
def search_lst(any_lst, arg):
    return any_lst.index(arg)


list_gen(20001)
dict_gen(my_list)
dict2_gen(my_list)
search_dict(my_dict2, 9900)
search_lst(my_list, 9900)

"""
list_gen: сложность O(n) время ~ 1022900
dict_gen2: сложность O(n) время ~ 1958200  почти в два раза медленнее списка, при одинаковой сложности
dict_gen: сложность O(n^2) время ~ 15167377300 самый медленный алгоритм
search_lst: сложность О(n) время - 0
search_dict: сложность О(1) время - 0

Дмитрий, скажите,  какой смысл от О большой при таких разницах во времени при одинаковой сложности или отсутсвии 
разницы при разной сложности?
"""