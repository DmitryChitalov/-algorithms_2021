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


import time
from random import randint


def time_measure(func):
    def wrapper(n):
        time_start = time.time()
        result = func(n)
        time_stop = time.time()
        print(f"Время выполнения {func.__name__}: ", time_stop - time_start)
        return result
    return wrapper


def source_sequence(n):
    for _ in range(n):
        yield randint(-100, 100)


@time_measure
def fill_list(n):
    res_list = []
    for number in source_sequence(n):
        res_list.append(number)
    return res_list


@time_measure
def fill_dict(n):
    res_dict = {}
    for i, number in enumerate(source_sequence(n)):
        res_dict[i] = n
    return res_dict

'''
Заполнение списка и словаря у меня получилось примерно одинаково. До 10000 значений список выполняется быстрее,
далее словарь заполняется быстрее. Для милиона значений:
Время выполнения fill_list:  1.2446677684783936
Время выполнения fill_dict:  1.0761220455169678

'''

fill_list(1000000)
fill_dict(1000000)

