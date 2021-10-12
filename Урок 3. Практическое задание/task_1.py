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

import time


def check_speed_1(func):
    def wrapper(n):
        start_val = time.time()
        func(n)
        end_val = time.time()
        print(f'{func.__name__}')
        print(end_val - start_val)
        return func(n)

    return wrapper


def check_speed_2(func):
    def wrapper(argument_1, argument_2):
        start_val = time.time()
        func(argument_1, argument_2)
        end_val = time.time()
        print(f'{func.__name__}')
        print(end_val - start_val)
        return func(argument_1, argument_2)

    return wrapper


# A
@check_speed_1
def filling_dct(n):
    test_dct = dict()
    for el in range(n):
        test_dct[el] = el
    return test_dct


# filling_dct(5*10**6)


@check_speed_1
def filling_lst(n):
    test_lst = []
    for el in range(n):
        test_lst.append(el)
    return test_lst


# filling_lst(5*10**6)

# B


@check_speed_2
def dct_pop(test_dct, n):
    for el in range(n):
        test_dct.popitem()
    return test_dct


@check_speed_2
def lst_pop(test_lst, n):
    for el in range(n):
        test_lst.pop()
    return test_lst


# dct_pop(filling_dct(5*10**7), 5*10**4)
# lst_pop(filling_lst(5*10**7), 5*10**4)

@check_speed_1
def dct_summation(test_dct):
    res = 0
    for el in test_dct.values():
        res += el
    return res


@check_speed_1
def lst_summation(test_lst):
    res = 0
    for el in test_lst:
        res += el
    return res


dct_summation(filling_dct(5 * 10 ** 7))
lst_summation(filling_lst(5 * 10 ** 7))
