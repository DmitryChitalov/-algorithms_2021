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
from time import time


def time_func(func):
    def the_wrapper(*arg):
        t1 = time()
        res = func(*arg)
        delta = time() - t1
        print(f'Время выполнения функции: {func.__name__} - {delta}')
        return res

    return the_wrapper


@time_func
def func_with_list(n):
    list_fulling = []
    for i in range(n):
        list_fulling.append(i)
    return list_fulling


@time_func
def even_list(list_reg):
    for i in range(len(list_reg)):
        list_reg[i] *= 2


@time_func
def insert_new_in_list(n, list_need):
    for i in range(n):
        list_need.insert(i - 2, i)


@time_func
def pop_list(list_pop):
    len_list = round(len(list_pop) / 2)
    for i in range(len_list):
        list_pop.pop(i)


@time_func
def func_with_dict(n):
    dict_new = {}
    for i in range(n):
        dict_new[i] = i + 1
    return dict_new


@time_func
def even_dict(dict_user):
    for i in dict_user.keys():
        dict_user[i] *= 2


@time_func
def insert_dict(dict_reg, n):
    for i in range(n):
        dict_reg[i * 32] = i * 21


@time_func
def remove_dict(dict_reg):
    len_of_dict = round(len(dict_reg) / 2)
    for i in range(len_of_dict):
        dict_reg.pop(i)


print(f'{"-" * 30}list{"-" * 30}')
list_func = func_with_list(100000)
insert_new_in_list(1000, list_func)
even_list(list_func)
pop_list(list_func)

print(f'{"-" * 30}dict{"-" * 30}')
dict_func = func_with_dict(100000)
insert_dict(dict_func, 1000)
even_dict(dict_func)
remove_dict(dict_func)

"""Быстрее выполняются операции со словарями, потому что большинство операция имеют константную сложность, 
в отличии от операций над списками"""
