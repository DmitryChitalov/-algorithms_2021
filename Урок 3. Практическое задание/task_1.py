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

first_list = []
first_dictionary = {}
number_operations = 10000000


def time_decorator(function):
    def time_count(*args):
        start = time.time()
        function(*args)
        end = time.time()
        time_work = end - start
        print(time_work)
    return time_count


@time_decorator
def append_list(lst, x):
    for i in range(x):
        lst.append(i)
    print('время заполнения списка - ')
    return lst


@time_decorator
def append_dictionary(dictionary, x):
    for i in range(x):
        dictionary[i] = i
    print('время заполнения словаря - ')
    return dictionary


append_list(first_list, number_operations)
append_dictionary(first_dictionary, number_operations)

"""список работает быстрее словаря из-за расчёта хеша для эллементов"""
