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


def time_of_func(func):
    def wrapped(*args):
        start_time = time.time()
        res = func(*args)
        print(f'Время выполнения {func.__name__} {time.time() - start_time}')
        return res

    return wrapped


@time_of_func
def filling_list(list, n):
    for i in range(n):
        list.append(i)
    return list


@time_of_func
def filling_dict(dict, n):
    for i in range(n):
        dict[i] = i
    return dict


@time_of_func
def find_el_in_list(list, el):
    if el in list:
        return "Элемент найден"
    else:
        return "Элемент не найден"

@time_of_func
def find_el_in_dict(dict, el):
    if el in dict:
        return "Элемент найден"
    else:
        return "Элемент не найден"


l = filling_list([], 20000000)
d = filling_dict({}, 20000000)
print(find_el_in_list(l, 18888888))
print(find_el_in_dict(d, 18888888))

""" Заполнение списка и словаря занимает примерно одно и тоже время, т.к. сложность операции одинаковая O(1).
    При этом операции поиска в словаре значительно быстрее, так как словарь представляет из себя 
    хеш таблицу"""