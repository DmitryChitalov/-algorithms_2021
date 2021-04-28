
"""
Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т. д.
"""

from memory_profiler import profile
from functools import reduce
from random import randint
from numpy import array
from timeit import default_timer



@profile
def func_1(my_list):
    y = 0
    for el in range(int(len(my_list)) // 2):
        my_list[y], my_list[y + 1] = my_list[y + 1], my_list[y]
        y += 2
    return my_list


func_1(list(range(100000)))

@profile
def func_2(my_list):
    y = 0
    for el in range(int(len(my_list)) // 2):
        my_list[y], my_list[y + 1] = my_list[y + 1], my_list[y]
        y += 2
    return my_list


func_2(array(list(range(100000))))


"""

Сначала  профилирование показало  32.1 MiB, для оптимизайии использовала numpy и уменьшилась память стало 29.9 MiB.
"""

"""
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. 
"""

@profile
def func_3(old_list):
    gen_list = [old_list[el + 1] for el in range(len(old_list) - 1)
                if old_list[el] < old_list[el + 1]]
    return gen_list


func_3([randint(100, 1000) for _ in range(100000)])



@profile
def func_4(my_list):
    new_list = array([my_list[el + 1] for el in range(len(my_list) - 1)
                      if my_list[el] < my_list[el + 1]])
    return new_list


func_4(array([randint(100, 1000) for _ in range(100000)]))

"""
Здесь также использовала numpy, сначало было  32.0 MiB, а стало  30.4 MiB.
"""

"""
Генератор только четных эллементов
"""


@profile
def func_5(my_list):
    new_list = [x for x in my_list if not x%2]
    return new_list

func_5(list(range(100000)))

@profile
def func_6(my_list):
    new_list = [x for x in my_list if not x%2]
    return new_list

func_6(array(list(range(100000))))

"""
Применила numpy, хорошо отработал. Было 32.3 MiB  и стало 29.4 MiB 
"""
